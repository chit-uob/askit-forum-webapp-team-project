<template>
<div class="m-2">
  <div>Add members to {{ $route.params.mod }}</div>
  <div>
    <div>All users</div>
    <div>
      <div class=" grid-cols-4 grid">
        <div>Full name</div>
        <div>Email</div>
        <div>Member</div>
        <div>Admin</div>
      </div>
      <div class="h-16 overflow-y-scroll scroll ">
        <div class=" grid-cols-4 grid " v-for="(user, index) in users">
          <div class="truncate">{{ user.first_name }} {{ user. last_name }}</div>
          <div class="truncate">{{ user.email }}</div>
          <div><input type="checkbox" name="member" :id="`member_`+user.email" :checked="user.member" v-on:click="membersChecked(index)"></div>
          <div><input type="checkbox" name="admin" :id="`admin_`+user.email" :checked="user.admin" v-on:click="adminsChecked(index)"></div>
        </div>
      </div>
      <button v-on:click="update" type="button" class="p-2 my-2 rounded border-black border-2">Update</button>
    </div>
  </div>
</div>
</template>
  
  <script>
  import axiosClient from "@/views/axiosClient";

  export default {
    name: "addMembersView",
    data() {
    return {
      users: [],
      admin:[],
      member:[]
    };
  },
  mounted() {
    axiosClient({
      method: "get",
      url: `/module/${this.$route.params.mod}/getUsers`,
    })
        .then((response) => {
          console.log(response)
          this.users = response.data
          for (let i = 0; i < this.users.length; i++){
            this.admin[i] = this.users[i].admin 
            this.member[i] = this.users[i].member 
          } 
        })
        .catch((error) => {
          console.log(error);
        });
      },
    methods: {
    
      update(){
        console.log("updating...")
        var updatedUsers = []
        for(let i = 0; i < this.users.length; i++){
          console.log(i)
          if((this.users[i].admin != this.admin[i] ) || (this.users[i].member != this.member[i])){
            const data = {
              email: this.users[i].email,
              member: this.member[i],
              admin: this.admin[i]
            }
            this.users[i].admin = this.admin[i]
            this.users[i].member = this.member[i]
            updatedUsers.push(data)
          }
        }
        console.log(updatedUsers)
        axiosClient.post(
            `/module/${this.$route.params.mod}/updateRoles`, updatedUsers
          )
          .then((response) => {
            console.log(response)
            
          })
          .catch((error) => {
            console.log(error);
          });

      },
      membersChecked(pos){
        this.member[pos] = !this.member[pos]
        console.log(this.member[pos])
      },
      adminsChecked(pos){
        this.admin[pos] = !this.admin[pos]
        console.log(this.admin[pos])
      }

    }
  }
  
  </script>
  
  <style scoped>
  
  </style>
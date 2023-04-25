<template>
<div class="p-10 dark:bg-slate-900">
  <div class=" text-4xl mb-3">Add members to {{ $route.params.mod }}</div>
  <div>
    <div class="text-xl">All users</div>
    <div class=" dark:bg-gray-800 rounded border-2 dark:border-white border-black p-2 shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff]">
      <div class="  grid-cols-4 font-medium  grid border-b-2 border-black" >
        <div>Full name</div>
        <div>Email</div>
        <div class="text-center">Member</div>
        <div class="text-center">Admin</div>
      </div>
      <div class="h-64 overflow-y-scroll scroll ">
        <div class=" grid-cols-4 grid p-1 " :class="colour(index)" v-for="(user, index) in users">
          <div class="truncate">{{ user.first_name }} {{ user. last_name }}</div>
          <div class="truncate">{{ user.email }}</div>
          <div class="justify-self-center"><input class="transition focus:ring-4 focus:outline-none focus:ring-blue-400"  type="checkbox" name="member" :id="`member_`+user.email" :checked="user.member" v-on:click="membersChecked(index)"></div>
          <div class="justify-self-center"><input class="transition focus:ring-4 focus:outline-none focus:ring-blue-400" type="checkbox" name="admin" :id="`admin_`+user.email" :checked="user.admin" v-on:click="adminsChecked(index)"></div>
        </div>
      </div>
    </div>   
    <div class="flex"> 
      <button v-on:click="update" type="button" class="dark:shadow-[3px_3px_0px_0px_#ffffff] dark:border-0 shadow-[3px_3px_0px_0px_#000000] focus:ring-4 focus:outline-none focus:ring-pink-400 p-2 my-2 rounded border-black border-2 bg-blue-500 text-white hover:bg-blue-600 transition" >Update</button>
      <div v-if="success" class="mx-5 self-center text-lg text-green-700 font-medium">Success!</div>
    </div>
    <div class="my-4">
      <label class="text-lg font-medium">Add/Remove members by email</label>
      <input type="text" placeholder="Add multiple emails seperated by commas e.g: (person1@email.com,person2@email.com)" id="default-input" v-model="usersCSV" class="transition shadow-[3px_3px_0px_0px_#000000] bg-gray-50 text-gray-900 text-sm rounded-lg focus:outline-none focus:ring-4 focus:ring-blue-400 focus:border-blue-500 block w-full p-2.5 border-2 border-black dark:border-white dark:bg-gray-800" >
      <div class="flex">
        <button v-on:click="addMembers(false)" type="button" class="shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff] dark:border-0 focus:ring-4 focus:outline-none focus:ring-pink-400 p-2 my-2 mr-2 rounded border-black border-2 bg-blue-500 text-white hover:bg-blue-600 transition" >Add</button>
        <button v-on:click="addMembers(true)" type="button" class="shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff] dark:border-0 focus:ring-4 focus:outline-none focus:ring-pink-400 p-2 my-2 rounded border-black border-2 bg-red-700 text-white hover:bg-red-800 transition" >Remove</button>
        <div v-if="membersAddShow" class="mx-5 self-center text-lg font-medium">{{ successFromMembersAdd }} success, {{ failFromMembersAdd }} failed <span class="text-sm text-gray-500">(refresh the page to see changes)</span></div>
      </div>
    </div>
    <div class="my-4">
      <label class="text-lg font-medium">Add/Remove admins by email</label>
      <input type="text" placeholder="Add multiple emails seperated by commas e.g: (person1@email.com,person2@email.com)" id="default-input" v-model="adminsCSV" class=" transition shadow-[3px_3px_0px_0px_#000000] bg-gray-50 text-gray-900 text-sm rounded-lg focus:outline-none focus:ring-4 focus:ring-blue-400 focus:border-blue-500 block w-full p-2.5 border-2 border-black dark:border-white dark:bg-gray-800" >
      <div class="flex">
        <button v-on:click="addAdmins(false)" type="button" class="shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff] dark:border-0 focus:ring-4 focus:outline-none focus:ring-pink-400 p-2 my-2 mr-2 rounded border-black border-2 bg-blue-500 text-white hover:bg-blue-600 transition" >Add</button>
        <button v-on:click="addAdmins(true)" type="button" class="shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff] dark:border-0 focus:ring-4 focus:outline-none focus:ring-pink-400 p-2 my-2 rounded border-black border-2 bg-red-700 text-white hover:bg-red-800 transition" >Remove</button>
        <div v-if="adminsAddShow" class="mx-5 self-center text-lg font-medium">{{ successFromAdminsAdd }} success, {{ failFromAdminsAdd }} failed <span class="text-sm text-gray-500">(refresh the page to see changes)</span></div>
      </div>
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
      usersCSV: "",
      adminsCSV: "",
      successFromMembersAdd: 0,
      successFromAdminsAdd: 0,
      failFromMembersAdd: 0,
      failFromAdminsAdd: 0,
      membersAddShow: false,
      adminsAddShow: false,
      users: [],
      admin:[],
      member:[],
      success: false
    };
  },
  mounted() {
    axiosClient({
      method: "get",
      url: `/module/${this.$route.params.mod}/getUsers`,
    })
        .then((response) => {
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
      successTimer(){
        this.success = true
        var that = this;
        setTimeout(function() {that.success=false},3000)
      },
      colour(index){
        if(index%2==0){
          return "bg-white dark:bg-gray-800"
        }
        else{
          return "bg-gray-200 dark:bg-gray-700"
        }
      },
      update(){
        var updatedUsers = []
        for(let i = 0; i < this.users.length; i++){
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
        if(updatedUsers.length != 0){
        axiosClient.post(
            `/module/${this.$route.params.mod}/updateRoles`, updatedUsers
          )
          .then((response) => {
            this.successTimer()
            console.log(response)
            
          })
          .catch((error) => {
            console.log(error);
          });
        }
      },
      membersChecked(pos){
        this.member[pos] = !this.member[pos]
      },
      adminsChecked(pos){
        this.admin[pos] = !this.admin[pos]
      },
      addMembers(remove){
        this.membersAddShow = false
        var updatedUsers=this.usersCSV.split(',')
        var url = `/module/${this.$route.params.mod}/updateMembers`
        if(remove) url = `/module/${this.$route.params.mod}/removeMembers`
        axiosClient.post(
            url, updatedUsers
          )
          .then((response) => {
            this.successFromMembersAdd = response.data.success
            this.failFromMembersAdd = response.data.fail
            this.membersAddShow=true
            console.log(response)
            
          })
          .catch((error) => {
            console.log(error);
          });
      },
      addAdmins(remove){
        this.adminsAddShow = false
        var updatedUsers=this.adminsCSV.split(',')
        var url = `/module/${this.$route.params.mod}/updateAdmins`
        if (remove) url = `/module/${this.$route.params.mod}/removeAdmins`
        axiosClient.post(
            url , updatedUsers
          )
          .then((response) => {
            this.successFromAdminsAdd = response.data.success
            this.failFromAdminsAdd = response.data.fail
            this.adminsAddShow=true
            console.log(response)
            
          })
          .catch((error) => {
            console.log(error);
          });
      }

    }
  }
  
  </script>
  
  <style scoped>
  
  </style>
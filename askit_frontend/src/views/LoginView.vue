<template>
  <div class="bg-gray-100 min-h-screen flex flex-col justify-center items-center">
    <div class="flex items-center flex-wrap mb-8">
      <h1 class="text-6xl font-bold text-center font-sans text-black mr-8">ASK.IT</h1>
      <form @submit.prevent="submitForm" class="bg-white p-8 rounded-lg shadow-md w-96">
        <h1 class="text-3xl font-bold mb-8 text-center">Log in</h1>
        <div class="mb-4">
          <label for="username" class="block text-gray-700 font-bold mb-2">Username</label>
          <input type="email" name="username" v-model="username" placeholder="Email" class="border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400">
        </div>
        <div class="mb-4">
          <label for="password" class="block text-gray-700 font-bold mb-2">Password</label>
          <input type="password" name="password" v-model="password" placeholder="Password" class="border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400">
        </div>
        <div class="mb-2">
        <button type="submit" class="bg-blue-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline hover:bg-blue-600">Log in</button>
        </div>
        <div>
        <a href="/sign-up/">Don't have an account sign up!</a>
        </div>
      </form>
      
    </div>
  </div>
</template>





<!--<template>-->
<!--    <div class="">-->
<!--        <h1>Log in</h1>-->

<!--        <form @submit.prevent="submitForm">-->
<!--            <label for="username">Username</label>-->
<!--            <input type="email" name="username" v-model="username" class="border-2">-->
<!--            <label for="password">Password</label>-->
<!--            <input type="password" name="password" v-model="password" class="border-2">-->
<!--            <button type="submit" class="bg-blue-300">Log in</button>-->
<!--        </form> -->
<!--    </div>-->
<!--</template>-->

<script>
import axiosClient from './axiosClient';

export default {
    name: 'LoginView',
    data(){
        return{
            username: '',
            password: '',
        }
    },
    methods: {
        submitForm(e) {
            const formData = {
                username: this.username,
                password: this.password
            }

            axiosClient.post('/v1/token/login/', formData)
            .then(response =>{
                console.log(response)

                const token = response.data.auth_token

                this.$store.commit('setToken', token)

                axiosClient.defaults.headers.common['Authorization'] = "Token " + token

                localStorage.setItem("token", token)
                this.$router.push('/')
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
      
}
</script>
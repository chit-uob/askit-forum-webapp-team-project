<template>
  <div class="bg-gradient-to-r from-cyan-100 to-blue-500 min-h-screen flex flex-col justify-center items-center">
    <div class="flex items-center flex-wrap mb-8">
      <h1 class="text-8xl font-bold text-center font-sans text-black mr-8">ASK.IT</h1>
      <form @submit.prevent="submitForm" class="bg-gray-100 p-8 rounded-lg shadow-md w-96">
        <h1 class="text-3xl font-bold mb-8 text-center">Sign up</h1>
        <div class="mb-2">
          <label for="username" class="block text-gray-700 font-bold mb-1">Email</label>
          <input :class="validEmail" type="email" name="username" v-model="username" placeholder="Email"
                 class="border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400">
        </div>
        <div class="mb-2">
          <label for="firstname" class="block text-gray-700 font-bold mb-1">First name</label>
          <input type="text" name="firstname" v-model="firstname" placeholder="First name"
                 class="border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400 ">
        </div>
        <div class="mb-2">
          <label for="lastname" class="block text-gray-700 font-bold mb-1">Last name</label>
          <input type="text" name="lastname" v-model="lastname" placeholder="Last name"
                 class="border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400">
        </div>
        <div class="mb-2">
          <label for="password" class="block text-gray-700 font-bold mb-1">Password</label>
          <input :class="invalidPasswordBox" type="password" name="password" v-model="password" placeholder="Password"
                 class="border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400">
        </div>
        <div class="mb-3">
          <p class="text-gray-700 font-bold mb-2"> By signing up, you agree to our <a href="/privacy" target="_blank" class="text-blue-400 hover:underline hover:text-blue-500">Privacy Policy</a>.</p>
        </div>
        <div class="mb-3">
          <button :disabled="!isValidEmail || isFormComplete" type="submit"
                  class="bg-blue-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline hover:bg-blue-600 disabled:bg-gray-500">
            Sign up
          </button>
          <label v-if="invalid" class="text-red-600 pl-4">{{ errorMessage }}</label>
        </div>
        <div>
          <label class="text-black">Already have an account? </label><a href="/log-in/" class="text-blue-400 hover:underline hover:text-blue-500">Log in!</a>
        </div>
      </form>
    </div>
  </div>
</template>


<!--<template>-->
<!--    <div >-->
<!--        <h1>Sign up</h1>-->
<!--        <form @submit.prevent="submitForm">-->
<!--            <label for="username">Username</label>-->
<!--            <input type="email" name="username" v-model="username" placeholder="email"  class="border-2">-->
<!--            <label for="password">Password</label>-->
<!--            <input type="password" name="password" v-model="password" placeholder="password" class="border-2">-->
<!--            <button type="submit"  class="bg-blue-300">Sign up</button>-->
<!--        </form>-->
<!--    </div>-->
<!--</template>-->
<script>
import axiosClient from './axiosClient';

export default {
  name: 'SignUpView',
  data() {
    return {
      username: '',
      password: '',
      firstname: '',
      lastname: '',
      validEmail: '',
      invalid: false,
      invalidPasswordBox: '',
      errorMessage: ''
      
    }
  },
  computed: {
    isValidEmail() {
      if(/^[^@]+@\w+(\.\w+)+\w$/.test(this.username)){
        this.validEmail = 'border-green-500 focus:ring-green-400'
        return true
      }
      else{ 
        this.validEmail = 'focus:ring-blue-400 border-gray-200'
        return false
      }
    },
    isFormComplete(){
      return (this.username === '') || (this.password === '') || (this.firstname === '') || (this.lastname === '');
    }
  },
  methods: {
    submitForm(e) {
      console.log(this.lastname)
      axiosClient.post('/v1/users/', {
        username: this.username,
        email: this.username,

        password: this.password
      })
          .then(response => {
            
            axiosClient.post(`/signup/`, {
              username: this.username,
              first_name: this.firstname,
              last_name: this.lastname,
            })
            console.log(this.$route.query.redirect)
            this.$router.push({name: 'LogIn', query: {redirect: this.$route.query.redirect}})
            console.log(response)
          })
          .catch(error => {
            console.log(error)
            if(Object.values(error.response.data)[0][0] == "A user with that username already exists."){
              this.errorMessage = "Email already in use."
            }
            else {
              this.errorMessage = Object.values(error.response.data)[0][0]
              this.invalidPasswordBox= 'border-red-500 focus:ring-red-100'
            }
            this.invalid = true
            
          })
    }
  }
}
</script>
<template>
  <div class="bg-gray-100 min-h-screen flex flex-col justify-center items-center">
    <div class="flex items-center flex-wrap mb-8">
      <h1 class="text-6xl font-bold text-center font-sans text-black mr-8">ASK.IT</h1>
      <form @submit.prevent="submitForm" class="bg-white p-8 rounded-lg shadow-md w-96">
        <h1 class="text-3xl font-bold mb-8 text-center">Sign up</h1>
        <div class="mb-4">
          <label for="username" class="block text-gray-700 font-bold mb-2">Email</label>
          <input type="email" name="username" v-model="username" placeholder="Email"
                 class="border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400">
        </div>
        <div class="mb-4">
          <label for="firstname" class="block text-gray-700 font-bold mb-2">First name</label>
          <input type="text" name="firstname" v-model="firstname" placeholder="First name"
                 class="border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400">
        </div>
        <div class="mb-4">
          <label for="lastname" class="block text-gray-700 font-bold mb-2">Last name</label>
          <input type="text" name="lastname" v-model="lastname" placeholder="Last name"
                 class="border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400">
        </div>
        <div class="mb-4">
          <label for="password" class="block text-gray-700 font-bold mb-2">Password</label>
          <input type="password" name="password" v-model="password" placeholder="Password"
                 class="border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400">
        </div>
        <div class="mb-4">
          <button type="submit"
                  class="bg-blue-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline hover:bg-blue-600">
            Sign up
          </button>
        </div>
        <div>
          <a href="/log-in/">Already have an account log in!</a>
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
    }
  },
  methods: {
    submitForm(e) {
      axiosClient.post('/v1/users/', {
        username: this.username,
        email: this.username,

        password: this.password
      })
          .then(response => {
            console.log(this.lastname)
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
          })
    }
  }
}
</script>
<template>
  <div class="bg-gray-100 min-h-screen flex flex-col justify-center items-center">
    <div class="flex items-center flex-wrap mb-8">
      <h1 class="text-6xl font-bold text-center font-sans text-black mr-8">ASK.IT</h1>
      <form @submit.prevent="submitForm" class="bg-white p-8 rounded-lg shadow-md w-96">
        <h1 class="text-3xl font-bold mb-8 text-center">Reset password</h1>
        <div class="mb-4">
          <label for="password" class="block text-gray-700 font-bold mb-2">Password</label>
          <input type="password" name="password" v-model="password" placeholder="Password" :class="textInput">
        </div>
        <div class="mb-4">
          <label  class="block text-gray-700 font-bold mb-2">Confirm password</label>
          <input type="password" v-model="Cpassword" placeholder="Retype password" :class="textInput">
        </div>
        <div class="mb-2">
          <button type="submit"
                  class="bg-blue-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline hover:bg-blue-600">
            Reset password
          </button>
          <label v-if="invalid" class="text-red-600 pl-4" >{{ errorMessage }}</label>
        </div>
        <div>
          <a>Don't have an account? </a>
          <button v-on:click="redirectToSignUp" class="text-blue-400 hover:underline hover:text-blue-500">Sign up!</button>
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
  name: 'ResetPasswordView',
  data() {
    return {
      password: '',
      Cpassword: '',
      fields: true,
      invalid: false,
      textInput: 'border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-400',
      errorMessage: ''
    }
  },
  methods: {
    submitForm(e) {
      const formData = {
        uid: this.$route.params.uid,
        token: this.$route.params.token,
        new_password: this.password,
        re_new_password: this.Cpassword
      }

      axiosClient.post('/v1/users/reset_password_confirm/', formData)
          .then(response => {
            console.log(response)

            //const token = response.data.auth_token

            //this.$store.commit('setToken', token)

            //axiosClient.defaults.headers.common['Authorization'] = "Token " + token

            //localStorage.setItem("token", token)
           this.$router.push(this.$route.query.redirect || '/')
          })
          .catch(error => {
            console.log(error)
           // if (error.response.status === 400) {
            //  this.errorMessage = "Invalid username or password"
          //  } //else {
              // set this.errorMessage to the first element of the only attribute of error.response.data
          //    this.errorMessage = Object.values(error.response.data)[0][0]
           // }
           // this.invalid = true
            //this.textInput = "border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-2 focus:ring-red-100 border-red-500"
          })
    },
    redirectToSignUp() {
      this.$router.push({name: 'SignUp', query: {redirect: this.$route.query.redirect}})
    }
  }

}
</script>
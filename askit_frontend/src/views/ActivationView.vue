<template>
  <div class="h-screen w-screen flex justify-center content-center dark:bg-gradient-to-r dark:from-gray-700 dark:via-gray-900 dark:to-black bg-gradient-to-r from-green-200 via-green-300 to-blue-500">
      <div class="flex flex-col justify-center">
        <div class="p-10 dark:bg-gray-600/50 backdrop-blur-md bg-white/50  rounded drop-shadow-lg shadow-white">
          <h1 class=" text-center">Your account has been activated, please close this window</h1>
        </div>
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
  name: 'ActivationView',
  data() {
    return {
    }
  },
  mounted() {
    axiosClient.post('/v1/users/activation/', {
                      uid: this.$route.params.uid,
                      token: this.$route.params.token,
          })
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
    },
    
  }
</script>
<template>
  <div>Your account has been activated, please close this window</div>
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
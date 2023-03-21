<template>
    <div class="">
        <h1>Log in</h1>

        <form @submit.prevent="submitForm">
            <label for="username">Username</label>
            <input type="email" name="username" v-model="username" class="border-2">
            <label for="password">Password</label>
            <input type="password" name="password" v-model="password" class="border-2">
            <button type="submit" class="bg-blue-300">Log in</button>
        </form> 
    </div>
</template>

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
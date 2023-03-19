<template>
    <div class="">
        <h1>Log in</h1>

        <form @submit.prevent="submitForm">
            <input type="email" name="username" v-model="username">
            <input type="password" name="password" v-model="password">
            <button type="submit">Log in</button>
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
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
      
}
</script>
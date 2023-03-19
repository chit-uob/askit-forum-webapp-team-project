<template>
    <div >
        <h1>Sign up</h1>
        <form @submit.prevent="submitForm">
            <input type="email" name="username" v-model="username" placeholder="email">
            <input type="password" name="password" v-model="password" placeholder="password">
            <button type="submit">Sign up</button>
        </form>
    </div>
</template>

<script>
import axiosClient from './axiosClient';

export default {
    name: 'SignUpView',
    data(){
        return{
            username: '',
            password: '',
        }
    },
    methods: {
        submitForm(e) {
            console.log(this.username)
            console.log(this.password)
            axiosClient.post('/v1/users/', {
                username: this.username,
                password: this.password
            })
            .then(response =>{
                this.$router.push('/log-in')
                console.log(response)
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
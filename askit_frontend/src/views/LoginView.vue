<template>
    <div class="bg-gradient-to-r from-cyan-100 to-blue-500 dark:bg-gradient-to-r from-blue-700 to-gray-700 min-h-screen flex flex-col justify-center items-center">
      <div class="flex items-center flex-wrap mb-8">
            <h1 class="text-8xl font-bold text-center font-sans text-black mr-8">ASK.IT</h1>
            <form @submit.prevent="submitForm" class=" dark:bg-gray-900 bg-gray-100 p-8 rounded-lg shadow-md w-96">
                <h1 class="text-3xl dark:text-blue-400 font-bold mb-8 text-center">Log in</h1>
                <div class="mb-4">
                    <label for="username" class="block dark:text-blue-300 text-black font-bold mb-2">Email</label>
                    <input type="email" name="username" v-model="username" placeholder="Email" :class="textInput">
                </div>
                <div class="mb-4">
                    <label for="password" class="block dark:text-blue-300  text-black font-bold mb-2">Password</label>
                    <input type="password" name="password" v-model="password" placeholder="Password" :class="textInput">
                </div>
                <div class="mb-2">
                    <button type="submit"
                            class="transition focus:ring-4 dark:text-white  focus:ring-pink-400 bg-blue-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline hover:bg-blue-600">
                        Log in
                    </button>
                    <label v-if="invalid" class="text-red-600 pl-4">{{ errorMessage }}</label>
                </div>
                <div>
                    <a>Don't have an account? </a>
                    <button v-on:click="redirectToSignUp"
                            class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 text-blue-400 hover:underline hover:text-blue-500">
                         Sign up!
                    </button>
                    <button v-on:click="redirectToResetPassword"
                            class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 text-blue-400 hover:underline hover:text-blue-500">
                        Forgot password?
                    </button>
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
    data() {
        return {
            username: '',
            password: '',
            fields: true,
            invalid: false,
            textInput: 'border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400',
            errorMessage: ''
        }
    },
    methods: {
        submitForm(e) {
            const formData = {
                username: this.username,
                password: this.password
            }

            axiosClient.post('/v1/token/login/', formData)
                .then(response => {

                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axiosClient.defaults.headers.common['Authorization'] = "Token " + token

                    localStorage.setItem("token", token)
                    localStorage.removeItem("largeFont")
                    localStorage.removeItem("theme")
                    localStorage.removeItem("readableFont")
                    localStorage.removeItem("letterSpacing")
                    localStorage.removeItem("grayscale")
                    localStorage.removeItem("invert")
                    localStorage.removeItem("colourHue")

                    this.$root.loadModules()
                    this.$router.push(this.$route.query.redirect || '/')
                })
                .catch(error => {
                    console.log(error)
                    if (error.response.status === 400) {
                        this.errorMessage = "Invalid username or password"
                    } else {
                        // set this.errorMessage to the first element of the only attribute of error.response.data
                        this.errorMessage = Object.values(error.response.data)[0][0]
                    }
                    this.invalid = true
                    this.textInput = "border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-red-300 border-red-500"
                })
        },
        redirectToSignUp() {
            this.$router.push({name: 'SignUp', query: {redirect: this.$route.query.redirect}})
        },
        redirectToResetPassword() {
            this.$router.push({name: 'ForgotPassword', query: {redirect: this.$route.query.redirect}})
        }
    }

}
</script>
<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <nav v-if="enable" class="bg-teal-100 px-2 py-1 sm:px-4 border-b-[3px] border-black h-[62px]" id="nav-vue">
    <div class="container mx-auto flex flex-wrap items-center justify-between">
      <router-link to="/" class="pl-4">
        <span class="text-2xl font-bold">ASK.IT</span>
      </router-link>
      <form class="w-1/2" @submit.prevent="search">
        <label for="default-search"
               class="sr-only mb-2 text-sm font-medium text-gray-900">Search</label>
        <div class="relative">
          <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
            <i class="fa fa-search" aria-hidden="true"></i>
          </div>
          <input type="search" id="default-search"
                 class="block w-full h-[45px] rounded-lg border-2 border-black bg-white p-4 pl-10 text-sm text-gray-900 focus:border-teal-500 focus:ring-teal-500"
                 placeholder="Search questions" v-model="searchTerm" required>
          <button type="submit"
                  class="absolute rounded-lg bg-blue-700 px-4 py-1 text-sm font-medium text-white h-[33px] right-2.5 bottom-1.5 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300">
            Search
          </button>
        </div>
      </form>
      <button type="button"
              class="ml-3 inline-flex items-center rounded-lg bg-teal-100 p-2 text-sm text-gray-500 outline-1 outline-teal-300 hover:bg-teal-300 focus:outline-none focus:ring-2 focus:ring-teal-200 md:hidden"
              aria-controls="navbar-default" aria-expanded="false"
              v-on:click="showNav">
        <span class="sr-only">Open main menu</span>
        <i class="fa fa-bars" aria-hidden="true"></i>
      </button>
      <div class="z-20 mt-2 w-full flex-grow p-4 text-black" :class="this.showMobileNav ? 'block' : 'hidden'"
           id="mobile-nav">
        <ul>
          <li><i class="pr-1 fa fa-bell-o" aria-hidden="true"></i>Notifications</li>
          <li><i class="pr-1 fa fa-user" aria-hidden="true"></i>Profile</li>
          <li><i class="pr-1 fa fa-question-circle" aria-hidden="true"></i>Help</li>
          <li><i class="pr-1 fa fa-cog" aria-hidden="true"></i>Settings</li>
        </ul>
      </div>
      <div class="hidden w-full md:block md:w-auto" id="navbar-default">
        <ul class="mt-4 flex flex-col p-4 md:space-x-8 md:mt-0 md:flex-row md:border-0 md:text-sm md:font-medium">
          <li>
            <a href="#"
               class="block rounded py-2 pr-4 pl-3 text-gray-700 hover:bg-gray-100 md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-700"
               aria-current="page"><i class="fa fa-bell-o scale-150" aria-hidden="true"></i></a>
          </li>
          <li>
            <a href="#"
               class="block rounded py-2 pr-4 pl-3 text-gray-700 hover:bg-gray-100 md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-700"><i
                class="fa fa-user scale-150" aria-hidden="true"></i></a>
          </li>
          <li>
            <a href="#"
               class="block rounded py-2 pr-4 pl-3 text-gray-700 hover:bg-gray-100 md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-700"><i
                class="fa fa-question-circle scale-150" aria-hidden="true"></i></a>
          </li>
          <li>
            <a href="#"
               class="block rounded py-2 pr-4 pl-3 text-gray-700 hover:bg-gray-100 md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-700"><i
                class="fa fa-cog scale-150" aria-hidden="true"></i></a>
          </li>
        </ul>
      </div>
      <button type="button" v-on:click="logout"
              class="">
        Logout
      </button>
    </div>
  </nav>
  <div class="flex">
    <div class="hidden flex-col justify-items-center bg-cyan-50 w-[175px] md:block border-r-[3px] border-black"
         v-if="enable">
      <h1 class="ml-5 p-3 text-lg font-bold">Modules</h1>
      <div v-for="module in modules" class="mt-2 mr-5 ml-5 rounded-2xl bg-gray-400 w-[100px] h-[100px]">
        <a :href="'/module/' + module.title" class="text-sky-600 hover:underline"><p class="p-8">{{ module.title }}</p>
        </a>
      </div>
    </div>
    <div class="w-full">
      <router-view/>
    </div>
  </div>

  <footer class="rounded-lg bg-sky-100 p-4 shadow md:flex md:items-center md:justify-between md:p-6">
    <span class="text-sm text-gray-500 sm:text-center">© 2023 <a href="#" class="hover:underline">TeamAI55</a>. All Rights Reserved.
    </span>
    <span class="text-sm text-gray-500 sm:text-center">Alpha Project Disclaimer This server is provided by the School of Computer Science at the University of Birmingham to allow users to provide feedback on software developed by students as part of an assignment. While we take reasonable precautions, we cannot guarantee the security of the data entered into the system. Do NOT enter any real personal data (e.g., financial information or otherwise) into the system. The assignment runs until May 31st 2023, at which time the server and all associated data will be destroyed.
    </span>
    <ul class="mt-3 flex flex-wrap items-center text-sm text-gray-500 sm:mt-0">
      <!--        <li>-->
      <!--            <a href="#" class="mr-4 hover:underline md:mr-6">About</a>-->
      <!--        </li>-->
      <li>
        <a target="_blank" href="/privacy" class="mr-4 hover:underline md:mr-6">Privacy Policy</a>
      </li>
      <!--        <li>-->
      <!--            <a href="#" class="mr-4 hover:underline md:mr-6">Licensing</a>-->
      <!--        </li>-->
      <!--        <li>-->
      <!--            <a href="#" class="hover:underline">Contact</a>-->
      <!--        </li>-->
    </ul>
  </footer>

</template>

<script>
import axiosClient from "@/views/axiosClient";

export default {
  name: 'App',
  watch: {
    $route: {
      handler: function () {
        if (this.$route.path.startsWith('/log-in') ||
            this.$route.path.startsWith('/sign-up') ||
            this.$route.path.startsWith('/privacy') ||
            this.$route.path.startsWith('/password/reset')
        ) {
          if (this.$store.state.isAuthenticated) {
            this.$router.push("/")
          }
          this.enable = false
        } else {
          console.log("here")
          this.enable = true
          if (!this.$store.state.isAuthenticated) {
            this.$router.push({name: 'LogIn', query: {redirect: this.$route.path}})
          }
        }
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    console.log(token)

    if (token) {
      axiosClient.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axiosClient.defaults.headers.common['Authorization'] = ''
    }

  },
  data() {
    return {
      showMobileNav: false,
      searchTerm: '',
      enable: true,
      modules: []
    }
  },
  methods: {
    showNav() {
      this.showMobileNav = !this.showMobileNav;
    },
    search() {
      console.log(this.$route.path);
      if (this.$route.path.startsWith('/module/')) {
        this.$router.push({
          path: '/search',
          query: {searchTerm: this.searchTerm, module: this.$route.path.split('/')[2]}
        });
      } else if (this.$route.path.startsWith('/search')) {
        this.$router.push({path: '/search', query: {searchTerm: this.searchTerm, module: this.$route.query.module}});
      } else {
        this.$router.push({path: '/search', query: {searchTerm: this.searchTerm, module: null}});
      }
    },
    logout() {
      axiosClient.post('/v1/token/logout/')
          .then(response => {

            this.$store.commit('removeToken')

            axiosClient.defaults.headers.common['Authorization'] = ""
            localStorage.setItem("token", "")
            this.$router.push('/log-in/')
          })
          .catch(error => {
            console.log(error)
          })
    },
    loadModules() {
      axiosClient.get('/module/list/')
          .then(response => {
            this.modules = response.data
          })
          .catch(error => {
            console.log(error)
          })
    }
  },
  created() {
    if (this.$store.state.isAuthenticated) {
      this.loadModules()
    }
  },
}


</script>

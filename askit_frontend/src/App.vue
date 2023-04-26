<template class="hue-rotate-[30deg] hue-rotate-[60deg] hue-rotate-[90deg] hue-rotate-[120deg] hue-rotate-[150deg] hue-rotate-[180deg] hue-rotate-[210deg] hue-rotate-[240deg] hue-rotate-[270deg] hue-rotate-[300deg] hue-rotate-[330deg] hue-rotate-[360deg]
hue-rotate-[-30deg] hue-rotate-[-60deg] hue-rotate-[-90deg] hue-rotate-[-120deg] hue-rotate-[-150deg] hue-rotate-[-180deg] hue-rotate-[-210deg] hue-rotate-[-240deg] hue-rotate-[-270deg] hue-rotate-[-300deg] hue-rotate-[-330deg] hue-rotate-[-360deg] tracking-tight tracking-wide">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <nav v-if="enable"
         class="bg-teal-100 dark:bg-slate-900 px-2 sm:px-4 border-b-[3px] border-black dark:border-white text-black dark:text-white"
         id="nav-vue">
        <div class="container mx-auto flex flex-wrap items-center justify-between h-full">
            <router-link to="/" class="pl-4 transition focus:ring-4 focus:outline-none focus:ring-blue-400">
                <span class="text-2xl font-bold">ASK.IT</span>
            </router-link>
            <form class="w-1/2" @submit.prevent="search">
                <label for="default-search"
                       class="sr-only mb-2 text-sm font-medium text-gray-900 dark:text-gray-100">Search</label>
                <div class="relative">
                    <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                        <i class="fa fa-search" aria-hidden="true"></i>
                    </div>
                    <input type="search" id="default-search" ref="search"
                           class="transition focus:ring-4 focus:outline-none block w-full h-[45px] rounded-lg border-2 border-black dark:border-white bg-white dark:bg-black p-4 pl-10 text-sm text-gray-900 dark:text-gray-100 focus:border-blue-500 dark:focus:border-blue-300 focus:ring-blue-500 dark:focus:ring-blue-300"
                           placeholder="Search questions" v-model="searchTerm" required>
                    <button type="submit"
                            class="transition absolute rounded-lg bg-blue-700 px-4 text-sm font-medium text-white h-[33px] right-2.5 bottom-1.5 hover:bg-blue-800 dark:hover:bg-blue-200 focus:outline-none focus:ring-4 focus:ring-pink-400">
                        Search
                    </button>
                </div>
            </form>
            <div class="w-auto" id="navbar-default">
                <ul class="flex flex-col p-4 md:space-x-8 md:mt-0 md:flex-row md:border-0 md:text-sm md:font-medium">
                    <li>
                        <a href="/settings/"
                           class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 block rounded py-2 pr-4 pl-3 text-gray-700 dark:text-gray-200 hover:bg-gray-100 md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-700"><i
                                class="fa fa-cog scale-150 pr-2" aria-hidden="true"></i>Settings</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="absolute md:hidden text-black dark:text-white">
        <button class="bg-cyan-600 hover:bg-cyan-700 text-white font-bold py-2 px-4 rounded" @click="toggleModule"
                v-if="enable">
            Select module
        </button>
    </div>
    <div class="flex text-black dark:text-white">
        <div tabindex="0" ref="modules"
             class="focus:ring-4 focus:outline-none focus:ring-inset focus:ring-blue-400 flex-col justify-items-center bg-cyan-50 dark:bg-slate-900 w-[175px] md:block border-r-[3px] border-black dark:border-white"
             v-if="enable" :class="{ hidden: !showModule }">
            <h1 class="ml-5 p-3 text-lg font-bold">Modules</h1>
            <a v-for="module in modules"
               class="shadow-[4px_4px_0px_0px_#000000] dark:shadow-[4px_4px_0px_0px_#ffffff] transition hover:translate-x-1 hover:bg-[#fff6fe] dark:hover:bg-[#240020] focus:ring-4 focus:outline-none focus:ring-blue-400 mx-5 my-4 rounded-2xl border-2  border-black dark:border-white bg-white dark:bg-black flex h-[100px] w-[100px] justify-center"
               :href="'/module/' + module.title">
                <div class="justify-center flex w-full m-2 rounded-[0.6rem] border-2 border-black dark:border-white border-dashed">
                    <p class="inline-block place-self-center text-xl tracking-[1px]">{{ module.title }}</p>
                </div>
            </a>
        </div>
        <div class="w-full">
            <router-view/>
        </div>
    </div>

    <footer class="border-t-[3px] dark:border-white border-black  bg-sky-100 dark:bg-slate-900 p-4 shadow md:flex md:items-center md:justify-between md:p-6 text-black dark:text-white text-sm">
    <span class=" sm:text-center">© 2023 <a href="#" class="hover:underline">TeamAI55</a>. All Rights Reserved.
    </span>
        <span class="sm:text-center">Alpha Project Disclaimer This server is provided by the School of Computer Science at the University of Birmingham to allow users to provide feedback on software developed by students as part of an assignment. While we take reasonable precautions, we cannot guarantee the security of the data entered into the system. Do NOT enter any real personal data (e.g., financial information or otherwise) into the system. The assignment runs until May 31st 2023, at which time the server and all associated data will be destroyed.
    </span>
        <ul class="mt-3 flex flex-wrap items-center sm:mt-0">
            <li>
                <a target="_blank" href="/privacy" class="mr-4 hover:underline md:mr-6">Privacy Policy</a>
            </li>
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
                    this.$route.path.startsWith('/password/reset') ||
                    this.$route.path.startsWith('/activate')
                ) {
                    if (this.$store.state.isAuthenticated && !this.$route.path.startsWith('/privacy')) {
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
            modules: [],
            showModule: false
        }
    },
    methods: {
        handleKeyboardShortcuts(event) {
            if (event.altKey && (event.key === 'K' || event.key === 'k')) {
                this.$refs.search.focus()
            }
            if (event.altKey && (event.key === 'M' || event.key === 'm')) {
                this.$refs.modules.focus()
            }
            if (event.altKey && (event.key === 'H' || event.key === 'h')) {
                this.$router.push({path: '/'})
            }
            if (event.altKey && (event.key === 'Q' || event.key === 'q') && this.$route.params.mod) {
                this.$router.push({path: '/ask/' + this.$route.params.mod})
            }
        },
        toggleModule() {
            this.showModule = !this.showModule;
        },
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
                this.$router.push({
                    path: '/search',
                    query: {searchTerm: this.searchTerm, module: this.$route.query.module}
                });
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
                    if (error.response.status === 401) {
                        this.clientSideLogout()
                    }
                })
        },
        clientSideLogout() {
            this.$store.commit('removeToken')

            axiosClient.defaults.headers.common['Authorization'] = ""
            localStorage.setItem("token", "")
            this.$router.push('/log-in/')
        }
    }
    ,
    created() {
        window.addEventListener('keydown', this.handleKeyboardShortcuts)

        if (this.$store.state.isAuthenticated) {
            this.loadModules()
        }

        if (localStorage.getItem("theme") === "dark") {
            document.body.classList.remove('light')
            document.body.classList.add('dark')
        } else if (localStorage.getItem("theme") === "light") {
            document.body.classList.remove('dark')
            document.body.classList.add('light')
        } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.body.classList.remove('light')
            document.body.classList.add('dark')
        } else {
            document.body.classList.remove('dark')
            document.body.classList.add('light')
        }
    }
    ,
    mounted() {
        if (localStorage.getItem("largeFont") === "true") {
            // remove all different text size class
            document.querySelectorAll('.text-xs').forEach(e => e.classList.remove('text-xs'));
            document.querySelectorAll('.text-sm').forEach(e => e.classList.remove('text-sm'));
            document.querySelectorAll('.text-base').forEach(e => e.classList.remove('text-base'));
            document.querySelectorAll('.text-lg').forEach(e => e.classList.remove('text-lg'));
            document.querySelectorAll('.text-xl').forEach(e => e.classList.remove('text-xl'));
            document.body.classList.add('text-xl')
        }
        if (localStorage.getItem("readableFont") === "true") {
            document.body.classList.add('font-[sans-serif]')
        }
        if (localStorage.getItem("grayscale") === "true") {
            document.body.classList.add('grayscale')
        }
        if (localStorage.getItem("invert") === "true") {
            document.body.classList.add('invert')
        }
        document.body.classList.add('hue-rotate-[' + localStorage.getItem("colourHue") + 'deg]')
        document.querySelectorAll('.tracking-tight').forEach(e => e.classList.remove('tracking-tight'));
        document.body.classList.add('tracking-' + localStorage.getItem("letterSpacing"))
    },
    beforeDestroy() {
        console.log("before destroy")
        window.removeEventListener('keydown', this.handleKeyboardShortcuts)
    },
}


</script>

<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <nav class="bg-teal-200 px-2 py-2.5 sm:px-4" id="nav-vue">
    <div class="container mx-auto flex flex-wrap items-center justify-between">
      <router-link to="/" class="pl-4">
        <span class="text-xl font-bold">ASK.IT</span>
      </router-link>
      <form class="w-1/2">
        <label for="default-search"
               class="sr-only mb-2 text-sm font-medium text-gray-900">Search</label>
        <div class="relative">
          <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
            <i class="fa fa-search" aria-hidden="true"></i>
          </div>
          <input type="search" id="default-search"
                 class="block w-full rounded-lg border border-teal-400 bg-teal-50 p-4 pl-10 text-sm text-gray-900 focus:border-teal-500 focus:ring-teal-500"
                 placeholder="Search questions" required>
          <button type="submit"
                  class="absolute rounded-lg bg-blue-700 px-4 py-2 text-sm font-medium text-white right-2.5 bottom-2.5 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300">
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
      <div class="z-20 mt-2 w-full flex-grow p-4 text-black" :class="this.showMobileNav ? 'block' : 'hidden'" id="mobile-nav">
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
               aria-current="page"><i class="fa fa-bell-o" aria-hidden="true"></i></a>
          </li>
          <li>
            <a href="#"
               class="block rounded py-2 pr-4 pl-3 text-gray-700 hover:bg-gray-100 md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-700"><i
                class="fa fa-user" aria-hidden="true"></i></a>
          </li>
          <li>
            <a href="#"
               class="block rounded py-2 pr-4 pl-3 text-gray-700 hover:bg-gray-100 md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-700"><i
                class="fa fa-question-circle" aria-hidden="true"></i></a>
          </li>
          <li>
            <a href="#"
               class="block rounded py-2 pr-4 pl-3 text-gray-700 hover:bg-gray-100 md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-700"><i
                class="fa fa-cog" aria-hidden="true"></i></a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <router-view/>

  <footer class="rounded-lg bg-sky-100 p-4 shadow md:flex md:items-center md:justify-between md:p-6">
    <span class="text-sm text-gray-500 sm:text-center">© 2023 <a href="#" class="hover:underline">TeamAI55</a>. All Rights Reserved.
    </span>
    <ul class="mt-3 flex flex-wrap items-center text-sm text-gray-500 sm:mt-0">
      <!--        <li>-->
      <!--            <a href="#" class="mr-4 hover:underline md:mr-6">About</a>-->
      <!--        </li>-->
      <li>
        <a href="/privacy" class="mr-4 hover:underline md:mr-6">Privacy Policy</a>
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
  export default {
    name: 'App',
    data() {
      return {
        showMobileNav: false
      }
    },
    methods: {
      showNav() {
        this.showMobileNav = !this.showMobileNav;
      }
    }
  }
</script>

<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <nav class="bg-teal-200 px-2 sm:px-4 py-2.5 rounded" id="nav_vue">
    <div class="container flex flex-wrap items-center justify-between mx-auto">
        <router-link to="/" class="pl-4 flex items-center">
            <span class="self-center text-xl font-bold whitespace-nowrap">ASK.IT</span>
        </router-link>
        <form class="w-1/2">
            <label for="default-search"
                   class="mb-2 text-sm font-medium text-gray-900 sr-only">Search</label>
            <div class="relative">
                <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                    <i class="fa fa-search" aria-hidden="true"></i>
                </div>
                <input type="search" id="default-search"
                       class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500"
                       placeholder="Search questions" required>
                <button type="submit"
                        class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2">
                    Search
                </button>
            </div>
        </form>
        <button type="button"
                class="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200"
                aria-controls="navbar-default" aria-expanded="false"
                v-on:click="showNav">
            <span class="sr-only">Open main menu</span>
            <i class="fa fa-bars" aria-hidden="true"></i>
        </button>
        <div class="w-full flex-grow mt-2 text-black p-4 z-20 hidden" id="mobile-nav">
            <ul>
                <li><i class="fa fa-bell-o pr-1" aria-hidden="true"></i>Notifications</li>
                <li><i class="fa fa-user pr-1" aria-hidden="true"></i>Profile</li>
                <li><i class="fa fa-question-circle pr-1" aria-hidden="true"></i>Help</li>
                <li><i class="fa fa-cog pr-1" aria-hidden="true"></i>Settings</li>
            </ul>
        </div>
        <div class="hidden w-full md:block md:w-auto" id="navbar-default">
            <ul class="flex flex-col p-4 mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0">
                <li>
                    <a href="#"
                       class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0"
                       aria-current="page"><i class="fa fa-bell-o" aria-hidden="true"></i></a>
                </li>
                <li>
                    <a href="#"
                       class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0"><i
                            class="fa fa-user" aria-hidden="true"></i></a>
                </li>
                <li>
                    <a href="#"
                       class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0"><i
                            class="fa fa-question-circle" aria-hidden="true"></i></a>
                </li>
                <li>
                    <a href="#"
                       class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0"><i
                            class="fa fa-cog" aria-hidden="true"></i></a>
                </li>
            </ul>
        </div>
    </div>
</nav>
  <router-view/>

<footer class="p-4 bg-sky-100 rounded-lg shadow md:flex md:items-center md:justify-between md:p-6">
    <span class="text-sm text-gray-500 sm:text-center">© 2023 <a href="#" class="hover:underline">TeamAI55</a>. All Rights Reserved.
    </span>
    <ul class="flex flex-wrap items-center mt-3 text-sm text-gray-500 sm:mt-0">
<!--        <li>-->
<!--            <a href="#" class="mr-4 hover:underline md:mr-6 ">About</a>-->
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

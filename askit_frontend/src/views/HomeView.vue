<template>
  <div class="bg-pink-50">
  <div class="min-h-screen">
    <div class="flex justify-between py-10">
      <div class="px-16">
        <h1 class="text-5xl font-bold">Welcome back</h1>
        <h1 class="text-5xl italic font-bold">user</h1>
      </div>

      <div class="grid grid-cols-2">
        <div class="grid grid-rows-3 text-right self-start">
          <h2 class="self-start text-3xl font-bold">Student name</h2>
          <h2 class="self-center text-xl">University of Somewhere</h2>
          <h2 class="self-end">email@student.xzy.ac.uk</h2>
        </div>
        <div
            class="self-start mt-2 mr-5 ml-5 rounded-2xl bg-white w-[100px] h-[100px] transition ease-in-out delay-75 hover:scale-[1.02] duration-150 hover:bg-[#F2FFFA] border-[0.12em] border-black"
            style="box-shadow: .13em .13em;"></div>
      </div>

    </div>
    <br>

    <div class="grid grid-cols-2 gap-5 px-10">
      <div class="bg-white border-2 border-gray-400 rounded-md p-5">
        <div class="flex items-center justify-center">
  <div class="flex items-center">
        <span class="text-xl text-center font-bold mb-5 ml-2">Notifications</span>
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bell-fill" viewBox="0 0 16 16">
      <path d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2zm.995-14.901a1 1 0 1 0-1.99 0A5.002 5.002 0 0 0 3 6c0 1.098-.5 6-2 7h14c-1.5-1-2-5.902-2-7 0-2.42-1.72-4.44-4.005-4.901z"/>
    </svg>

  </div>
</div>

        <hr class="border-gray-400 mb-5">
        <div>Notification 1</div>
        <div>Notification 2</div>
        <div>Notification 3</div>
      </div>
      <div class="bg-white border-2 border-gray-400 rounded-md p-5">
        <div class="text-xl text-center font-bold mb-5">Calendar</div>
        <hr class="border-gray-400 mb-5">
      </div>
    </div>
  </div>
  </div>
</template>


<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faBell } from '@fortawesome/free-solid-svg-icons'

library.add(faBell)

// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
    FontAwesomeIcon
  },

}
</script>

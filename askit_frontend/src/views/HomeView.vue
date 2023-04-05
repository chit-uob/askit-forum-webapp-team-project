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
          <span class="text-xl text-center font-bold mb-5">Notifications</span>
          <font-awesome-icon icon="bell" class="text-xl text-center font-bold mb-5 ml-2"/>
        </div>
        <hr class="border-gray-400 mb-5">
<!--        hard coded the below part-->
        <div>Notification 1</div>
        <div>Notification 2</div>
        <div>Notification 3</div>
      </div>
      <div class="box-content bg-white border-2 border-gray-400 rounded-md p-5">
        <div class="text-xl text-center font-bold mb-5">Calendar</div>
        <hr class="border-gray-400 mb-5">
      </div>
    </div>
    <br>
    <br>
    <div class="bg-white border-2 border-gray-400 rounded-md p-5 px-10">

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

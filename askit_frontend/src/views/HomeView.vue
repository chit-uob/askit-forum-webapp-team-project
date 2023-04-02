<template>
  <div class="flex min-h-screen justify-between py-10">
    <div class="px-10 ">
      <h1 class="text-5xl font-bold">Welcome back</h1>
      <h1 class="text-5xl font-bold">user</h1>
    </div>

      <div class="grid grid-cols-2">
        <div class="grid grid-rows-3 text-right self-start">
          <h2 class="self-start text-3xl font-bold">Student name</h2>
          <h2 class="self-center text-xl">University of Somewhere</h2>
          <h2 class="self-end">email@student.xzy.ac.uk</h2>
        </div>
        <div class="self-start mt-2 mr-5 ml-5 rounded-2xl bg-white w-[100px] h-[100px] transition ease-in-out delay-75 hover:scale-[1.02] duration-150 hover:bg-[#F2FFFA] border-[0.12em] border-black" style="box-shadow: .13em .13em;"></div>
      </div>



  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },

}
</script>

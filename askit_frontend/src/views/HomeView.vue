<template>
  <div class="flex min-h-screen justify-end py-10">
    <div class="px-10 pr-64">
      <h1 class="text-5xl font-bold">Welcome back</h1>
      <h1 class="text-5xl font-bold">user</h1>
    </div>

      <div class="flex-row ">
        <div class="grid grid-rows-3 text-right">
          <h2 class="self-start text-3xl font-bold">Student name</h2>
          <h2 class="self-center text-xl">University of Somewhere</h2>
          <h2 class="self-end">email@student.xzy.ac.uk</h2>
        </div>
      </div>

      <div class=" mt-2 mr-5 ml-5 rounded-2xl bg-white w-[100px] h-[100px] transition ease-in-out delay-75 hover:scale-[1.02] duration-150 hover:bg-[#F2FFFA] border-[0.12em] border-black" style="box-shadow: .13em .13em;"></div>

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

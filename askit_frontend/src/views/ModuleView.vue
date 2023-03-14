<template>
  <div class="w-screen h-screen flex">
    <div class="w-[175px] h-full bg-cyan-100 flex-col justify-items-center">
      <h1 class="ml-5 font-bold text-lg p-3 ">Modules</h1>
      <div class="ml-5 mr-5 mt-2 w-[100px] h-[100px] rounded-2xl bg-gray-400">
        <a href="/module/OSSP" class=" text-sky-600 hover:underline"><p class="p-8">OSSP</p></a>
      </div>
      <div class="ml-5 mr-5 mt-2 w-[100px] h-[100px] rounded-2xl bg-gray-400">
        <a href="/module/TP" class=" text-sky-600 hover:underline"><p class="p-8">TP</p></a>
      </div>
    </div>
    <div class="w-full h-screen">
      <div class="p-10 inline-flex justify-between w-full">
        <h1 class="text-5xl font-bold">{{ $route.params.mod }}</h1>
        <a href="/ask">
        <button type="submit" 
                class="text-white  bg-blue-600 hover:bg-blue-500 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2">
          Ask Question
        </button>
        </a>
      </div>
      <h2 class="pl-10 text-2xl font-bold">All Questions</h2>
      <div v-for="question in questions" :key="question.id">
        <a class="pt-2 pl-10 pr-10 flex w-full" :href="`/question/${question.id}`">
          <div class="card inline-flex w-full h-20 bg-cyan-200 rounded-2xl shadow">
            <div class=" w-[100px] p-3 flex flex-col justify-evenly border-r-2 border-black">
              <p class="text-xs text-right">{{ question.score }} votes</p>
              <p class="text-xs text-right">{{ question.num_answers }} answers</p>
              <p class="text-xs text-right">{{ question.views }} views</p>
            </div>
            <div class=" w-8/12 p-3 flex flex-col justify-evenly">
              <h3>{{ question.title }}</h3>
              <p>Asked by [User]{{ question.author }}</p>
              <p>{{ question.tags.substring(10,question.tags.length-1) }}</p>
            </div>
            <div class=" w-[80px] p-3 flex flex-col justify-evenly">
              <h3>{{ question.pub_date }}</h3>
            </div>
          </div>
        </a>
      </div>
    </div>
    <div class="w-[400px] h-full bg-gray-200 p-3">


      
    </div>
  </div>
</template>

<script>
import axiosClient from "@/views/axiosClient";

export default {
  name: "ModuleView",
  data() {
    return {
      questions: []
    };
  },
  mounted() {
    axiosClient({
      method: "get",
      url: `/module/${this.$route.params.mod}/`,
    })
        .then((response) => {
          this.questions = response.data;
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error);
        });
  },
  methods: {}
};
</script>
<template>
  <div class="w-screen h-screen flex">
    <div class="w-[150px] h-full bg-cyan-100">
      Side Bar
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
          <div class="card inline-flex w-full h-20 bg-cyan-200 rounded-2xl shadow outline-black">
            <div class=" w-[100px] p-3 flex flex-col justify-evenly">
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
      <h1 class=" font-bold text-lg">Modules</h1>
        <a href="/module/OSSP" class=" text-sky-600 hover:underline"><p>OSSP</p></a>
        <a href="/module/TP" class="text-sky-600 hover:underline"><p>TP</p></a>
      
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
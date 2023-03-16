<template>
  <div class="flex">
    <div class="flex-col justify-items-center bg-cyan-100 w-[175px]">
      <h1 class="ml-5 p-3 text-lg font-bold">Modules</h1>
      <div class="mt-2 mr-5 ml-5 rounded-2xl bg-gray-400 w-[100px] h-[100px]">
        <a href="/module/OSSP" class="text-sky-600 hover:underline"><p class="p-8">OSSP</p></a>
      </div>
      <div class="mt-2 mr-5 ml-5 rounded-2xl bg-gray-400 w-[100px] h-[100px]">
        <a href="/module/TP" class="text-sky-600 hover:underline"><p class="p-8">TP</p></a>
      </div>
    </div>
    <div class="w-2/3">
      <div class="inline-flex w-full justify-between p-10">
        <h1 class="text-5xl font-bold">{{ $route.params.mod }}</h1>
        <a :href="`/ask/${$route.params.mod}`">
          <button type="submit"
                  class="rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-500 focus:outline-none focus:ring-4 focus:ring-blue-300">
            Ask Question
          </button>
        </a>
      </div>
      <h2 class="pl-10 text-2xl font-bold">All Questions</h2>
      <div v-for="question in questions" :key="question.id">
        <a class="flex w-full pt-2 pr-10 pl-10" :href="`/question/${question.id}`">
          <div class="inline-flex h-20 w-full rounded-2xl bg-cyan-200 shadow card">
            <div class="flex flex-col justify-evenly border-r-2 border-black p-3 w-[100px]">
              <p class="text-right text-xs">{{ question.score }} votes</p>
              <p class="text-right text-xs">{{ question.num_answers }} answers</p>
              <p class="text-right text-xs">{{ question.views }} views</p>
            </div>
            <div class="flex w-8/12 flex-col justify-evenly p-3">
              <h3 class="truncate">{{ question.title }}</h3>
              <p>Asked by {{ question.author }}</p>
              <div class="flex">
                <div v-for="tag in question.tags" class="mr-2">
                  <button
                      class="rounded bg-blue-50 px-2 text-center text-sm font-light text-blue-400 mt-0.5 h-[25px] hover:bg-blue-100">
                    {{ tag }}
                  </button>
                </div>
              </div>
            </div>
            <div class="flex flex-col justify-evenly p-3 w-[80px]">
              <h3>{{ formatPubDate(question.pub_date) }}</h3>
            </div>
          </div>
        </a>
      </div>
    </div>
    <div class="hidden flex-col bg-gray-200 p-3 w-[400px] md:block">


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

<script setup>
import { formatPubDate } from "./dateUtils";
</script>
<template>
  <div class="flex min-h-screen">
<!--    <div class="flex-col justify-items-center bg-cyan-100 w-[175px]">-->
<!--      <h1 class="ml-5 p-3 text-lg font-bold">Modules</h1>-->
<!--      <div class="mt-2 mr-5 ml-5 rounded-2xl bg-gray-400 w-[100px] h-[100px]">-->
<!--        <a href="/module/OSSP" class="text-sky-600 hover:underline"><p class="p-8">OSSP</p></a>-->
<!--      </div>-->
<!--      <div class="mt-2 mr-5 ml-5 rounded-2xl bg-gray-400 w-[100px] h-[100px]">-->
<!--        <a href="/module/TP" class="text-sky-600 hover:underline"><p class="p-8">TP</p></a>-->
<!--      </div>-->
<!--    </div>-->
    <div class="w-[70%] pb-[50px]">
      <div class="inline-flex w-full justify-between p-10">
        <h1 class="text-5xl font-bold">{{ $route.params.mod }}</h1>
        <div>
          <a :href="`/advanced-search/`">
            <button type="submit"
                    class="rounded-lg bg-blue-600 px-4 py-2 m-1 text-sm font-medium text-white hover:bg-blue-500 focus:outline-none focus:ring-4 focus:ring-blue-300">
              Advanced Search
            </button>
          </a>
          <a :href="`/ask/${$route.params.mod}`">
            <button type="submit"
                    class="rounded-lg bg-blue-600 px-4 py-2 m-1 text-sm font-medium text-white hover:bg-blue-500 focus:outline-none focus:ring-4 focus:ring-blue-300">
              Ask Question
            </button>
          </a>
        </div>
      </div>
      <div>
      <h2 class="pl-10 text-2xl  mb-6">Popular questions</h2>

      <a v-for="question in popQuestions" :key="question.id" :href="`/question/${question.id}`" 
      class="grid grid-cols-[100px_1fr_95px] mx-10 mb-[10px] box-content min-h-[98px] rounded-2xl bg-gradient-to-l from-[#f1fffd] to-[#ffffff] border-[0.24em] border-black " style="box-shadow: .27em .27em;">
        <div class="grid grid-rows-3 text-right  text-xs font-medium pr-2 border-r-[0.2em] border-gray-200 my-3  object-fill box-content">
          <div class=" self-start ">{{ question.score }} votes</div>
          <div class=" self-center ">{{ question.num_answers }} answers</div>
          <span class=" self-end  ">{{ question.views }} views</span>
        </div>

        <div class="grid grid-rows-3 pl-2 text-xs font-medium py-3  box-content object-fill">
          <div class=" truncate self-start text-base leading-[1.15] text-blue-500 hover:underline hover:text-blue-400">{{ question.title }}</div>
          <div class=" self-center ">Asked by <span  v-if="question.author" class="text-blue-500 hover:underline hover:text-blue-400">{{ question.author  }}</span><span  v-if="!(question.author)" class="">Anonymous</span></div>
          <div v-if="question.tags[0] != ''"  class="flex">
            <div v-for="tag in question.tags" class=" self-end mr-[2px] text-blue-500 hover:underline hover:text-blue-400">[{{ tag }}]</div>
          </div>
          <div v-if="question.tags[0] == ''"  class="flex">
            <div class=" self-end mr-[2px]">No tags!  (<span class=" text-cyan-500">╥</span>_<span class=" text-cyan-500">╥</span>)</div>
          </div>
        </div>
        
        <div class=" bg-lime-300 rounded-r-[13px] rounded-bl-2xl grid box-content">
          <div class="  place-self-center py-2 px-3 border-[.1em] border-black border-dashed border-spacing-5 rounded-r-md rounded-bl-md">
            <div class=" text-center leading-[0.9] text-[38px] font-semibold ">{{ formatDay(question.pub_date) }}</div>
            <div class=" text-center text-[16px] font-medium leading-none ">{{ formatMonthYear(question.pub_date).toLowerCase() }}</div>
          </div>
        </div>
      </a>
      </div>
      <div>
      <h2 class="pl-10 text-2xl mt-16 mb-6">All questions</h2>

      <a v-for="question in questions" :key="question.id" :href="`/question/${question.id}`" 
      class="grid grid-cols-[100px_1fr_95px] mx-10 mb-[10px] box-content min-h-[98px] rounded-2xl bg-gradient-to-l from-[#f1fffd] to-[#ffffff] border-[0.24em] border-black " style="box-shadow: .27em .27em;">
        <div class="grid grid-rows-3 text-right  text-xs font-medium pr-2 border-r-[0.2em] border-gray-200 my-3  object-fill box-content">
          <div class=" self-start ">{{ question.score }} votes</div>
          <div class=" self-center ">{{ question.num_answers }} answers</div>
          <span class=" self-end  ">{{ question.views }} views</span>
        </div>

        <div class="grid grid-rows-3 pl-2 text-xs font-medium py-3  box-content object-fill">
          <div class=" truncate self-start text-base leading-[1.15] text-blue-500 hover:underline hover:text-blue-400">{{ question.title }}</div>
          <div class=" self-center ">Asked by <span  v-if="question.author" class="text-blue-500 hover:underline hover:text-blue-400">{{ question.author  }}</span><span  v-if="!(question.author)" class="">Anonymous</span></div>
          <div v-if="question.tags[0] != ''"  class="flex">
            <div v-for="tag in question.tags" class=" self-end mr-[2px] text-blue-500 hover:underline hover:text-blue-400">[{{ tag }}]</div>
          </div>
          <div v-if="question.tags[0] == ''"  class="flex">
            <div class=" self-end mr-[2px]">No tags!  (<span class=" text-cyan-500">╥</span>_<span class=" text-cyan-500">╥</span>)</div>
          </div>
        </div>
        
        <div class=" bg-lime-300 rounded-r-[13px] rounded-bl-2xl grid box-content">
          <div class="  place-self-center py-2 px-3 border-[.1em] border-black border-dashed border-spacing-5 rounded-r-md rounded-bl-md">
            <div class=" text-center leading-[0.9] text-[38px] font-semibold ">{{ formatDay(question.pub_date) }}</div>
            <div class=" text-center text-[16px] font-medium leading-none ">{{ formatMonthYear(question.pub_date).toLowerCase() }}</div>
          </div>
        </div>
      </a>
      </div>
    </div>
    <div class="hidden flex-col bg-gray-200 w-[30%] p-3  md:block">


    </div>
  </div>
</template>

<script>
import axiosClient from "@/views/axiosClient";

export default {
  name: "ModuleView",
  data() {
    return {
      questions: [],
      popQuestions: []
    };
  },
  mounted() {
    axiosClient({
      method: "get",
      url: `/module/${this.$route.params.mod}/`,
    })
        .then((response) => {
          this.questions = response.data;
          this.questions.reverse()
          this.popQuestions = this.questions
          this.popQuestions = this.popQuestions.filter(a => withinTime(a.pub_date, 5) )
          this.popQuestions = this.popQuestions.sort((a,b) => b.views - a.views).slice(0,3)
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
import { formatDay } from "./dateUtils";
import { formatMonthYear } from "./dateUtils"; 
import { withinTime } from "./dateUtils"

</script>
<script>
// import { Ref } from 'vue';
import {QuillEditor} from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import axiosClient from "@/views/axiosClient";

export default {
  name: 'ask_questions',
  components: {
    QuillEditor
  },
  data() {
    return {
      questionTitle: '',
      questionExplanation: '',
      questionTags: '',
      questionSummary: '',
      questionAnswer: '',
      questionAnswerExplanation: '',
      questionAnswerTags: '',
      questionAnswerSummary: '',
    }
  },
  methods: {
    addQuestion() {
      console.log(this.questionTitle)
      console.log(this.questionExplanation)
      console.log(this.questionTags)
      console.log(this.questionSummary)
      console.log(this.questionAnswer)
      console.log(this.questionAnswerExplanation)
      console.log(this.questionAnswerTags)
      console.log(this.questionAnswerSummary)
    }
  }
}


</script>

<template>

  <div class="absolute left-2/3 ml-7 mt-0.5 w-0.5 h-full bg-gray-600"></div>
  <div class="absolute left-2/3 ml-7 mt-96 w-0.5 h-full bg-gray-600"></div>




  <div class="grid grid-cols-2 items-start" style="grid-template-columns: 2fr 1fr;">
    <div>
    <label for="message" class="block text-lg font-medium text-gray-900">Title</label>
    <textarea id="message" rows="1"
              class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Enter your title" v-model="questionTitle"></textarea>
    
<!-- Explain your problem -->
  <div class="w-full">
    <label for="large-input" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">Explain your problem</label>
    <QuillEditor id="large-input" theme="snow" toolbar="full" class="h-40">
    </QuillEditor>
  </div>


<!-- what have you already tried? -->
  <div class="w-full">
    <label for="large-input" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">What have you already tried?</label>
    <QuillEditor id="large-input" theme="snow" toolbar="full" class="h-40">
    </QuillEditor>
  </div>

  
  <!--summary-->
  <div class>
    <label for="message" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">Summary (optional)</label>
    <textarea id="message" rows="1"
              class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Type or auto-generate summary"></textarea>
    <button type="button"
            class=" mt-3 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 ">
      Auto-generate summary
    </button>
  </div>


  <!--tags-->
  <div class="mb-6">
    <label for="message" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">Tags</label>
    <textarea id="message" rows="1"
              class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Type or auto-generate tags"></textarea>
    <button type="button"
            class="mt-3 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
      Auto-generate tags
    </button>
  </div>

    </div>

    
    <div>
    <p class=" flex justify-end text-black mr-40 text-lg font-medium underline">Rules:</p>
    <div class="flex justify-end">
    <div class="w-11/12">
      <ol class="list-decimal list-inside">
        <li class="mb-2 break-words">No subtle put-downs or unfriendly language.</li>
        <li class="mb-2 break-words">No name-calling or personal attacks.</li>
        <li class="mb-2 break-words">No bigotry.</li>
        <li class="mb-2 break-words">No harassment.</li>
        <li class="mb-2 break-words">Report any unacceptable behaviour</li>


        <p class=" flex justify-end text-black mr-16 text-lg font-medium underline">How to write a good question!</p>

        <li class="mb-2 break-words">Make sure your question is on-topic and suitable for this site</li>
        <li class="mb-2 break-words">Search, and research</li>
        <li class="mb-2 break-words">Write a title that summarizes the specific problem</li>
        <li class="mb-2 break-words">Introduce the problem before you post any code</li>
        <li class="mb-2 break-words">Help othersreproduce the problem </li>
        <li class="mb-2 break-words">Check if the auto generated tags are relevant</li>
        <li class="mb-2 break-words">Proofread before posting!</li>
        <li class="mb-2 break-words">Ensure that the summary properly captures your question</li>
        <li class="mb-2 break-words">Make sure to respond to feedback after posting!!</li>

      </ol>
    </div>
  </div>
    </div>


  </div>

  <div>


  </div>


  <button v-on:click="addQuestion" type="button"
          class="mt-3 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
    Add Question
    </button>


</template>

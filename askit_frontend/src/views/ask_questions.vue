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

  <!-- <p class= ".p-52">rules</p> -->
  <!-- <label for="message" class="block -ml-40 text-lg font-medium text-gray-900 dark:text-black">Title</label> -->

  <div>
    <label for="message" class="block mb-2 text-lg font-medium text-gray-900">Title</label>
    <textarea id="message" rows="1"
              class="block p-2.5 w-2/3 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Enter your title" v-model="questionTitle"></textarea>
  </div>


  <div class="w-2/3">
    <label for="large-input" class="block mb-2 text-lg font-medium text-green-700">Explain your
      problem</label>
    <QuillEditor id="large-input" theme="snow" toolbar="full" class="h-52">
    </QuillEditor>
  </div>


  <div class="w-2/3">
    <label for="large-input" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">What have you already
      tried?</label>

    <QuillEditor id="large-input" theme="snow" toolbar="full">
    </QuillEditor>
  </div>

  <!--summary-->
  <div class>
    <label for="message" class="block mb-2 text-lg font-medium text-green-700">Summary
      (optional)</label>
    <textarea id="message" rows="1"
              class="block p-2.5 w-2/3 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
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
              class="block p-2.5 w-2/3 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Type or auto-generate tags"></textarea>
    <button type="button"
            class="mt-3 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
      Auto-generate tags
    </button>
  </div>

  <button v-on:click="addQuestion" type="button"
          class="mt-3 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
    Add Question
    </button>


</template>

<script>
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import axiosClient from "@/views/axiosClient";

export default {
  name: 'AskView',
  components: {
    QuillEditor
  },
  data() {
    return {
      tagClass: "mt-3 mr-2 mb-2 rounded-lg bg-blue-700 px-5 text-sm font-medium text-white py-2.5 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300",
      isSummDisabled: false,
      isTagDisabled: false,
      isAskDisabled: false,
      summaryLoadWheel: 'hidden',
      tagLoadWheel: 'hidden',
      askLoadWheel: 'hidden',
      questionTitle: '',
      questionExplanation: '',
      questionTried: '',
      questionTags: '',
      questionSummary: '',
      suggestQuestion: {
        title: 'suggest question title',
        explanation: 'suggest question explanation',
        tags: 'suggest question tags',
        summary: 'suggest question summary',
        id: -1,
      },
      showSuggestQuestion: false,
    }
  },
  methods: {
    addQuestion() {
      this.isAskDisabled = true
      this.askLoadWheel = 'flex pl-1'

      this.getSuggestQuestion()

    },


    submitQuestion() {
      axiosClient.post(`/ask/module/${this.$route.params.mod}/`, {
        title: this.questionTitle,
        explanation: this.questionExplanation,
        tried: this.questionTried,
        tags: this.questionTags,
        summary: this.questionSummary,
      })
          .then((response) => {
            console.log(response);
            // redirect to question base on response.id
            window.location.href = '/question/' + response.data.id;
          })
          .catch((error) => {
            console.log(error);
          });
    },

    getSummary() {
      this.isSummDisabled = true
      this.summaryLoadWheel = 'flex pl-1'
      axiosClient.post("/ask/summary/", {
        title: this.questionTitle,
        explanation: this.questionExplanation,
        tried: this.questionTried,
      })
          .then((response) => {
            this.summaryLoadWheel = 'hidden'
            this.questionSummary = response.data.summary;
            this.isSummDisabled = false
          })
          .catch((error) => {
            this.isSummDisabled = false
            this.summaryLoadWheel = 'hidden'
            console.log(error);
          });
    },

    getTags() {
      this.isTagDisabled = true
      this.tagLoadWheel = 'flex pl-1'
      axiosClient.post("/ask/tagging/", {
        title: this.questionTitle,
        explanation: this.questionExplanation,
        tried: this.questionTried,
      })
          .then((response) => {
            this.tagLoadWheel = 'hidden'
            this.questionTags = response.data.tag.join(', ');
            this.isTagDisabled = false
          })
          .catch((error) => {
            this.isTagDisabled = false
            this.tagLoadWheel = 'hidden'
            console.log(error);
          });
    },

    get_spacy() {
      axiosClient.post("/ask/spacy/", {
        title: this.questionTitle,
        explanation: this.questionExplanation,
        tried: this.questionTried,
      })
          .then((response) => {
            console.log(response);
          })
          .catch((error) => {
            console.log(error);
          });
    },

    getSuggestQuestion() {
      axiosClient.post(`/ask/suggest/${this.$route.params.mod}/`, {
        title: this.questionTitle,
        explanation: this.questionExplanation,
        tags : this.questionTags,
      })
          .then((response) => {
            console.log(response);
            if (response.data.success === false) {
              this.submitQuestion();
              return;
            }
            this.suggestQuestion = response.data;
            this.showSuggestQuestion = true;
          })
          .catch((error) => {
            console.log(error);
          });
    },

    acceptSuggestion() {
      this.showSuggestQuestion = false;
      window.location.href = '/question/' + this.suggestQuestion.id;
    },

    denySuggestion() {
      this.showSuggestQuestion = false;
      this.submitQuestion();
    },
  }
}

</script>

<template>

  <!-- HTML code for the pop-up window -->
<!-- HTML code for the pop-up window -->
<div class="fixed z-10 inset-0 overflow-y-auto dark:bg-gray-900" v-if="showSuggestQuestion">
  <div class="flex items-center justify-center min-h-screen">
    <div class="bg-white dark:bg-gray-800 w-full max-w-md p-6 rounded-lg shadow-lg">
      <h2 class="text-lg font-medium mb-4 dark:text-white">Is this question the same as your question?</h2>
      <p class="mb-4 dark:text-gray-300">Title: {{ suggestQuestion.title }}</p>
      <p class="mb-4 dark:text-gray-300">Summary: {{ suggestQuestion.summary }}</p>
      <p class="mb-4 dark:text-gray-300">Explanation: {{ suggestQuestion.explanation }}</p>
      <p class="mb-4 dark:text-gray-300">Tags: {{ suggestQuestion.tags }}</p>
      <div class="flex">
        <button class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded m-1 dark:bg-red-600" v-on:click="acceptSuggestion">
          Yes, DELETE my question and view that question
        </button>
        <button class="transition focus:ring-4 focus:outline-none focus:ring-pink-400 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded m-1 dark:bg-blue-600" v-on:click="denySuggestion">
          No
        </button>
      </div>
    </div>
  </div>
</div>



  <div class=" dark:bg-gray-900 flex">

    <div class="w-full pt-2 pl-4 md:w-2/3">
      <label for="message" class="block text-lg font-medium dark:text-white text-gray-900">Title</label>
      <textarea id="message" rows="1"
                class="transition focus:ring-2 focus:outline-none  block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:text-white"
                placeholder="Enter your title" v-model="questionTitle"></textarea>


      <!-- Explain your problem -->
      <div class="w-full">
        <label for="large-input" class="mb-2 block text-lg font-medium dark:text-white text-gray-900">Explain your problem</label>
        <QuillEditor id="large-input" theme="snow" toolbar="full" class="h-72" v-model:content="questionExplanation"
                     content-type="text">
        </QuillEditor>
      </div>


      <!-- what have you already tried? -->
      <div class="w-full">
        <label for="large-input" class="mb-2 block text-lg font-medium dark:text-white text-gray-900">What have you already
          tried?</label>
        <QuillEditor id="large-input" theme="snow" toolbar="full" class="h-40" v-model:content="questionTried"
                     content-type="text">
        </QuillEditor>
      </div>

      <!--summary-->
      <div class>
        <label for="message" class="mb-2 block text-lg font-medium dark:text-white text-gray-900">Summary (optional)</label>
        <textarea :disabled="isSummDisabled" id="message" rows="1"
                  class="transition focus:ring-2 focus:outline-none block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500  dark:bg-gray-800 dark:text-white"
                  placeholder="Type or auto-generate summary" v-model="questionSummary"></textarea>
        <div class="flex items-center">
          <button type="button" :disabled="isSummDisabled"
                  class="transition focus:outline-none  mt-3 mr-2 mb-2 rounded-lg bg-blue-700 px-5 text-sm font-medium text-white py-2.5 hover:bg-blue-800 focus:ring-4 focus:ring-pink-400 disabled:bg-slate-500"
                  v-on:click="getSummary">
            Auto-generate summary
            <i class="fa fa-list scale-100" aria-hidden="true"></i>

          </button>
          <div role="status" :class="summaryLoadWheel">
            <svg aria-hidden="true" class="w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                 viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                  d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                  fill="currentColor"/>
              <path
                  d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                  fill="currentFill"/>
            </svg>
            <span class="sr-only">Loading...</span>
          </div>
        </div>
      </div>

      <!--tags-->
      <div class="mb-6">
        <label for="message" class="mb-2 block text-lg font-medium dark:text-white text-gray-900">Tags</label>

        <textarea :disabled="isTagDisabled" id="message" rows="1"
                  class="transition focus:ring-2 focus:outline-none block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-600 dark:bg-gray-800 dark:text-white"
                  placeholder="Type or auto-generate tags" v-model="questionTags"></textarea>
        <div class="flex items-center">
          <button type="button" :disabled="isTagDisabled"
                  class="transition focus:outline-none mt-3 mr-2 mb-2 rounded-lg bg-blue-700 px-5 text-sm font-medium text-white py-2.5 hover:bg-blue-800 focus:ring-4 focus:ring-pink-400 disabled:bg-slate-600"
                  v-on:click="getTags">
            Auto-generate tags
            <i class="fa fa-tags scale-100" aria-hidden="true"></i>

          </button>
          
          <div role="status" :class="tagLoadWheel">
            <svg aria-hidden="true" class="w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                 viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                  d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                  fill="currentColor"/>
              <path
                  d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                  fill="currentFill"/>
            </svg>
            <span class="sr-only">Loading...</span>
          </div>
        </div>
      </div>

      <div class="flex items-center">
        <button v-on:click="addQuestion" type="button" :disabled="isAskDisabled"
                class="transition focus:outline-none mt-3 mr-2 mb-2 rounded-lg bg-blue-700 px-5 text-sm font-medium text-white py-2.5 hover:bg-blue-800 focus:ring-4 focus:ring-pink-400 disabled:bg-slate-600">
          Add Question
          <i class="fa fa-paper-plane scale-100" aria-hidden="true"></i>

        </button>
        <div role="status" :class="askLoadWheel">
          <svg aria-hidden="true" class="w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
               viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
                d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                fill="currentColor"/>
            <path
                d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                fill="currentFill"/>
          </svg>
          <span class="sr-only">Loading...</span>
        </div>
      </div>
    </div>

    <div class="hidden md:block md:w-1/3">
      <div class="text-center">
        <p class="text-lg font-medium dark:text-white text-black underline">Rules:</p>
      </div>
      <div class="flex justify-end">
        <div class="w-11/12">
          <ol class="list-inside list-decimal">
            <li class="mb-2 break-words">No subtle put-downs or unfriendly language.</li>
            <li class="mb-2 break-words">No name-calling or personal attacks.</li>
            <li class="mb-2 break-words">No bigotry.</li>
            <li class="mb-2 break-words">No harassment.</li>
            <li class="mb-2 break-words">Report any unacceptable behaviour</li>


            <div class="text-center">
              <p class="text-lg font-medium dark:text-white text-black underline">How to write a good
                question!</p>
            </div>

            <li class="mb-2 break-words">Make sure your question is on-topic and suitable for this site</li>
            <li class="mb-2 break-words">Search, and research</li>
            <li class="mb-2 break-words">Write a title that summarizes the specific problem</li>
            <li class="mb-2 break-words">Introduce the problem before you post any code</li>
            <li class="mb-2 break-words">Help others reproduce the problem</li>
            <li class="mb-2 break-words">Check if the auto generated tags are relevant</li>
            <li class="mb-2 break-words">Proofread before posting!</li>
            <li class="mb-2 break-words">Ensure that the summary properly captures your question</li>
            <li class="mb-2 break-words">Make sure to respond to feedback after posting!!</li>

          </ol>
        </div>
      </div>
    </div>
  </div>

</template>

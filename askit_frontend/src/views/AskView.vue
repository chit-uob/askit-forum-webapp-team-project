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
      summaryLoadWheel: 'hidden',
      tagLoadWheel: 'hidden',
      questionTitle: '',
      questionExplanation: '',
      questionTried: '',
      questionTags: '',
      questionSummary: '',
    }
  },
  methods: {
    addQuestion() {
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
      this.summaryLoadWheel = 'flex pl-1'
      axiosClient.post("/ask/summary/", {
        title: this.questionTitle,
        explanation: this.questionExplanation,
        tried: this.questionTried,
      })
          .then((response) => {
            this.summaryLoadWheel = 'hidden'
            this.questionSummary = response.data.summary;
          })
          .catch((error) => {
            this.summaryLoadWheel = 'hidden'
            console.log(error);
          });
    },

    getTags() {
      this.tagLoadWheel = 'flex pl-1'
      axiosClient.post("/ask/tagging/", {
        title: this.questionTitle,
        explanation: this.questionExplanation,
        tried: this.questionTried,
      })
          .then((response) => {
            this.tagLoadWheel = 'hidden'
            this.questionTags = response.data.tag.join(', ');
          })
          .catch((error) => {
            this.tagLoadWheel = 'hidden'
            console.log(error);
          });
    }
  }
}

</script>

<style>

/* .h-screen {
    height: 100vh;
  } */
.loading{
display: initial;
}
</style>
<template>

   <!-- <div class="absolute left-2/3 ml-5 h-96 bg-gray-600 w-0.5"></div>
   <div class="absolute left-2/3 ml-5 h-96 mt-96 bg-gray-600 w-0.5"></div> 
   <div class="absolute  bottom-28 left-2/3 ml-5 h-72 mt-12 bg-gray-600 w-0.5"></div>  -->

   <!-- <div class="h-screen flex left-2/3 ml-5">
    <div class="h-full w-1 bg-gray-500"></div>
  </div> -->


  <div class="flex">

    <div class="w-full pt-2 pl-4 md:w-2/3">
      <label for="message" class="block text-lg font-medium text-gray-900">Title</label>
      <textarea id="message" rows="1"
                class="block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500"
                placeholder="Enter your title" v-model="questionTitle"></textarea>

                
      <!-- Explain your problem -->
      <div class="w-full">
        <label for="large-input" class="mb-2 block text-lg font-medium text-gray-900">Explain your problem</label>
        <QuillEditor id="large-input" theme="snow" toolbar="full" class="h-72" v-model:content="questionExplanation"
                     content-type="json">
        </QuillEditor>
      </div>


      <!-- what have you already tried? -->
      <div class="w-full">
        <label for="large-input" class="mb-2 block text-lg font-medium text-gray-900">What have you already
          tried?</label>
        <QuillEditor id="large-input" theme="snow" toolbar="full" class="h-40" v-model:content="questionTried"
                     content-type="json">
        </QuillEditor>
      </div>

      <!--summary-->
      <div class>
        <label for="message" class="mb-2 block text-lg font-medium text-gray-900">Summary (optional)</label>
        <textarea id="message" rows="1"
                  class="block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500"
                  placeholder="Type or auto-generate summary" v-model="questionSummary"></textarea>
        <div class="flex items-center">
        <button type="button"
                class="mt-3 mr-2 mb-2 rounded-lg bg-blue-700 px-5 text-sm font-medium text-white py-2.5 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300"
                v-on:click="getSummary">
          Auto-generate summary
        </button>
        <div role="status" :class="summaryLoadWheel">
          <svg aria-hidden="true" class="w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
            <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
          </svg>
          <span class="sr-only">Loading...</span>
        </div>
        </div>
      </div>

      <!--tags-->
      <div class="mb-6">
        <label for="message" class="mb-2 block text-lg font-medium text-gray-900">Tags</label>
        <textarea id="message" rows="1"
                  class="block w-full rounded-lg border border-gray-300 bg-gray-50 text-sm text-gray-900 p-2.5 focus:border-blue-500 focus:ring-blue-500"
                  placeholder="Type or auto-generate tags" v-model="questionTags"></textarea>
        <div class="flex items-center">
        <button type="button"
                class="mt-3 mr-2 mb-2 rounded-lg bg-blue-700 px-5 text-sm font-medium text-white py-2.5 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300"
                v-on:click="getTags">
          Auto-generate tags
        </button>
        <div role="status" :class="tagLoadWheel">
          <svg aria-hidden="true" class="w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
            <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
          </svg>
          <span class="sr-only">Loading...</span>
        </div>
        </div>
      </div>

      <button v-on:click="addQuestion" type="button"
              class="mt-3 mr-2 mb-2 rounded-lg bg-blue-700 px-5 text-sm font-medium text-white py-2.5 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300">
        Add Question
      </button>
    </div>

    <div class="hidden md:block md:w-1/3">
      <div class="text-center">
        <p class="text-lg font-medium text-black underline">Rules:</p>
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
              <p class="text-lg font-medium text-black underline">How to write a good
                question!</p>
            </div>

            <li class="mb-2 break-words">Make sure your question is on-topic and suitable for this site</li>
            <li class="mb-2 break-words">Search, and research</li>
            <li class="mb-2 break-words">Write a title that summarizes the specific problem</li>
            <li class="mb-2 break-words">Introduce the problem before you post any code</li>
            <li class="mb-2 break-words">Help othersreproduce the problem</li>
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

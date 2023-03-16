<template>
  <div class="bg-sky-100">
    <div class="max-w-6xl mx-auto bg-white shadow-lg overflow-hidden w-10/12">
      <div class="p-4 flex items-center">
        <div class="flex flex-col items-center">
          <button class="bg-green-500 hover:bg-green-600 text-white font-bold py-1 px-2 rounded mr-2"
                  v-on:click="upvoteQuestion">
            <i class="fa fa-arrow-up"></i>
          </button>
          <span class="text-gray-600 text-lg font-bold mr-2">{{ question.score }}</span>
          <button class="bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-2 rounded mr-2"
                  v-on:click="downvoteQuestion">
            <i class="fa fa-arrow-down"></i>
          </button>
        </div>
        <div class="flex-grow">
          <h1 class="p-2 text-3xl font-bold font-mono">{{ question.title }}</h1>
          <div class="flex justify-between mb-2">
            <p class="p-2 font-thin font-sans">Author: {{ question.author }}</p>
            <span class="text-gray-600 w-full text-right">Date Published: {{ formatPubDate(question.pub_date) }}</span>
          </div>
          <div>

            <p class="p-2 mb-2"><span class="font-bold">Explanation:</span> <br>
              {{ question.explanation }}
            </p>
            <p class="p-2 mb-2"><span class="font-bold">Tried what:</span> <br>
              {{ question.tried_what }}</p>
            <p class="p-2 mb-2"><span class="font-bold">Summary:</span> <br>
              {{ question.summary }}</p>
            <div class="flex">
              <div v-for="tag in question.tags" class="mr-2">
                <button class="bg-blue-50 hover:bg-blue-100 text-blue-400  py-1 px-2 rounded ">{{ tag }}</button>
              </div>
            </div>
          </div>

        </div>
      </div>
      <div class="px-2 flex justify-center">
        <button
            class="bg-blue-100 hover:bg-blue-300 text-black font-sans font-bold py-2 px-4 ml-4 rounded border-gray-300 w-5/6"
            @click="showForm = !showForm">Answer this question
        </button>
      </div>
      <div v-if="showForm" class="p-2 flex justify-center">
        <form @submit.prevent="addAnswer" class="w-5/6">
          <br>
          <div>
            <QuillEditor theme="snow" toolbar="full" name="content" v-model:content="answerInput" contentType="text">
            </QuillEditor>
          </div>
          <br>
          <button class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 ml-4 rounded" type="submit">
            Submit answer
          </button>
        </form>
      </div>
      <div class="p-5">

        <h1 class="text-2xl font-bold mb-4">Answers:</h1>

        <div v-for="answer in answers" :key="answer.id">
          <div class="p-4 flex items-center mb-4 bg-white rounded-lg shadow">
            <div class="flex flex-col items-center">
              <button class="bg-green-500 hover:bg-green-600 text-white font-bold py-1 px-2 rounded mr-2"
                      v-on:click="upvoteAnswer(answer.id)">
                <i class="fa fa-arrow-up"></i>
              </button>
              <span class="text-gray-600 text-lg font-bold mr-2">{{ answer.score }}</span>
              <button class="bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-2 rounded mr-2"
                      v-on:click="downvoteAnswer(answer.id)">
                <i class="fa fa-arrow-down"></i>
              </button>
            </div>
            <div class="flex-grow">
              <div class="flex justify-between">
                <p class="text-gray-600 text-sm">Author: {{ answer.author }} </p>
                <p class="text-gray-600 text-sm text-right ">Published: {{ formatPubDate(answer.pub_date) }}</p>
              </div>
              <p v-if="answer.is_solution" class="text-green-500 text-sm font-semibold mt-2">Solution</p>
              <p class="text-lg">{{ answer.content }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axiosClient from "@/views/axiosClient";

export default {
  name: "QuestionView",
  data() {
    return {
      showForm: false,

      question: {
        title: "Loading...",
        explanation: "Loading...",
        tried_what: "Loading...",
        summary: "Loading...",
        pub_date: "2000-01-01T00:00:00Z",

      },
      answers: [],
      answerInput: "",
    };
  },
  mounted() {
    axiosClient({
      method: "get",
      url: `/question/${this.$route.params.id}/`,
    })
        .then((response) => {
          this.question = response.data;
          this.answers = response.data.answer_list.sort((a, b) => b.score - a.score);
        })
        .catch((error) => {
          console.log(error);
        });
  },
  methods: {
    addAnswer() {
      console.log(this.answerInput)
      axiosClient.post(`/question/${this.$route.params.id}/submit_answer/`,
          {
            content: this.answerInput,
          })
          .then((response) => {
            this.answers.push(response.data);
            this.answerInput = "";
            this.showForm = false;
          })
          .catch((error) => {
            console.log(error);
          });
    },

    upvoteQuestion() {
      axiosClient.post(`/question/${this.$route.params.id}/upvote/`)
          .then((response) => {
            this.question.score = response.data.score;
          })
          .catch((error) => {
            console.log(error);
          });
    },
    downvoteQuestion() {
      axiosClient.post(`/question/${this.$route.params.id}/downvote/`)
          .then((response) => {
            this.question.score = response.data.score;
          })
          .catch((error) => {
            console.log(error);
          });
    },
    upvoteAnswer(answerId) {
      axiosClient.post(`/question/${this.$route.params.id}/answer/${answerId}/upvote/`)
          .then((response) => {
            this.answers = this.answers.map((answer) => {
              if (answer.id === answerId) {
                answer.score = response.data.score;
              }
              return answer;
            }).sort((a, b) => b.score - a.score);
          })
          .catch((error) => {
            console.log(error);
          });
    },
    downvoteAnswer(answerId) {
      axiosClient.post(`/question/${this.$route.params.id}/answer/${answerId}/downvote/`)
          .then((response) => {
            this.answers = this.answers.map((answer) => {
              if (answer.id === answerId) {
                answer.score = response.data.score;
              }
              return answer;
            }).sort((a, b) => b.score - a.score);
          })
          .catch((error) => {
            console.log(error);
          });

    },
  },
};
</script>
<script setup>
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import { formatPubDate } from "./dateUtils";

</script>

<style scoped>

</style>
<template>
  <body style="background-color:#dbeafe; ">
  <div class="max-w-6xl mx-auto bg-white rounded-lg shadow-lg overflow-hidden" style="width:90%;">
    <div class="p-4 flex items-center">
      <div class="flex flex-col items-center">
        <button class="bg-green-500 hover:bg-green-600 text-white font-bold py-1 px-2 rounded mr-2">
          <i class="fa fa-arrow-up" v-on:click="upvoteQuestion"></i>
        </button>
        <span class="text-gray-600 text-lg font-bold mr-2">{{ question.score }}</span>
        <button class="bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-2 rounded mr-2">
          <i class="fa fa-arrow-down" v-on:click="downvoteQuestion"></i>
        </button>
      </div>
      <div class="flex-grow">
        <h1 class="p-2 text-3xl font-bold font-mono">Question {{ question.title }}</h1>
        <div class="flex justify-between mb-2">
          <p class="p-2 font-thin font-sans"> Abc(abc123@student.bham.ac.uk){{ question.author }}</p>
          <span class="text-gray-600 w-full text-right">Date Published: {{ question.pub_date }}</span>
        </div>
        <div>
          <p class="p-2 mb-2">{{ question.explanation }},{{ question.author }}, {{ question.module }}, {{
              question.tried_what
            }}, {{ question.summary }}, {{ question.pub_date }},
            {{ question.status }}, {{ question.views }}, {{ question.upvote_or_downvote }},
            {{ question.tags }}{{ question.tags }}{{ question.tags }}{{ question.tags }}{{
              question.tags
            }}{{ question.tags }}{{ question.tags }}{{ question.tags }}{{ question.tags }}{{ question.tags }}</p>
          <button class="bg-blue-50 hover:bg-blue-100 text-blue-400  py-1 px-2 rounded ">{{ question.tags }}</button>

        </div>
      </div>
    </div>
    <div class="p-10">

      <button
          class="bg-blue-200 hover:bg-blue-300 text-black font-sans font-bold py-2 px-4 ml-4 rounded border-gray-300"
          @click="showForm = !showForm">Answer
      </button>

      <div v-if="showForm">

        <form @submit.prevent="addAnswer">
          <br>
          <input class="border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none"
                 type="text" name="content" v-model="answerInput">

          <button class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 ml-4 rounded" type="submit">
            Submit answer
          </button>
        </form>
      </div>

      <br><br>

      <h1 class="text-2xl font-bold mb-4">Answers:</h1>

      <!--        {% for answer in answer_list %}-->
      <div v-for="answer in answers" :key="answer.id">
        <div class="p-4 flex items-center mb-4 bg-white rounded-lg shadow">
          <div class="flex flex-col items-center">
            <button class="bg-green-500 hover:bg-green-600 text-white font-bold py-1 px-2 rounded mr-2">
              <i class="fa fa-arrow-up"></i>
            </button>
            <span class="text-gray-600 text-lg font-bold mr-2">{{ answer.score }}</span>
            <button class="bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-2 rounded mr-2">
              <i class="fa fa-arrow-down"></i>
            </button>
          </div>
          <div class="flex-grow">
            <div class="flex justify-between">
              <p class="text-gray-600 text-sm">Author: abc123@student.bham.ac.uk {{ answer.author }} </p>
              <p class="text-gray-600 text-sm text-right ">Published: {{ answer.pub_date }}</p>
            </div>
            <p v-if="answer.is_solution" class="text-green-500 text-sm font-semibold mt-2">Solution</p>
            <p class="text-lg">{{ answer.content }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  </body>
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
          console.log(response.data)
          this.answers = response.data.answer_list;
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
  },
};
</script>

<style scoped>

</style>
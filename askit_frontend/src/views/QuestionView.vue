<template>
  <div class="max-w-6xl mx-auto bg-white rounded-lg shadow-lg overflow-hidden" style="width:90%;">
    <div class="p-4 flex items-center">
      <div class="flex flex-col items-center">
        <button class="bg-green-500 hover:bg-green-600 text-white font-bold py-1 px-2 rounded mr-2">
          <i class="fa fa-arrow-up"></i>
        </button>
        <span class="text-gray-600 text-lg font-bold mr-2">{{ question.score }}</span>
        <button class="bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-2 rounded mr-2">
          <i class="fa fa-arrow-down"></i>
        </button>
      </div>
      <div>
        <h1 class="text-3xl font-bold ">{{ question.title }}</h1>
        <p class="mb-2">{{ question.explanation }},{{ question.author }}, {{ question.module }}, {{
            question.tried_what
          }}, {{ question.summary }}, {{ question.pub_date }},
          {{ question.status }}, {{ question.score }}, {{ question.views }}, {{ question.upvote_or_downvote }},
          {{ question.tags }}</p>
      </div>
    </div>
    <div class="p-4">
      <p class="mb-4">{{ question.author }}, {{ question.module }}, {{ question.explanation }}, {{
          question.tried_what
        }}, {{ question.summary }}, {{ question.pub_date }},
        {{ question.status }}, {{ question.score }}, {{ question.views }}, {{ question.upvote_or_downvote }},
        {{ question.tags }}</p>
      <form @submit.prevent="addAnswer" class="mt-4">
        <!--          {% csrf_token %}-->
        <div class="flex items-center">
          <input class="border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none"
                 type="text" name="content" v-model="answerInput">
          <button class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 ml-4 rounded" type="submit">
            Submit answer
          </button>
        </div>
        <br><br>
      </form>
      <h1 class="text-2xl font-bold mb-4">Answers:</h1>

      <!--        {% for answer in answer_list %}-->
      <div v-for="answer in answers" :key="answer.id">
        <div class="p-4 mb-4 bg-white rounded-lg shadow">
          <p class="text-lg">{{ answer.content }}</p>
          <p class="text-gray-600 text-sm mt-2">Author: {{ answer.author }} | Published: {{ answer.pub_date }} | Score:
            {{ answer.score }}</p>
          <p v-if="answer.is_solution" class="text-green-500 text-sm font-semibold mt-2">Solution</p>
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
  },
};
</script>

<style scoped>

</style>
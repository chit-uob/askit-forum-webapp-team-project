<template>
  <div class="bg-sky-100">
    <div class="mx-auto w-10/12 max-w-6xl overflow-hidden bg-white shadow-lg">
      <div class="flex items-center p-4">
        <div class="flex flex-col items-center">
          <button class="mr-2 rounded bg-green-500 px-2 py-1 font-bold text-white hover:bg-green-600"
                  :class="{ 'border border-4 border-green-600': question.upvote_or_downvote === 'upvote'}"
                  v-on:click="upvoteQuestion">
            <i class="fa fa-arrow-up"></i>
          </button>
          <span class="mr-2 text-lg font-bold text-gray-600">{{ question.score }}</span>
          <button class="mr-2 rounded bg-red-500 px-2 py-1 font-bold text-white hover:bg-red-600"
                  :class="{ 'border border-4 border-red-600': question.upvote_or_downvote === 'downvote'}"
                  v-on:click="downvoteQuestion">
            <i class="fa fa-arrow-down"></i>
          </button>
        </div>
        <div class="flex-grow">
          <div class="flex justify-between items-center mb-2">
            <h1 class="p-2 font-mono text-3xl font-bold">{{ question.title }}</h1>
            <button  v-if=" question.author != 'adinotadmin@mail.com' "   v-on:click="deleteQuestion" type="button"
                      class="justify-between rounded-lg bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-blue-300">
                Delete Question
            </button>
          </div>
          <div class="mb-2 flex justify-between">
            <p class="p-2 font-sans font-thin w-full">Author: {{ question.author }}</p>
            <span class="w-full text-right text-gray-600">Date Published: {{ formatPubDate(question.pub_date) }}</span>
          </div>
          <div>
            <p class="mb-2 p-2"><span class="font-bold">Explanation:</span> <br>
              {{ question.explanation }}
            </p>
            <p class="mb-2 p-2"><span class="font-bold">Tried what:</span> <br>
              {{ question.tried_what }}</p>
            <p class="mb-2 p-2"><span class="font-bold">Summary:</span> <br>
              {{ question.summary }}</p>
            <div class="flex">
              <div v-for="tag in question.tags" class="mr-2">
                <button class="rounded bg-blue-50 px-2 py-1 text-blue-400 hover:bg-blue-100">{{ tag }}</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="flex justify-center px-2">
        <br>
      </div>

      <div class="p-5">
        <div class="flex items-center">
          <h1 class="font-bold">Comments:</h1>
          <button
              class="ml-4 rounded border-gray-300 bg-blue-100 px-4 py-1 font-sans font-bold text-black hover:bg-blue-300"
              @click="showComments = !showComments">Add Comment
          </button>
        </div>
        <div v-if="showComments" class="flex justify-center p-2">
          <form @submit.prevent="addComment" class="w-5/6">
            <br>
            <div>
              <QuillEditor theme="snow" toolbar="full" name="content" v-model:content="commentInput" contentType="text">
              </QuillEditor>
            </div>
            <br>
            <button class="ml-4 rounded bg-blue-500 px-4 py-2 font-bold text-white hover:bg-blue-600" type="submit">
              Submit
            </button>
          </form>
        </div>

        <div v-if="all_comments.length === 0" class="mb-4 flex items-center rounded-lg bg-white p-2 shadow">
          <p>No comments yet.</p>
        </div>

        <div v-for="com in all_comments" :key="com.id">
          <div class="flex items-center rounded-lg bg-white py-1 px-2 shadow">
            <div class="flex-grow">
              <div class="flex justify-between">
                <p class="text-sm text-gray-600">Author: {{ com.author }} </p>
                <p class="text-right text-sm text-gray-600">Published: {{ formatPubDate(com.pub_date) }}</p>
              </div>
              <p v-if="com.is_solution" class="mt-2 text-sm font-semibold text-green-500">Solution</p>
              <p class="text-lg">{{ com.content }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="flex justify-center px-2">
        <button
            class="ml-4 w-5/6 rounded border-gray-300 bg-blue-100 px-4 py-2 font-sans font-bold text-black hover:bg-blue-300"
            @click="showForm = !showForm">Answer this question
        </button>
      </div>
      <div v-if="showForm" class="flex justify-center p-2">
        <form @submit.prevent="addAnswer" class="w-5/6">
          <br>
          <div>
            <QuillEditor theme="snow" toolbar="full" name="content" v-model:content="answerInput" contentType="text">
            </QuillEditor>
          </div>
          <br>
          <button class="ml-4 rounded bg-blue-500 px-4 py-2 font-bold text-white hover:bg-blue-600" type="submit">
            Submit answer
          </button>
        </form>
      </div>
      <div class="p-5">
        <h1 class="mb-4 text-2xl font-bold">Answers:</h1>

        <div v-if="answers.length === 0" class="mb-4 flex items-center rounded-lg bg-white p-4 shadow">
          <p class="text-lg">No answers yet. Be the first to answer this question!</p>
        </div>

        <div v-for="answer in answers" :key="answer.id">
          <div class="mb-4 flex items-center rounded-lg bg-white p-4 shadow">
            <div class="flex flex-col items-center">
              <button class="mr-2 rounded bg-green-500 px-2 py-1 font-bold text-white hover:bg-green-600"
                      :class="{ 'border border-4 border-green-600': answer.upvote_or_downvote === 'upvote' }"
                      v-on:click="upvoteAnswer(answer.id)">
                <i class="fa fa-arrow-up"></i>
              </button>
              <span class="mr-2 text-lg font-bold text-gray-600">{{ answer.score }}</span>
              <button class="mr-2 rounded bg-red-500 px-2 py-1 font-bold text-white hover:bg-red-600"
                      :class="{ 'border border-4 border-red-600': answer.upvote_or_downvote === 'downvote' }"
                      v-on:click="downvoteAnswer(answer.id)">
                <i class="fa fa-arrow-down"></i>
              </button>
            </div>
            <div class="flex-grow">
              <div class="flex justify-between">
                <p class="text-sm text-gray-600">Author: {{ answer.author }} </p>
                <p class="text-right text-sm text-gray-600">Published: {{ formatPubDate(answer.pub_date) }}</p>
              </div>
              <p v-if="answer.is_solution" class="mt-2 text-sm font-semibold text-green-500">Solution</p>
              <p class="text-lg">{{ answer.content }}</p>
            </div>
          </div>
          <!-- <button  v-if=" answer.author != 'adinotadmin@mail.com' "   v-on:click="deleteQuestion" type="button"
                    class="mt-3 mr-2 mb-2 rounded-lg bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-blue-300">
              Delete Question
          </button> -->
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
      showComments: false,

      question: {
        title: "Loading...",
        explanation: "Loading...",
        tried_what: "Loading...",
        summary: "Loading...",
        pub_date: "2000-01-01T00:00:00Z",
        // Module: {
        //   title: ""
        // }

      },
      answers: [],
      answerInput: "",
      all_comments: [],
      commentInput: "",
      moduleTitle: "",
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
          this.all_comments = response.data.comment_list;
          //this.question.Module.title = response.data.Module.title;
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

    addComment() {
      console.log(this.commentInput)
      axiosClient.post(`/question/${this.$route.params.id}/submit_comment/`,
          {
            content: this.commentInput,
          })
          .then((response) => {
            this.all_comments.push(response.data);
            this.commentInput = "";
            this.showComments = false;
          })
          .catch((error) => {
            console.log(error);
          });
    },

    upvoteQuestion() {
      axiosClient.post(`/question/${this.$route.params.id}/upvote/`)
          .then((response) => {
            this.question.score = response.data.score;
            if (response.data.success) {
              this.question.upvote_or_downvote = "upvote";
            }
          })
          .catch((error) => {
            console.log(error);
          });
    },
    downvoteQuestion() {
      axiosClient.post(`/question/${this.$route.params.id}/downvote/`)
          .then((response) => {
            this.question.score = response.data.score;
            if (response.data.success) {
              this.question.upvote_or_downvote = "downvote";
            }
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
                if (response.data.success) {
                  answer.upvote_or_downvote = "upvote";
                }
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
                if (response.data.success) {
                  answer.upvote_or_downvote = "downvote";
                }
              }
              return answer;
            }).sort((a, b) => b.score - a.score);
          })
          .catch((error) => {
            console.log(error);
          });
      },

    deleteQuestion(){
      axiosClient.delete(`/question/${this.$route.params.id}/delete/`)
          .then((response) => {
            window.location.href = `/module/${response.data.module}`;
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
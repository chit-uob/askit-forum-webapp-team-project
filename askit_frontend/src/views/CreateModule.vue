<template>
  <div>
    <div class="mb-6">
      <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Module
        name</label>
      <input type="text" id="default-input" v-model="moduleTitle"
             class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
    </div>

    <label for="message" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Module description</label>
    <textarea id="message" rows="4" v-model="moduleExplanation"
              class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Description here..."></textarea>

    <button v-on:click="addModule" type="button"
            class="mt-3 mr-2 mb-2 rounded-lg bg-blue-700 px-5 text-sm font-medium text-white py-2.5 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300">
      Add module
    </button>
  </div>
  <!--  <div class="mb-6">-->
  <!--    <label for="large-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Large input</label>-->
  <!--    <input type="text" id="large-input" class="block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">-->
  <!--  </div>-->

  <!--  <div>-->
  <!--    <label for="small-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Small input</label>-->
  <!--    <input type="text" id="small-input" class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">-->
  <!--  </div>-->


</template>

<script>
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import axiosClient from "@/views/axiosClient";

export default {
  name: "createdModule",

  data() {
    return {
      // summaryLoadWheel: 'hidden',
      // tagLoadWheel: 'hidden',
      moduleTitle: '',
      moduleExplanation: '',
    }
  },
  methods: {
    addModule() {
      axiosClient.post(`/create_module/new/`, {
        title: this.moduleTitle,
        explanation: this.moduleExplanation,
      })
          .then((response) => {
            console.log(response);
            // redirect to question base on response.id
            window.location.href = '/module/' + response.data.title;
          })
          .catch((error) => {
            console.log(error);
          });
    }
  }
}

</script>

<style scoped>

</style>
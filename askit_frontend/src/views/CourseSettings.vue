<template>
  <main class="p-8 bg-[#D6FFD6] dark:bg-slate-800 overflow-visible">
    <h1 class="text-4xl font-bold">Course Settings for {{ $route.params.mod }}</h1>

    <div class="pt-4 mb-6">
      <label for="default-input" class="block mb-2 text-sm font-medium ">Course
        Name</label>
      <input type="text" id="default-input" v-model="moduleTitle" placeholder="Course name here..."
             class="shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff] bg-gray-50 text-gray-900 text-sm rounded-lg focus:ring-4 focus:outline-none transition focus:ring-blue-400 focus:border-blue-500 block w-full p-2.5 border-2 border-black dark:bg-gray-800 dark:text-white">
    </div>
    <label for="message" class="block mb-2 text-sm font-medium ">Course description</label>
    <textarea id="message" rows="16" v-model="moduleExplanation"
              class="shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff] block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg focus:ring-4 focus:outline-none transition focus:ring-blue-400 focus:border-blue-500 border-2 border-black dark:bg-gray-800 dark:text-white"
              placeholder="Description here..."></textarea>

    <button v-on:click="ManageMembers" type="button"
            class="shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff] dark:border-0 dark:bg-orange-500 transition mt-4 w-60 rounded bg-white px-4 text-sm font-semibold py-2 hover:bg-blue-500 focus:ring-4 focus:ring-pink-400 focus:outline-none border-2 border-black" >
      Manage Members
    </button>
    <div class="flex-row flex gap-x-20 mt-20">
      <button v-on:click="SaveChanges" type="button"
              class="shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff] dark:border-0 transition w-60 rounded bg-blue-600 px-4 text-sm font-semibold text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-pink-400 focus:outline-none border-2 border-black" >
        Save Changes
      </button>

      <button v-on:click="deleteModule" type="button" class=" shadow-[3px_3px_0px_0px_#000000] dark:shadow-[3px_3px_0px_0px_#ffffff] dark:border-0 transition w-60 rounded bg-red-600 px-4 text-sm font-semibold text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-pink-400 focus:outline-none border-2 border-black" >
        Delete Module
      </button>
    </div>
  </main>
</template>

<script>

import '@vueup/vue-quill/dist/vue-quill.snow.css'
import axiosClient from "@/views/axiosClient";

  export default {

    name: 'courseSettingsVue',

    data() {
      return {
        moduleTitle: '',
        moduleExplanation: '',
      }
    },
    methods: {
      deleteModule() {
        axiosClient({
          method: "delete",
          url: `/create_module/delete/${this.$route.params.mod}/`,
        })
            .then((response) => {
              console.log(response.data)
              window.location.href = '/';
            })
            .catch((error) => {
              console.log(error);
            });
      },
      ManageMembers() {
        window.location.href = `/module/${this.$route.params.mod}/add-members/`;
      },
        SaveChanges() {
          axiosClient({
            method: "post",
            url: `/course_settings/update/${this.$route.params.mod}/`,
            data: {
              title: this.moduleTitle,
              description: this.moduleExplanation,
            }
          })
              .then((response) => {
                window.location.href = `/module/${this.$route.params.mod}/`;
              })
              .catch((error) => {
                console.log(error);
              });
        },
    },
    mounted() {
      axiosClient({
        method: "get",
        url: `/course_settings/details/${this.$route.params.mod}/`,
      })
          .then((response) => {
            this.moduleTitle = response.data.title;
            this.moduleExplanation = response.data.description;
          })
          .catch((error) => {
            console.log(error);
          });
    },
}
</script>
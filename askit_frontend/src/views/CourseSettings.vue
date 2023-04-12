<template>
  <main class="p-8 bg-[#D6FFD6] overflow-visible">
    <h1 class="text-4xl font-bold">Course Settings for {{ $route.params.mod }}</h1>

    <div class="pt-4 mb-6">
      <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900">Course
        Name</label>
      <input type="text" id="default-input" v-model="moduleTitle"
             class="bg-gray-50 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 border-2 border-black" style="box-shadow: .2em .2em black;">
    </div>
    <label for="message" class="block mb-2 text-sm font-medium text-gray-900">Course description</label>
    <textarea id="message" rows="16" v-model="moduleExplanation"
              class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg focus:ring-blue-500 focus:border-blue-500 border-2 border-black" style="box-shadow: .2em .2em black;"
              placeholder="Description here..."></textarea>

    <button v-on:click="ManageMembers" type="button"
            class="mt-4 w-60 rounded bg-white px-4 text-sm font-medium text-black py-2 hover:bg-blue-500 focus:ring-4 focus:ring-blue-300 border-2 border-black" style="box-shadow: .2em .2em black;">
      Manage Members
    </button>
    <div class="flex-row flex gap-x-20 mt-20">
      <button v-on:click="SaveChanges" type="button"
              class="w-60 rounded bg-blue-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-blue-300 border-2 border-black" style="box-shadow: .2em .2em black;">
        Save Changes
      </button>

      <button v-on:click="deleteModule" type="button" class="w-60 rounded bg-red-600 px-4 text-sm font-medium text-white py-2 hover:bg-blue-500 focus:ring-4 focus:ring-blue-300 border-2 border-black" style="box-shadow: .2em .2em black;">
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
    }
}
</script>
<script setup>
// import { Ref } from 'vue';
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'

</script>

<template>

  
<label for="message" class="block mb-2 text-lg font-medium text-gray-900 dark:text-black">Title</label>
<textarea id="message" rows="1" class="block p-2.5 w-1/2 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Enter your title"></textarea>

  <label for="large-input" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">Explain your problem</label>
<div class="w-1/2">
  <QuillEditor theme="snow" toolbar="full">
  </QuillEditor>
</div>
  <label for="large-input" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">What have you already tried?</label>

  

<QuillEditor theme="snow" toolbar="full">
</QuillEditor>
<!--summary-->
  <div class="mb-6">
  <label for="large-input" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">Summary (optional)</label>
  <input type="text" id="large-input" class="block w-1/2 p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
</div>
<button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Auto-generate summary</button>

<!--tags-->
<div class="mb-6">
  <label for="large-input" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">Tags</label>
  <input type="text" id="large-input" class="block w-1/2 p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
</div>


<button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Auto-generate tags</button>

<button type="button" class="text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">Submit</button>
</template>

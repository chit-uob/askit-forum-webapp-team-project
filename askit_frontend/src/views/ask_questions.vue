<script setup>
// import { Ref } from 'vue';
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'

</script>

<template>

<div class="absolute left-2/3 ml-7 mt-0.5 w-0.5 h-screen bg-gray-600"></div>


<div>
<label for="message" class="block mb-2 text-lg font-medium text-gray-900 dark:text-black">Title</label>
<textarea id="message" rows="1" class="block p-2.5 w-2/3 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Enter your title"></textarea>
</div>


<label for="large-input" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">Explain your problem</label>
<div class="w-2/3">
  <QuillEditor id ="large-input" theme="snow" toolbar="full">
  </QuillEditor>
</div>


<label for="large-input" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">What have you already tried?</label>
<div class="w-2/3">
<QuillEditor id ="large-input" theme="snow" toolbar="full">
</QuillEditor>
</div>

<!--summary-->
<div class>
<label for="message" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">Summary (optional)</label>
<textarea id="message" rows="1" class="block p-2.5 w-2/3 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Type or auto-generate summary"></textarea>
<button type="button" class=" mt-3 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Auto-generate summary</button>
</div>




<!--tags-->
<div class="mb-6">
<label for="message" class="block mb-2 text-lg font-medium text-green-700 dark:text-black">Tags</label>
<textarea id="message" rows="1" class="block p-2.5 w-2/3 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Type or auto-generate tags"></textarea>
<button type="button" class="mt-3 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Auto-generate tags</button>
</div>


</template>

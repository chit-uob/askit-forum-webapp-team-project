<template>


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
.crypto_bg {
  background: #fffaf0;
}

</style>
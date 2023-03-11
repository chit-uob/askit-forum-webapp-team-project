<template>
    <div>
      <div>
        <h1>{{ $route.params.mod.toUpperCase() }}</h1>
        <button>Ask Question</button>
      </div>
      <div>
        <h2>Most recent questions</h2>
          <div v-for="question in questions" :key="question.id">
            <p>{{ question.title }}</p>
            <p>Asked by {{ question.author }}</p>
            <p>{{ question.tags }}</p>
          </div>
      </div>
    </div>


  </template>

<script>
import axiosClient from "@/views/axiosClient";

export default {
  name: "ModuleView",
  data() {
    return {
      
      questions: [
        { id: 1, title: 'Learn HTML?', author: 'Aymon', tags: ['HTML', 'help'] },
        { id: 2, title: 'Learn JavaScript?', author: 'Aliyu', tags: ['JS', 'help'] },
        { id: 3, title: 'Learn Vue?', author: 'Adi', tags: ['Vue', 'help'] }
      ]
    };
  },
  mounted() {
    axiosClient({
      method: "get",
      url: `/module/${this.$route.params.mod}/`,
    })
        .then((response) => {
          this.questions = response.data;
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error);
        });
  },
  methods: {
    
  }
};
</script>
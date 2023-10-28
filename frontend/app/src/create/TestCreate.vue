<script>
import { RouterLink, RouterView } from "vue-router";

export default {
  data() {
    return {
      questions: [],
      question: '',
      ans1: '',
      ans2: '',
      ans3: '',
      correct: '',
      counter: 0,
    };
  },
  methods: {
    add_question() {
        this.questions.push({question: this.question, ans1: this.ans1, ans2: this.ans2, ans3: this.ans3, correct: this.correct})
    },

    create_test() {

    }
  },
};
</script>

<template>
  <div class="wrapper">
    <input type="text" v-model="question" placeholder="вопрос" />
    <input type="text" v-model="ans1" placeholder="ответ 1" />
    <input type="text" v-model="ans2" placeholder="ответ 2" />
    <input type="text" v-model="ans3" placeholder="ответ 3" />
    <input type="num" v-model="correct" placeholder="номер правильного ответа">
    <button @click="add_question">Создать вопрос</button>
  </div>
  <button @click="create_test">Завершить создание теста</button>
</template>

<style scoped>
</style>

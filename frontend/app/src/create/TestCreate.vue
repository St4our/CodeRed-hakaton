<script>
import { RouterLink, RouterView } from 'vue-router';

export default {
  data() {
    return {
      test: [],
      questions: [],
      question: '',
      ans1: '',
      ans2: '',
      ans3: '',
      name: ``,
      correct: '',
      counter: 1,
      message: ''
    };
  },
  methods: {
    add_question() {
      this.questions.push({
        question: this.question,
        ans1: this.ans1,
        ans2: this.ans2,
        ans3: this.ans3,
        correct: this.correct,
      });
      this.question = '';
      this.ans1 = '';
      this.ans2 = '';
      this.ans3 = '';
      this.correct = '';
      this.counter += 1;
    },

    create_test() {
      this.test.push({
        name: this.name,
        question: this.questions,
      });
      this.name = ''
      this.message = "Создано"
      this.$router.go(-1)
    },
  },
};
</script>

<template>
  <div class="container">
    <input
      class="name-test"
      placeholder="Название теста"
      v-model="name"
      type="text"
    />
    <div class="overflow">
      <div class="group">
        <div
          class="wrapper-test"
          :class="{ next: nexttarget == 1, back: backtarget == 1 }"
        >
          <div class="question">
            <span>{{ counter }}</span>
            <input type="text" v-model="question" placeholder="Вопрос" />
          </div>
          <div class="test-body">
            <input type="text" v-model="ans1" :placeholder="'Ответ1'" />

            <input type="text" v-model="ans2" :placeholder="'Ответ2'" />

            <input type="text" v-model="ans3" :placeholder="'Ответ3'" />

            <input
              type="number"
              v-model="correct"
              :placeholder="'Номер правильного ответа'"
            />
          </div>
          <div class="wrapper-button">
            <button type="button" @click="add_question" class="answer">
              Создать
            </button>
            <button type="button" @click="create_test" class="answer">
              Завершить создание теста
            </button>
          </div>
        </div>
      </div>
      <span class="success" v-if="message">{{ message }}</span>
    </div>
  </div>
</template>

<style scoped>
button{
  background: transparent;
  color: #fff;
}
.success{
  position: absolute;
  bottom: 10%;
  color: #3f7512 !important;
}
input{
  border-radius: 10px;
  padding: 5px;
  background: transparent;
}
input::placeholder{
  color: #fff;
}
.question span {
  margin-right: 10px;
  font-size: 18px;
}
.name-test {
  position: absolute;
  top: 10%;
  text-align: center;
}
.test-body input:last-child {
  margin: 0 auto;
}
input:not(.question input) {
  width: 50%;
}
input:last-child {
  text-align: center;
}
.wrapper {
  width: 100%;
  height: 100%;
}
.wrapper-button {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
}
.group {
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 100%;
  height: 100%;
}
.overflow {
  width: 50%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 50px;
  overflow-x: scroll;
}
.overflow::-webkit-scrollbar {
  display: none;
}
.next {
  animation: next 800ms linear forwards;
}
.back {
  animation: back 800ms linear forwards;
}
.answer {
  border: none;
}
.form-check-input:checked {
  background-color: #751221;
  border-color: #ff072c;
}
.form-check-input:focus {
  border-color: #fe8686;
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgba(253, 13, 13, 0.25);
}
.test-body input,
label {
  cursor: pointer;
}

label {
  color: #fff;
}
span {
  color: #fff !important;
}
.test-body {
  height: 80%;
  padding: 10px;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  gap: 20px;
  border-top: 1px solid #ff072c;
  border-bottom: 1px solid #ff072c;
}
.wrapper-test {
  min-width: 100%;
  height: 60%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  border-radius: 16px;
}

h1 {
  position: absolute;
  top: 10%;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
@keyframes next {
  0% {
    transform: translateX(0);
    opacity: 1;
  }
  30% {
    transform: translateX(500px);
    opacity: 0;
  }
  90% {
    transform: translateX(0);
  }
  100% {
    opacity: 1;
  }
}
@keyframes back {
  0% {
    transform: translateX(0);
    opacity: 1;
  }
  30% {
    transform: translateX(-500px);
    opacity: 0;
  }
  90% {
    transform: translateX(0);
  }
  100% {
    opacity: 1;
  }
}
</style>

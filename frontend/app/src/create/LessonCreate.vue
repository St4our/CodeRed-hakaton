<script>
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';

export default {
  data() {
    return {
        name: '',
        src: '',
        description: ''
    };
  },
  methods: {},
};
</script>

<template>
  <div class="container">
    <input class="name" v-model="name" placeholder="Название урока" type="text" />
    <div class="wrapper-lesson">
      <input type="text" v-model="src" placeholder="src видео" />
      <textarea
        name=""
        id="" v-model="description"
        cols="30"
        rows="5"
        placeholder="Описание"
      ></textarea>
      <button @click="create">Создать</button>
    </div>
  </div>
</template>

<style scoped>
.name {
  position: absolute;
  top: 10%;
}
input {
  background: transparent;
  text-align: center;
  color: #fff;
}
textarea {
  background: transparent;
  text-align: center;
  color: #fff;
}
input::placeholder {
  color: #fff;
}
textarea::placeholder {
  color: #fff;
}
button {
  background: transparent;
  border: none;
  color: #fff;
}
iframe {
  border: 1px solid #a71d31;
}
.wrapper-lesson {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 20px;
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
</style>

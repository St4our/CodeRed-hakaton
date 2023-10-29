<script>
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';

export default {
  data() {
    return {};
  },
  methods: {},
};
</script>

<template>
  <div class="container">
    <h1>Урок</h1>
    <div class="wrapper-lesson">
      <iframe
        src="https://www.youtube.com/embed/xhFt8a4H098?si=NTue5cb6dJeXehX6"
        frameborder="0"
        width="1000px"
        height="500px"
      ></iframe>
    </div>
  </div>
</template>

<style scoped>
iframe{
  border: 1px solid #a71d31 ;
}
.wrapper-lesson {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
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

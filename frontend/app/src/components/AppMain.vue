<script>
import { RouterLink, RouterView } from "vue-router";
import axios from "axios";

export default {
  components: {},
  data() {
    return {};
  },
  methods: {
  },
  mounted() {
  },
};
</script>

<template>
  <div class="wrapper">
    <div class="nav">
      <div class="item active">О нас</div>
      <div class="item">Тарифы</div>
      <div class="item">Отзывы</div>
    </div>
    <div class="content">
      <div class="text">
        <h1>
          <span><i>The</i></span>
          <span><i>best</i></span>
          <span><i>products</i></span>
          <span><i>start</i></span>
          <span><i>with</i></span>
          <span><i>Sketch</i></span>
        </h1>
        <p>
          Create, prototype, collaborate, and bring your ideas to life with the
          design platform used by over one million people — from freelancers, to
          the world’s largest teams.
        </p>
      </div>
    </div>
  </div>
</template>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Inter&family=Poppins:wght@400;500&display=swap");

*,
*:before,
*:after {
  padding: 0;
  margin: 0;
  font-family: "Poppins", sans-serif;
}

:root {
  font-size: 32px;
}

body {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  min-height: 100vh;
  font-family: Helvetica;
}

.text {
  width: 40%;
}
.nav {
  top: 5%;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 50px;
}

.content {
    padding: 0px 50px;
}

.item {
  font-size: large;
}

.item.active {
  color: #950707;
}

.wrapper {
  width: 100%;
  height: 90vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
h1 {
  margin: 0;
  letter-spacing: -2px;
}

p {
  font-size: 0.9rem;
  color: #666;
  line-height: 1.3rem;
  position: relative;
  top: 0.8rem;
  opacity: 0;
  animation: 0.5s swift-up ease-out forwards, 0.5s fade-in ease-out forwards;
  animation-delay: 0.8s;
}

@keyframes fade-in {
  to {
    opacity: 1;
  }
}

span {
  display: inline-block;
  overflow: hidden;
  position: relative;
  top: 0.8rem;
  animation: 0.3s swift-up ease-in-out forwards;
}

i {
  font-style: normal;
  position: relative;
  top: 2rem;
  animation: 0.5s swift-up ease-in-out forwards;
}

@keyframes swift-up {
  to {
    top: 0rem;
  }
}

span:nth-of-type(1) i {
  animation-delay: 0s;
}

span:nth-of-type(2) i {
  animation-delay: 0.1s;
}

span:nth-of-type(3) i {
  animation-delay: 0.2s;
}

span:nth-of-type(4) i {
  animation-delay: 0.3s;
}

span:nth-of-type(5) i {
  animation-delay: 0.4s;
}

span:nth-of-type(6) i {
  animation-delay: 0.5s;
}

span:nth-of-type(1) {
  animation-delay: 0s;
}

span:nth-of-type(2) {
  animation-delay: 0.1s;
}

span:nth-of-type(3) {
  animation-delay: 0.2s;
}

span:nth-of-type(4) {
  animation-delay: 0.3s;
}

span:nth-of-type(5) {
  animation-delay: 0.4s;
}

span:nth-of-type(6) {
  animation-delay: 0.5s;
}
</style>

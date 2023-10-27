<script>
import { RouterLink, RouterView } from "vue-router";
import AppBackground from "./components/AppBackground.vue";
import AppRegister from "./components/AppRegister.vue";
import AppLogin from "./components/AppLogin.vue";

export default {
  components: {
    AppBackground,
    AppRegister,
    AppLogin,
  },
  data() {
    return {};
  },
  mounted() {},
  methods: {},
};
</script>

<template>
  <div class="container1">
    <RouterLink to="/" class="author">
      <span class="one">by</span> <span class="two">CodeRed</span> Team
    </RouterLink>
    <div class="img">
      <img src="./assets/codered.png" class="codered" alt="codered-png" />
    </div>
    <app-background class="bg"></app-background>
    <router-view class="register"></router-view>
  </div>
</template>

<style scoped>
.bg {
  height: 100vh;
}

.container1 {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.register,
.login {
  position: absolute;
}

.author {
  padding-right: 20px;
  padding-bottom: 20px;
  position: absolute;
  bottom: 0;
  right: 0;
}

.author {
  font-size: medium;
}

.author > .one {
  font-size: small;
}

.author > .two {
  color: #a71d31;
}

.img {
  position: absolute;
  top: 0;
  left: 0;
  padding-left: 35px;
  padding-top: 20px;
}
.codered {
  height: 110px;
  width: auto;
}

a {
  text-decoration: none;
  color: white;
}

@media (max-width: 600px) {
  .codered {
    height: 75px;
    width: auto;
  }

  .img {
    position: absolute;
    top: 0;
    left: 0;
    padding-left: 10px;
    padding-top: 10px;
  }
}
</style>

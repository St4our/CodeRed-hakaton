<script>
import { RouterLink, RouterView } from 'vue-router';
import AppBackground from './components/AppBackground.vue';
import AppRegister from './components/AppRegister.vue';
import AppLogin from './components/AppLogin.vue';

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
  <div class="container1" v-if="$route.path != '/'">
    <div class="author">
      <span class="one">by</span> <span class="two">CodeRed</span>
    </div>
    <div class="img">
      <RouterLink to="/menu">
        <img src="./assets/logo.png" class="codered" alt="logo.png" />
        <p class="text-codered">CodeRed</p>
      </RouterLink>
      <RouterLink to="/menu/profile">
        <img src="./assets/profile.png" class="profile" alt="profile.png" />
      </RouterLink>
    </div>
    <app-background class="bg"></app-background>
    <router-view class="register" v-if="$route.path != '/'"></router-view>
  </div>


  <div class="container1" v-if="$route.path == '/'">
    <router-view v-if="$route.path == '/'"></router-view>
  </div>
</template>

<style scoped>
.sub {
  color: #9c9e9e !important;
}
.main-color {
  color: #a71d31 !important;
}
.text-codered {
  margin: 0 0 0 10px;
  font-size: 16px;
  font-weight: 700;
  text-transform: uppercase;
}
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
  width: 100%;
  position: absolute;
  display: flex;
  justify-content: space-between;
  align-items: center;
  top: 0;
  left: 0;
  padding-left: 35px;
  padding-top: 20px;
  padding-right: 35px;
  z-index: 2;
}
.codered {
  height: 50px;
  width: auto;
  cursor: pointer;
  z-index: 2;
  position: relative;
}

.profile {
  height: 65px;
  width: auto;
}

a {
  text-decoration: none;
  color: white;
}

.img a {
  display: flex;
  justify-content: center;
  align-items: center;
}

@media (max-width: 600px) {
  .profile {
    height: 50px;
  }

  .img {
    position: absolute;
    top: 0;
    left: 0;
    padding-left: 10px;
    padding-top: 10px;
    padding-right: 10px;
  }
}
</style>

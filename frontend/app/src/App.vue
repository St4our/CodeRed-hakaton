<script>
import { RouterLink, RouterView } from 'vue-router'
import AppBackground from './components/AppBackground.vue'
import AppRegister from './components/AppRegister.vue'
import AppLogin from './components/AppLogin.vue'

export default {
  components: {
   AppBackground,
   AppRegister,
   AppLogin
  },
  data() {
    return {
      
    };
  },
  mounted() {

  },
  methods: {
    
  },
};
</script>

<template>
  <div class="container">
    <app-background class="bg"></app-background>
    <router-view class="register"></router-view>
  </div>
</template>

<style scoped>
.bg {
  
}

.container {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.register, .login {
  position: absolute;
}
</style>

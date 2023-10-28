<script>
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';
export default {
  components: {},
  data() {
    return {
      login: ``,
      password: ``,
      token: ``,
      error: ``,
      status: ``,
    };
  },
  methods: {
    async submit() {
      let error = await axios.post(`/login`, {
        email: this.email,
        password: this.password,
      });
      this.error = error.data.message;
      this.status = error.data.status;
      this.token = error.data.token;
      if (this.token) {
        document.cookie = new String();
        document.cookie = `token=${this.token}; max-age=1123200`;
      }
      setTimeout(() => {
        if (this.status == '200') {
          this.$refs.form.reset();
          this.$router.push({ name: 'home' });
        }
      }, 1000);
      setTimeout(() => {
        (this.error = ``), (this.status = ``);
        if (error) {
          (this.email = ``), (this.password = ``);
        }
      }, 3000);
    },
    exit(){
      console.log(document.cookie)
    }
  },
  mounted() {
    this.exit()
  },
};
</script>

<template>
  <div class="container">
      <div class="image">
          <div class="form-box">
            <h2 class="title">Вход</h2>
              <div class="form">
                  <form ref="form" @submit.prevent="submit">
                      <div class="input-box">
                          <input v-model="login" type="text" class="login" required>
                          <label for="">Логин</label>
                      </div>
                      <div class="input-box">
                          <input v-model="password" type="password" class="password" required>
                          <label for="">Пароль</label>
                      </div>
                      <div class="sign-up">
                          <button type="submit" class="sign-in">Войти</button>
                      </div>
                  </form>
              </div>
          </div>
      </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter&family=Poppins:wght@400;500&display=swap');

*,
*:before,
*:after {
    padding: 0;
    margin: 0;
    font-family: 'Poppins', sans-serif;
    color: #fff;
}

body {
    display: flex;
    /* background: #0c1022; */
    background: #F9F9F9;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    overflow: hidden;
}

.container {
    position: relative;
    width: 350px;
    height: 650px;
    background: rgba(0, 0, 0.75);
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding-inline: 32px;
    overflow: hidden;
}

.container::before {
    content: "";
    z-index: 0;
    position: absolute;
    height: 770px;
    width: 770px;
    background: conic-gradient(
        transparent, transparent, transparent, #d400d4
        /* transparent, transparent, transparent, #FF1D15 */
    );
    animation: animate 4s linear infinite;
    animation-delay: -2s;
}
.container::after {
    content: "";
    z-index: 0;
    position: absolute;
    height: 770px;
    width: 770px;
    background: conic-gradient(
        transparent, transparent, transparent, #FF1D15
    );
    /* #00cfff  F18904*/
    animation: animate 4s linear infinite;
}

@keyframes animate {
    0% {
        transform: rotate(0);
    }
    0% {
        transform: rotate(360deg);
    }
}

.image {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    inset: 5px;
    /* background-color: #0c1022; */
    background-color: #0f0f0f;
    z-index: 1;
    border-radius: 16px;
}

.form-box {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    min-height: 60vh;
    gap: 30px;
}



.form-box-2 {
    
    min-height: 60vh;
}

.form-box-2 .form h2 {
    font-size: 32px;
    color: black;
    text-align: center;
}



.form-box .form h2 {
    font-size: 32px;
    /* color: #fff; */
    text-align: center;
}

.form .input-box {
    position: relative;
    margin: 37px 0;
    width: 310px;
    border-bottom: 2px solid black;
}

.input-box input {
    width: 100%;
    height: 50px;
    background: transparent;
    border: none;
    outline: none;
    font-size: 16px;
    padding: 0 35px 0 5px;
    /* color: #fff; */
}
input:focus ~ label,
input:valid ~ label {
    top: -5px;
}

.input-box label {
    position: absolute;
    /* color: #fff; */
    top: 50%;
    left: 5px;
    transform: translateY(-50%);
    font-size: 16px;
    pointer-events: none;
    transition: .3s;
}

.d-none {
    display: none;
}

.group {
    width: 100%;
    display: flex;
    justify-content: space-between;
    font-size: 13px;
}

.node {
    position: relative;
    top: -15px;
    color: #FF8200;
    background-color: transparent;
    text-decoration: none;
    border: none;
    font-weight: 500;
    font-size: 16px;
    cursor: pointer;
}

.sign-in {
    padding: 7px 9px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    outline: none;
    border: none;
    border-radius: 5px;
    background-color: #A71D31;
    /* #FF8200 */
}

.sign-up-btn {
    padding: 12px 15px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    outline: none;
    border: none;
    border-radius: 5px;
    background-color: #FF8200;
}

.sign-up-btn:focus {
    /* color: #fff; */
    background-color: #0c1022;
    border: 2px solid #fff;
}

.sign-up {
    display: flex;
    justify-content: center;
    width: 100%;
    margin: 15px 0;
}

.disabled {
    pointer-events: none;
    opacity: 0.4;
}

.form {
    display: grid;
}

.a-back {
    text-decoration: none;
    color: #FF8200;
    text-align: center;
}                                                                                                                                         

.invalid {
    text-align: center;
    border: 2px solid red;
    color: red;
    padding: 10px;
    border-radius: 10px;
}

.title {
  font-size: 30px;
}


.author {
    position: absolute;
    bottom: 0;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
    margin-bottom: 10px;
}

.text {
    font-size: small;
}

.text>.one {
    font-size: smaller;
}

.text>.two {
    color: #A71D31;
}
.codered {
    height: 75px;
    width: auto;
}
</style>

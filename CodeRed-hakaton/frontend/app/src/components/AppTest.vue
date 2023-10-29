<script>
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';

export default {
  data() {
    return {
      nexttarget: 0,
      backtarget: 0,
      testindex: 0,
      info: [],
    };
  },
  methods: {
    next() {
      this.nexttarget = 1;
      this.testindex -= 100;
      let group = document.querySelector(`.group`);
      group.style.transform = `translateX(${this.testindex}%)`;
      setTimeout(() => (this.nexttarget = 0), 1000);
    },
    back() {
      this.backtarget = 1;
      this.testindex += 100;
      let group = document.querySelector(`.group`);
      group.style.transform = `translateX(${this.testindex}%)`;
      setTimeout(() => (this.backtarget = 0), 1000);
    },
    start() {
      this.testindex = 100 * Math.floor(this.info.length / 2);
      let group = document.querySelector(`.group`);
      group.style.transform = `translateX(${this.testindex}%)`;
    },
    async testload() {
      let response = await axios.get(`/tests`, {
        params: {
          test_id: this.$route.query.id,
        },
        headers: {
          Authorization: document.cookie.replace(`token=`, ``),
        },
      });

      this.info = response.data.tests[0];
    },
  },
  mounted() {
    this.testload();
    this.start();
  },
};
</script>

<template>
  <div class="container">
    <h1>{{ info.name }}</h1>
    <div class="overflow">
      <div class="group">
        <div
          v-for="(item, index) in info.questions"
          class="wrapper-test"
          :class="{ next: nexttarget == 1, back: backtarget == 1 }"
        >
          <div class="question">
            <span>{{ item.name }}</span>
          </div>
          <div class="test-body">
            <div class="form-check">
              <input
                class="form-check-input"
                type="radio"
                name="flexRadioDefault"
                :id="'flexRadioDefault' + index + 1"
              />
              <label
                class="form-check-label"
                :for="'flexRadioDefault' + index + 1"
              >
                {{ item.answer_1 }}
              </label>
            </div>
            <div class="form-check">
              <input
                class="form-check-input"
                type="radio"
                name="flexRadioDefault"
                :id="'flexRadioDefault' + index + 2"
              />
              <label
                class="form-check-label"
                :for="'flexRadioDefault' + index + 2"
              >
                {{ item.answer_2 }}
              </label>
            </div>
            <div class="form-check">
              <input
                class="form-check-input"
                type="radio"
                name="flexRadioDefault"
                :id="'flexRadioDefault' + index + 3"
              />
              <label
                class="form-check-label"
                :for="'flexRadioDefault' + index + 3"
              >
                {{ item.answer_3 }}
              </label>
            </div>
          </div>
          <div class="wrapper-button">
            <button v-if="index > 0" @click="back" class="answer">Назад</button>
            <button @click="next" class="answer">Ответить</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
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

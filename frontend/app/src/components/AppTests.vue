<script>
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';

export default {
  components: {},
  data() {
    return {
      Tests: [],
    };
  },
  methods: {
    async testsLoad() {
      let response = await axios.get(`/tests`, {
        headers: {
          Authorization: document.cookie.replace(`token=`, ``),
        },
      });
      this.Tests = response.data.tests;
    },
  },
  mounted() {
    this.testsLoad();
  },
};
</script>
<template>
  <div class="wrapper">
    <h1>Тесты</h1>
    <div class="wrapper-for-tests">
      <RouterLink
        v-for="(item, index) in Tests"
        :to="'/menu/tests/test?id=' + item.test_id"
      >
        <div class="test">
          <h4 class="title">{{ item.name }}</h4>
          <div class="points">?/{{ item.questions.length }}</div>
        </div>
      </RouterLink>
    </div>
    <div class="create">
      <RouterLink class="btn btn-outline-success" to="/menu/test/create"
        >Создать</RouterLink
      >
    </div>
  </div>
</template>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter&family=Poppins:wght@400;500&display=swap');
a {
  color: #9c9e9e;
}
*,
*:before,
*:after {
  padding: 0;
  margin: 0;
  font-family: 'Poppins', sans-serif;
}

::-webkit-scrollbar {
  width: 0;
}

a {
  text-decoration: none;
}

tbody a {
  color: #fff;
}

.wrapper {
  width: 100%;
  padding: 0 50px;
  height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: end;
}

.btn-outline-danger,
.btn-outline-success,
.btn-outline-light {
  padding: 5px 7px;
}

.create {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.wrapper-for-tests {
  height: 70%;
  width: 100%;
  border: 1px solid #fff;
  border-radius: 20px;
  padding: 20px 45px;
  display: flex;
  flex-direction: column;
  gap: 30px;
  margin-bottom: 20px;
  overflow-x: hidden;
  overflow-y: scroll;
}

.test {
  width: 100%;
  height: 75px;
  border: 1px solid #fff;
  border-radius: 50px;
  background-color: #06070e;
  padding: 7px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);

  transition: background-color 500ms;
}
h1 {
  position: absolute;
  top: 10%;
}

.test:hover {
  background-color: #c8c8c8;
  color: #0e0c07;
}

.points {
  font-size: 25px;
}

@media (max-width: 550px) {
  .scroll-table-body {
    height: 300px;
  }

  .wrapper {
    padding: 0 10px;
  }

  .btn-outline-danger,
  .btn-outline-success,
  .btn-outline-light {
    padding: 2px 4px;
    font-size: small;
  }
}
</style>

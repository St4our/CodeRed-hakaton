<script>
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';

export default {
  components: {},
  data() {
    return {};
  },
  methods: {},
  mounted() {},
};
</script>

<template>
  <div class="wrapper">
    <h1>Категории пользователей</h1>
    <div class="scroll-table table table-dark table-hover mb-3">
      <table class="table table-dark table-hover glass">
        <thead>
          <tr>
            <th scope="col"></th>
            <th scope="col">Название</th>
            <th scope="col">Удаление</th>
            <th scope="col">Переход</th>
          </tr>
        </thead>
        <tbody class="scroll-table-body">
          <tr v-for="(item, index) in 8">
            <th scope="row">{{index}}</th>
            <td>Mark</td>
            <td>
              <button type="button" class="btn btn-outline-danger">
                Удалить
              </button>
            </td>
            <td>
              <RouterLink to="#" class="btn btn-outline-light transition"
                >Перейти</RouterLink
              >
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="create">
      <RouterLink class="btn btn-outline-success" to="#">Создать</RouterLink>
    </div>
  </div>
</template>
<style scoped>
thead {
  background: #32353956;
}
.table-dark {
  --bs-table-bg: transparent !important ;
}
.glass {
  background: rgb(93 93 93 / 6%) !important;
  border-radius: 16px !important;
  box-shadow: 0 4px 30px rgb(0 0 0 / 10%) !important;
  backdrop-filter: blur(5px) !important;
  -webkit-backdrop-filter: blur(5px) !important;
  border: 1px solid rgba(9, 9, 9, 0.3) !important;
}
@import url('https://fonts.googleapis.com/css2?family=Inter&family=Poppins:wght@400;500&display=swap');

*,
*:before,
*:after {
  padding: 0;
  margin: 0;
  font-family: 'Poppins', sans-serif;
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
  justify-content: flex-end;
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

h1 {
  position: absolute;
  top: 10%;
}

.scroll-table-body {
  max-height: 460px;
  overflow-y: scroll;
  margin-top: 0px;
  margin-bottom: 20px;
  border-top: none;
  background: #32353956;
}
.scroll-table table {
  width: 100%;
  table-layout: fixed;
}
.scroll-table thead th {
  font-weight: bold;
  text-align: left;
  border: none;
  padding: 10px 15px;
  background: transparent;
  font-size: 14px;
}
.scroll-table tbody td {
  text-align: left;
  padding: 10px 15px;
  font-size: 14px;
  vertical-align: top;
}

/* Стили для скролла */
::-webkit-scrollbar {
  width: 6px;
}
::-webkit-scrollbar-track {
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}
::-webkit-scrollbar-thumb {
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}

.list-item {
  border: 1px solid #fff;
  transition: background-color 300ms;
}

.list-item:hover {
  background-color: #2d2d34;
  /* #06070e */
}

.list-nav {
  border: 1px solid #fff;
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

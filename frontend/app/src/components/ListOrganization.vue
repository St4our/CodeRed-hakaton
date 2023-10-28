<script>
import { RouterLink, RouterView } from "vue-router";
import axios from "axios";

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
    <h1>Список организаций</h1>
    <div class="scroll-table">
      <table>
        <thead>
          <tr class="list-nav">
            <th>Индекс</th>
            <th>Название</th>
            <th>Удаление</th>
            <th>Переход</th>
          </tr>
        </thead>
      </table>
      <div class="scroll-table-body">
        <table>
          <tbody>
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
            <tr class="list-item">
              <td>index</td>
              <td>Codered</td>
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
    </div>
    <div class="create">
      <RouterLink class="btn btn-outline-success" to="#">Создать</RouterLink>
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
  justify-content: center;
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
  height: 500px;
  overflow-x: auto;
  margin-top: 0px;
  margin-bottom: 20px;
  border: 1px solid #fff;
  border-top: none;
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
  background-color: #06070e;
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

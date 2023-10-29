<script>
import { RouterLink, RouterView } from "vue-router";
import axios from "axios";
export default {
  components: {},
  data() {
    return {
        categories: ['Монтажник', 'Сварщик', 'Токарь', 'Фрезеровщик', 'Слесарь', 'Электрик', 'Сверловщик', 'Распиловщик', 'Комплектовщик', 'Оператор станка с ЧПУ', 'Качественный контролер',
        'Грузчик', 'Маляр', 'Шлифовщик', 'Трубопроводчик']
    };
  },
  methods: {
    async request() {
      try {
        const response = await axios.get(
          `/categories`,
          {
            headers: {
              Authorization: `YmF4OkJheHRpeW9yb3YyMTE3`,
            },
          }
        );
        this.categories = response.data.categories;
        console.log(this.categories);
      } catch (error) {
        console.error(error);
      }
    },
  },
  mounted() {
    this.request();
  },
};
</script>

<template>
  <div class="wrapper">
    <h1>Категории пользователей</h1>
    <div class="scroll-table glass">
      <table class="table table-dark">
        <thead>
          <tr class="">
            <th>ID категории</th>
            <th>Категория</th>
            <th>Переход</th>
          </tr>
        </thead>
      </table>
      <div class="scroll-table-body glass">
        <table>
          <tbody class="scroll-table-body glass" >
            <tr v-for="item in this.categories" class="list-item">
              <td>{{ item.category_id }}</td>
              <td>{{item.name}}</td>
              <td>
                <RouterLink :to="'/adminmenu/list/users/category/users?category_id='+String(item.category_id)" class="btn btn-outline-light transition"
                  >Перейти</RouterLink
                >
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="create">
      <RouterLink class="btn btn-outline-success" to="/adminmenu/list/users/category/create">Создать</RouterLink>
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
.glass {
    border-radius: 16px !important;
    box-shadow: 0 4px 30px rgb(0 0 0 / 10%) !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(5px) !important;
    border: 1px solid rgba(9, 9, 9, 0.3) !important;
  }


.wrapper {
  width: 100%;
  padding: 0 50px;
  height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 35px;
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
.scroll-table-body {
  max-height: 400px;
  overflow-x: auto;
  margin-top: 0px;
  margin-bottom: 20px;

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
  
  transition: background-color 500ms;
}

.list-item:hover, .list-item:active {
    background-color: #35393C;
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
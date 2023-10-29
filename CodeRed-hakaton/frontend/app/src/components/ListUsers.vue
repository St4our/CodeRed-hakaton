<script>
import { RouterLink, RouterView } from "vue-router";
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      users: [],
      users_sort: [],
      category_id: '',
      success: ''
    };
  },
  methods: {
    async request() {
      try {
        const response = await axios.get(
          `/users`,
          {
            headers: {
              Authorization: `YmF4OkJheHRpeW9yb3YyMTE3`,
            },
          }
        );
        this.users = response.data;
        for (let i = 0; i < this.users.users.length; i++) {
          let user = this.users.users[i]
          console.log(user)
          if (user.category_id == this.category_id) {
            this.users_sort.push(user)
          }
        }
      } catch (error) {
        console.error(error);
      }
    },

    get_id(){
      this.category_id = this.$route.query.category_id
    },

    async delete_ID() {
      try {
        const response = await axios.delete(
          `/users`,
          {
            params: {
              user_id: 2
            },
            headers: {
              Authorization: `YmF4OkJheHRpeW9yb3YyMTE3`,
            },
          }
        );
        this.success = response.data.success;
        console.log(this.success)
      } catch (error) {
        console.error(error);
      }
    }
  },
  mounted() {
    this.get_id()
    this.request();
  },
};
</script>

<template>
  <div class="wrapper">
    <h1>Список Пользователей</h1>
    <div class="scroll-table glass">
      <table class="table table-dark">
        <thead>
          <tr class="">
            <th>ID пользователя</th>
            <th>Никнейм</th>
            <th>Почта</th>
          </tr>
        </thead>
      </table>
      <div class="scroll-table-body glass">
        <table>
          <tbody class="scroll-table-body glass" >
            <tr v-for="item in this.users_sort" class="list-item">
              <td>{{item.user_id}}</td>
              <td>{{item.username}}</td>
              <td>{{item.email}}</td>
              <td>
                <RouterLink to="/adminmenu/list/users/category/users" class="btn btn-outline-danger transition"
                  >Удалить</RouterLink
                >
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="create">
      <RouterLink class="btn btn-outline-success" :to="'/registration?category_id='+String(category_id)">Создать</RouterLink>
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
  color: red;
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
  justify-content: flex-end;
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
  height: 500px;
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
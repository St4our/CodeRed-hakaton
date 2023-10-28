<script>
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';

export default {};
</script>

<template>
  <div class="container">
    <table class="table table-dark table-hover">
      <thead>
        <tr>
          <th scope="col"></th>
          <th scope="col">Название</th>
          <th scope="col">Удаление</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>
            <button type="button" class="btn btn-outline-danger">
              Удалить
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.table {
  background: rgb(93 93 93 / 6%);
  border-radius: 16px;
  box-shadow: 0 4px 30px rgb(0 0 0 / 10%);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  border: 1px solid rgba(9, 9, 9, 0.3);
}
</style>

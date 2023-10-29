<script>
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';

export default {
  data() {
    return {
      password: false,
      edit: false,
      fullname: 'Лысенков Никита Егорович',
      phone: '+7(904)-206-53-93',
      email: 'nikitalysenkov8@gmail.com',
      organization: 'Тык',
      login: 'Nikita',
    };
  },
  methods: {
    async profileLoad(){
      let response = await axios.post(`/hello`)
    }
  },
};
</script>

<template>
  <div class="container">
    <div class="wrapper-profile">
      <div class="title">
        <span>Персонаж</span>
        <button v-if="!edit" class="edit" @click="edit = true">
          Редактировать
        </button>
        <button v-if="edit" class="submit" @click="edit = false">Сохранить</button>
      </div>
      <div class="wrapper-group">
        <div class="group">
          <span>ФИО: </span>
          <span v-if="!edit">Лысенков Никита Егорович</span>
          <input v-if="edit" type="text" v-model="fullname" />
        </div>
        <div class="group">
          <span>Номер: </span>
          <span v-if="!edit">+7(904)-206-53-93</span>
          <input v-if="edit" type="text" v-model="phone" />
        </div>
        <div class="group">
          <span>Email: </span>
          <span v-if="!edit">nikitalysenkov8@gmail.com</span>
          <input v-if="edit" type="text" v-model="email" />
        </div>
        <div class="group">
          <span>Организация: </span>
          <span v-if="!edit">Тык</span>
          <input v-if="edit" type="text" v-model="organization" />
        </div>
        <div class="group">
          <span>Логин: </span>
          <span v-if="!edit">Nikita</span>
          <input v-if="edit" type="text" v-model="login" />
        </div>
        <div class="group">
          <span>Пароль: </span>
          <div class="password">
            <span v-if="password">Ананас</span>
            <span v-if="!password">**********</span>
            <ion-icon
              @click="password = true"
              v-if="!password"
              name="eye"
            ></ion-icon>
            <ion-icon
              @click="password = false"
              v-if="password"
              name="eye-off"
            ></ion-icon>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
input {
  border: none;
}
.submit {
  color: #46a71d;
  border: none;
  background: transparent;
}
.edit {
  border: none;
  background: transparent;
  color: #a71d31;
}
.password {
  display: flex;
  align-items: center;
  gap: 10px;
}
.password ion-icon,
svg {
  cursor: pointer;
  fill: #a71d31;
}
.group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}
.wrapper-group {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  padding: 10px;
}
.title {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  width: 100%;
  border-bottom: 1px solid #a71d31;
}
.wrapper-profile {
  min-width: 100%;
  height: 60%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 50px;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
</style>

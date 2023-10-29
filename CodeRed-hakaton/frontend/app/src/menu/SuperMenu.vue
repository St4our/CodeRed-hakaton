<script>
import { RouterLink, RouterView } from 'vue-router';

export default {
  data() {
    return {
      active: 0,
    };
  },
  methods: {
    click() {
      this.active == 1 ? (this.active = 0) : (this.active = 1);
    },
    close() {
      if (this.active == 1) {
        this.active = 0;
      }
    },
  },
};
</script>

<template>
  <div class="container1">
    <div class="card1">
      <div class="face face1">
        <div class="content">
          <img
            src="../assets/organizations.png"
          />
          <h3>Список Организаций</h3>
        </div>
      </div>
      <div class="face face2">
        <div class="content">
          <RouterLink to="/supermenu/list/organization">Перейти</RouterLink>
        </div>
      </div>
    </div>
    <div class="card1">
      <div class="face face1">
        <div class="content">
          <img src="../assets/test.png" />
          <h3>Тесты</h3>
        </div>
      </div>
      <div class="face face2">
        <div class="content">
          <RouterLink to="/menu/test">Перейти</RouterLink>
        </div>
      </div>
    </div>
    <div class="card1">
      <div class="face face1">
        <div class="content">
          <img src="../assets/lessons.png" />
          <h3>Уроки</h3>
        </div>
      </div>
      <div class="face face2">
        <div class="content">
          <RouterLink to="#">Перейти</RouterLink>
        </div>
      </div>
    </div>
    <div class="card1">
      <div class="face face1">
        <div class="content">
          <img src="../assets/chat.png" />
          <h3>Чат Поддержки</h3>
        </div>
      </div>
      <div class="face face2">
        <div class="content">
          <RouterLink to="/menu/chat">Перейти</RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<style>

body {
  margin: 0;
  padding: 0;
  min-height: 100vh;
  background: #333;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: consolas;
}

.container1 {
  width: 100%;
  position: relative;
  display: flex;
  justify-content: space-between;
  gap: 25px;
}

.container1 .card1 {
  position: relative;
  cursor: pointer;
}

.container1 .card1 .face {
  width: 300px;
  height: 200px;
  transition: 0.5s;
}

.container1 .card1 .face.face1 {
  position: relative;
  background: #333;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1;
  transform: translateY(100px);
}

.container1 .card1:hover .face.face1 {
  background: #e9190f;
  transform: translateY(0);
  /* #ff0057 */
}

.container1 .card1 .face.face1 .content {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  opacity: 0.6;
  transition: 0.5s;
}


.container1 .card1 .face.face2 .content{
  display: flex;
  align-items: center;
  justify-content: center;
}

.container1 .card1:hover .face.face1 .content{
  opacity: 1;
}

.container1 .card1 .face.face1 .content img {
  max-width: 100px;
}

.container1 .card1 .face.face1 .content h3 {
  margin: 10px 0 0;
  padding: 0;
  color: #fff;
  text-align: center;
  font-size: 1.5em;
}

.container1 .card1 .face.face2 {
  position: relative;
  background: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  box-sizing: border-box;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
  transform: translateY(-100px);
}


.container1 .card1:hover .face.face2{
  transform: translateY(-150px);
}

.container1 .card1 .face.face2 .content p {
  margin: 0;
  padding: 0;
}


.container1 .card1 .face.face2 .content a{
  position: absolute;
  display:  inline-block;
  text-decoration: none;
  font-weight: 900;
  color: #333;
  padding: 5px;
  border: 1px solid #333;
  bottom: 0;
  margin-bottom: 5px;
}

.container1 .card1 .face.face2 .content a:hover {
  background: #333;
  color: #fff;
}

@media (max-width: 1300px) {
  .container1 {
    flex-direction: column;
    gap: 0;
  }
  .container1 .card1 .face{
    width: 250px;
    height: 85px;
    transition: 0.5s;
  }

  .container1 .card1 .face.face1 .content img{
    max-width: 40px;
  }

  .container1 .card1 .face.face1 .content h3{
    margin: 10px 0 0;
    padding: 0;
    color: #fff;
    text-align: center;
    font-size: 1.1em;
  }

  .container1 .card1 .face.face2{
    position: relative;
    background: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    box-sizing: border-box;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
    transform: translateY(15px);
  }

  .container1 .card1:hover .face.face2{
    transform: translateY(-17px);
  }
}
</style>

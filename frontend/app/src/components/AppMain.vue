<script>
import { RouterLink, RouterView } from "vue-router";
import axios from "axios";

export default {
  components: {},
  data() {
    return {};
  },
  methods: {
    go_down() {
      window.scrollTo({
        top: 1000,
        behavior: "smooth",
      });
    },

    go_up(){
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    }
  },
  mounted() {},
};
</script>

<template>
  <div class="wrapper">
    <div class="nav">
      <div class="item">О нас</div>
      <div class="item" @click="go_down">Тарифы</div>
      <div class="item"><RouterLink to="/form">Оставить заявку</RouterLink></div>
      <div class="item active"><RouterLink to="/login">Войти</RouterLink></div>
    </div>
    <div class="content">
      <div class="text">
        <h1>
          <span><i>ПрофТестиум</i></span>
          <span><i> - </i></span>
          <span><i>это</i></span>
          <br />
          <span><i>веб-приложение</i></span>
        </h1>
        <p>
          предназначенное для обучения и тестирования сотрудников предприятия.
          Она предоставляет удобную платформу, которая позволяет создавать и
          проводить обучающие курсы и тесты, проходить обучение в VR, а также
          отслеживать и оценивать академические достижения сотрудников.
        </p>
      </div>
      <div class="image">
        <img src="../assets/about.png" alt="" />
      </div>
    </div>
    <div class="services" id="bottom">
      <div class="cards">
        <div class="card shadow">
          <ul>
            <li class="pack">Базовый</li>
            <li id="basic" class="price bottom-bar">1500₽/месяц</li>
            <li class="bottom-bar">до 5 сотрудников</li>
            <li class="bottom-bar">1 администратор</li>
            <li class="bottom-bar">до 10 уроков</li>
            <li><RouterLink to="/form" class="btn">Подробнее</RouterLink></li>
          </ul>
        </div>
        <div class="card active">
          <ul>
            <li class="pack">Профессиональный</li>
            <li id="professional" class="price bottom-bar">3500₽/месяц</li>
            <li class="bottom-bar">до 20 сотрудников</li>
            <li class="bottom-bar">до 2 администраторов</li>
            <li class="bottom-bar">до 50 уроков</li>
            <li><RouterLink to="/form" class="btn active-btn">Подробнее</RouterLink></li>
          </ul>
        </div>
        <div class="card shadow">
          <ul>
            <li class="pack">Мастер</li>
            <li id="master" class="price bottom-bar">5000₽/месяц</li>
            <li class="bottom-bar">до 100 сотрудников</li>
            <li class="bottom-bar">до 3 администраторов</li>
            <li class="bottom-bar">до 100 уроков</li>
            <li><RouterLink to="/form" class="btn">Подробнее</RouterLink></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer">
      <div class="img">
        <RouterLink to="/menu">
          <img src="../assets/logo.png" class="codered" alt="logo.png" />
          <p class="text-codered">CodeRed</p>
        </RouterLink>
      </div>
      <div class="nav-bottom">
        <div class="item" @click="go_up">О нас</div>
        <div class="item">Тарифы</div>
        <div class="item"><RouterLink to="/form">Оставить заявку</RouterLink></div>
        <div class="item">
          <RouterLink to="/policy">Политика Конфиденциальности</RouterLink>
        </div>
      </div>
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

:root {
  font-size: 32px;
}

::-webkit-scrollbar {
  width: 0;
}

.footer {
  width: 100%;
  height: 100px;
  border-top: 1px solid #950707;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

a {
  text-decoration: none;
  color: var(--color-text);
  z-index: 2;
}

body {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  min-height: 100vh;
  font-family: Helvetica;
}

.text {
  width: 50%;
}

.image {
  height: 600px;
  width: auto;
  z-index: 1;
}
.nav {
  margin-top: 10px;
  top: 2%;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 50px;
  z-index: 2;
}

.nav-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  z-index: 2;
}

.content {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 0px 60px;
}

.services {
}

.item {
  font-size: large;

  transition: color 300ms;
}

.item.active,
.item:hover,
.item a:hover,
.item a:active {
  cursor: pointer;
  color: #950707;
}

.active a{
  color: #950707;
}

.active a:hover, .active a:active {
  color: #fff;
}

.wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: black;
  gap: 50px;
}
h1 {
  margin: 0;
  letter-spacing: -2px;
  font-size: 45px;
}

p {
  font-size: 1.1rem;
  color: #666;
  line-height: 1.3rem;
  position: relative;
  top: 0.8rem;
  opacity: 0;
  animation: 0.5s swift-up ease-out forwards, 0.5s fade-in ease-out forwards;
  animation-delay: 0.8s;
}

@keyframes fade-in {
  to {
    opacity: 1;
  }
}

span {
  display: inline-block;
  overflow: hidden;
  position: relative;
  top: 0.8rem;
  animation: 0.3s swift-up ease-in-out forwards;
}

i {
  font-style: normal;
  position: relative;
  top: 2rem;
  animation: 0.5s swift-up ease-in-out forwards;
}

@keyframes swift-up {
  to {
    top: 0rem;
  }
}

span:nth-of-type(1) i {
  animation-delay: 0s;
}

span:nth-of-type(2) i {
  animation-delay: 0.1s;
}

span:nth-of-type(3) i {
  animation-delay: 0.2s;
}

span:nth-of-type(4) i {
  animation-delay: 0.3s;
}

span:nth-of-type(5) i {
  animation-delay: 0.4s;
}

span:nth-of-type(6) i {
  animation-delay: 0.5s;
}

span:nth-of-type(1) {
  animation-delay: 0s;
}

span:nth-of-type(2) {
  animation-delay: 0.1s;
}

span:nth-of-type(3) {
  animation-delay: 0.2s;
}

span:nth-of-type(4) {
  animation-delay: 0.3s;
}

span:nth-of-type(5) {
  animation-delay: 0.4s;
}

span:nth-of-type(6) {
  animation-delay: 0.5s;
}

.codered {
  height: 50px;
  width: auto;
  cursor: pointer;
  z-index: 2;
}

.text-codered {
  margin: 0 0 0 10px;
  font-size: 16px;
  font-weight: 700;
  text-transform: uppercase;
}

.img {
  left: 0;
  padding-top: 10px;
}

.img a {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Services */

.sub {
  background: linear-gradient(
    135deg,
    rgba(163, 168, 240, 1) 0%,
    rgba(105, 111, 221, 1) 100%
  );
  display: flex;
  justify-content: flex-start;
  align-items: center;
  /* height: 25px;
  width: 50px; */
  height: 1.6rem;
  width: 3.3rem;
  border-radius: 1.6rem;
  padding: 0.3rem;
}
.circle {
  background-color: #fff;
  height: 1.4rem;
  width: 1.4rem;
  border-radius: 50%;
}
.checkbox:checked + .sub {
  justify-content: flex-end;
}

.cards {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}

.card {
  background: #fff;
  color: rgb(149, 7, 7);
  border-radius: 0.8rem;
}

.cards .card.active {
  background: rgb(149, 7, 7);
  color: #fff;
  display: flex;
  align-items: center;
  transform: scale(1.1);
  z-index: 1;
}
ul {
  margin: 2.6rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}
ul li {
  list-style-type: none;
  display: flex;
  justify-content: center;
  width: 100%;
  padding: 1rem 0;
}
ul li.price {
  font-size: 3rem;
  color: hsl(232, 13%, 33%);
  padding-bottom: 2rem;
}
.shadow {
  box-shadow: -5px 5px 15px 1px rgba(0, 0, 0, 0.1);
}

.card.active .price {
  color: #fff;
}

.btn {
  margin-top: 1rem;
  height: 2.6rem;
  width: 13.3rem;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 4px;
  background: rgb(149, 7, 7);
  color: #fff;
  outline: none;
  border: 0;
  font-weight: bold;
}
.active-btn {
  background: #fff;
  color: rgb(149, 7, 7);
}
.bottom-bar {
  border-bottom: 2px solid hsla(240, 8%, 85%, 0.582);
}
.card.active .bottom-bar {
  border-bottom: 2px solid hsla(240, 8%, 85%, 0.253);
}
.pack {
  font-size: 1.1rem;
}

@media (max-width: 280px) {
  ul {
    margin: 1rem;
  }
  h1 {
    font-size: 1.2rem;
  }
  .toggle {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    height: 80px;
  }
  .cards {
    margin: 0;
    display: flex;
    flex-direction: column;
  }

  .card {
    transform: scale(0.8);
    margin-bottom: 1rem;
  }
  .cards .card.active {
    transform: scale(0.8);
  }
}

@media (min-width: 280px) and (max-width: 320px) {
  ul {
    margin: 20px;
  }
  .cards {
    display: flex;
    flex-direction: column;
  }
  .card {
    margin-bottom: 1rem;
  }
  .cards .card.active {
    transform: scale(1);
  }
}

@media (min-width: 320px) and (max-width: 414px) {
  .cards {
    display: flex;
    flex-direction: column;
  }
  .card {
    margin-bottom: 1rem;
  }
  .cards .card.active {
    transform: scale(1);
  }
}
@media (min-width: 414px) and (max-width: 768px) {
  .card {
    margin-bottom: 1rem;
    margin-right: 1rem;
  }
  .cards .card.active {
    transform: scale(1);
  }
}
@media (min-width: 768px) and (max-width: 1046px) {
  .cards {
    display: flex;
  }
  .card {
    margin-bottom: 1rem;
    margin-right: 1rem;
  }
  .cards .card.active {
    transform: scale(1);
  }
}

@media (max-width: 930px) {
  .content {
    padding: 0 30px;
  }
}

@media (max-width: 825px) {
  .content {
    flex-direction: column;
  }
  .text {
    width: 80%;
  }

  .nav-bottom {
    gap: 15px;
  }

  .item {
    font-size: medium;
  }
}

@media (max-width: 420px) {

  .nav-bottom {
    flex-direction: column;
    gap: 0;
  }

  .h1 {
    font-size: 34px;
  }
}
</style>

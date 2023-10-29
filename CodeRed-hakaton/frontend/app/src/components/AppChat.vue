<script>
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';

export default {};
</script>

<template>
  <div class="container">
    <div class="wrapper-chat">
      <div class="title">
        <span class="sub">Поддержка</span>
        <span class="online sub">Online</span>
      </div>
      <div class="main-chat">
        <div class="message">
            <div class="title">
                <span class="sub">17:00</span>
                <span class="sub">Поддержка</span>
            </div>
            <div class="message-body">
                <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga ipsum voluptatem eaque voluptate quam distinctio facere suscipit asperiores fugiat, obcaecati unde debitis voluptatibus dolorum! Voluptas perferendis minus laudantium ullam odio!</span>
            </div>
        </div>
      </div>
      <div class="wrapper-send">
        <input type="text" class="input-send" />
        <button class="btn-send"><ion-icon name="send"></ion-icon></button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sub{
    color: #9c9e9e !important;
}
span{
    color: #fff;
}
.message-body{
    padding: 10px;
}
.message{
    background: #00000032;
}
.online{
    position: relative;
}
.online::before{
    content: '';
    position: absolute;
    top: 0;
    left: -10px;
    width: 8px;
    height: 8px;
    border-radius:100% ;
    background: #a71d31;
}
.main-chat {
  padding: 10px;
  width: 100%;
  height: 100%;
  background: rgba(60, 60, 60, 0.449);
  border-radius: 16px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  border: 1px solid rgba(9, 9, 9, 0.3);
}
.btn-send,
svg {
  color: #a71d31 !important;
}
.btn-send {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 26px;
  border-radius: 0 10px 10px 0;
  border: none;
  background: transparent;
}

.wrapper-send input {
  width: 50%;
  border: none;
  border-radius: 10px;
}
.wrapper-send {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 100%;
  height: 40px;
}
.main-color{
    color: #a71d31 !important;
}
.title {
  padding: 10px;
  width: 100%;
  height: 40px;
  background: #0116;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom:1px solid #a71d31 ;
}

.container {
  width: 100%;
  height: 70%;
}
.wrapper-chat {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
</style>

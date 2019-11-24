<template>
  <div>
    <div>
      <div class="background">
        <img
          class="img-fluid"
          src="https://sun9-68.userapi.com/c857216/v857216236/5fb54/v3frS2EH53Y.jpg"
          style="height:820px"
        />
      </div>
      <div class="head"></div>
      <nav class="container">
        <div class="row"></div>
        <div class="col align-self-end">
          <div class="header-list">
            <a href="/map">Карта</a>
            <a href="#info">Информация</a>
            <a href="#results">Результаты</a>
            <a href="#rate">Рейтинги</a>
            <a href="#feeds">Новости</a>
            <a href="#about">О портале</a>
            <a href="#login">Войти</a>
          </div>
        </div>
      </nav>
    </div>
    <div>
      <div class="buttons">
        <button class="button1" @click="$router.push('payment')">Оплатить ЖКХ</button>
        <button class="button1" @click="$router.push('map')">Сообщить о проблеме</button>
        <button class="button2">Предложить идею</button>
      </div>
      <div class="statistic">
        <div class="offset-md-2">
          <div class="row">
            <img class="user-icon" src="../../images/user.png" />
            <div class="user-nad">Зарегестрировано пользователей</div>
          </div>
        </div>
        <div class="numbers">
          <div class="row">
            <img class="user-icon" src="../../images/user.png" />
            <div class="user-nad">Всего решено проблем</div>
          </div>
        </div>
      </div>
      <div class="statistic2">
        <div class="offset-md-2">0 000 000</div>
        <div class="offset-md-3">0 000 000</div>
      </div>
      <div class="footer">
        <div class="row">
          <div class="col-3 offset-md-1">
            <p class="text">О Портале</p>
            <a href>
              Регламент обработки информации на портале ­­­«Удобный Город»
              <br />
            </a>
            <a href>
              Условия использования информации
              <br />
            </a>
            <a href>Расскажи друзьям</a>
          </div>
          <div class="col-3 offset-md-1">
            <p class="text">Посетителям</p>
            <a>
              Единные правила модерации
              <br />
            </a>
            <a>
              Часто задаваемые вопросы
              <br />
            </a>
            <a>Предложить идею или сообщить об ошибке в работе Портала</a>
          </div>
          <div class="col-3 offset-md-1">
            <p class="text">Мобильные приложения</p>
            <a href>
              iOS
              <br />
            </a>
            <a href>Android</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Index"
};
</script>

<style scoped>
body {
  background: #dcf5ff;
  font-family: "Roboto", sans-serif;
}

.background {
  position: absolute;
  z-index: -1;
}

.head {
  text-transform: uppercase;
  border-bottom: 3px solid #515369;
}

nav {
  padding-top: 0px;
  align-items: center;
  margin-left: 5%;
  margin-right: 5%;
  margin-top: 15px;
  padding-bottom: 35px;
  border-bottom: 3px solid #515369;
  position: relative;
  text-transform: uppercase;
  font-size: 14px;
}

nav .row {
  z-index: 1;
  align-items: center;
}

.header-list {
  float: right;
}

.header-list a {
  margin-left: 20px;
  color: black;
  text-decoration: none;
}

.buttons {
  text-align: center;
  align-content: center;
}
.buttons .button {
  margin-bottom: 25px;
}

.button1 {
  font-family: "Bebas Neue", cursive;
  text-transform: uppercase;
  margin-top: 664px;
  margin-right: 205px;
  width: 250px;
  height: 80px;
  border: 3px solid #515369;
  color: #30d5c8;
  background: rgba(0, 0, 150, 1);
}

.button2 {
  font-family: "Bebas Neue", cursive;
  text-transform: uppercase;
  margin-top: 664px;
  width: 250px;
  height: 80px;
  border: 3px solid #515369;
  color: #30d5c8;
  background: rgba(0, 0, 150, 1);
}

.statistic {
  background-color: #f7f4f2;
  display: flex;
}

.user-icon {
  margin-top: 150px;
  max-width: 50px;
}

.user-nad {
  margin-top: 150px;
  font-size: 20px;
}

.statistic2 {
  background-color: #f7f4f2;
  display: flex;
  font-size: 100px;
  padding-bottom: 100px;
}

.numbers {
  margin-left: 30%;
  font-family: "Bebas Neue", cursive;
}

.footer {
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>

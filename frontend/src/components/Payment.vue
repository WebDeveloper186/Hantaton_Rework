<template>
  <div class="main">
    <header>
      <nav>
        <h2>Единый сайт для оплаты ЖКУ</h2>
        <ul class="topmenu">
          <li>
            <a href="/">Главная</a>
          </li>
          <li>
            <a href="/map">Карта обращений</a>
          </li>
          <li>
            <a href="/payment">Платежи</a>
          </li>
          <li>
            <a href="/login">Контакты</a>
          </li>
        </ul>
      </nav>
    </header>

    <form>
      <div
        v-if="showInfo == false"
        class="login"
        style="margin: 200px;padding-left: 400px;"
      >
        <div
          class="col-3"
          style="background-color: gray;border-radius: 33px; padding-bottom: 15px"
        >
          <div class="form-group">
            <label for="exampleFormControlSelect1"
              >Выберите населенный пункт</label
            >
            <select
              class="form-control"
              id="exampleFormControlSelect1"
              v-model="select"
            >
              <option></option>
              <option>Сургут</option>
              <option>Белый Яр</option>
              <option>Лангепас</option>
              <option>Лянтор</option>
              <option>Солнечный</option>
            </select>
          </div>
          <div class="form-group">
            <label for="exampleInputEmail1">Введите адрес</label>
            <select class="form-control" id="exampleInputEmail1">
              <option v-for="item in chose" :key="chose.indexOf(item)">{{
                item
              }}</option>
            </select>
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Введите дом</label>
            <input
              type="number"
              class="form-control"
              id="exampleInputPassword1"
            />
          </div>
          <div class="form-group">
            <label for="exampleInputEmail">Введите квартиру</label>
            <input
              type="email"
              class="form-control"
              id="exampleInputEmail"
              aria-describedby="emailHelp"
            />
          </div>
          <button
            type="submit"
            class="btn btn-primary"
            style="margin-left: 30px"
            @click="change()"
          >
            Узнать платеж
          </button>
        </div>
      </div>
      <div v-else class="login" style="margin: 200px;padding-left: 400px;">
        <div
          class="col-8"
          style="background-color: gray;border-radius: 33px; padding-bottom: 15px"
        >
          <div class="form-group"></div>
          <div class="form-row">
            <div class="form-group col">
              <label for="inputState">Услуги ЖКУ:</label>
            </div>
            <div class="form-group col-md-3">
              <div id="result">0 руб.</div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col">
              <label for="inputState">Оплата за социальный наем:</label>
            </div>
            <div class="form-group col-md-3">
              <div id="result">0 руб.</div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col">
              <label for="inputState">Оплата взноса на кап.ремонт:</label>
            </div>
            <div class="form-group col-md-3">
              <div id="result">0 руб.</div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col">
              <label for="inputState">Оплата за паркинг:</label>
            </div>
            <div class="form-group col-md-3">
              <div id="result">0 руб.</div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col">
              <label for="inputState">Обслуживание системы наблюдения:</label>
            </div>
            <div class="form-group col-md-3">
              <div id="result">0 руб.</div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col">
              <label for="inputState">Обслуживание шлагбаумов:</label>
            </div>
            <div class="form-group col-md-3">
              <div id="result">0 руб.</div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col">
              <label for="inputState">Обращение с ТКО:</label>
            </div>
            <div class="form-group col-md-3">
              <div id="result">0 руб.</div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col">
              <label for="inputState">Отопление:</label>
            </div>
            <div class="form-group col-md-3">
              <div id="result">0 руб.</div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col">
              <label for="inputState">Электроснабжение:</label>
            </div>
            <div class="form-group col-md-3">
              <div id="result">0 руб.</div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col">
              <label for="inputState">Тепловая энергия для ГВС:</label>
            </div>
            <div class="form-group col-md-3">
              <div id="result">0 руб.</div>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col">
              <label for="inputState">Холодная вода для ГВС:</label>
            </div>
            <div class="form-group col-md-3">
              <div id="result">0 руб.</div>
            </div>
          </div>
          <button
            type="submit"
            class="btn btn-primary"
            style="margin-left: 190px"
          >
            Оплатить
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Payment",
  data() {
    return {
      showInfo: false,
      select: null,
      surgut: ["Ленина", "Маяковского", "Мира", "Губкина", "Чехова"],
      whiteyar: ["Совхозная", "Фадеева", "Лесная", "Некрасова"],
      langepas: ["Звездный проезд", "Комсомольская", "Минская", "Мира"],
      lyantor: ["Магистральная", "Брусничный", "Дружбы Народов", "Кедровый"],
      solnechniy: ["Космонавтов", "Молодежная", "Советская", "Строителей"],
      chose: []
    };
  },
  watch: {
    select() {
      if (this.select == "Сургут") {
        this.chose = [];
        this.chose = this.surgut;
      } else if (this.select == "Белый Яр") {
        this.chose = [];
        this.chose = this.whiteyar;
      } else if (this.select == "Лангепас") {
        this.chose = [];
        this.chose = this.langepas;
      } else if (this.select == "Лянтор") {
        this.chose = [];
        this.chose = this.lyantor;
      } else if (this.select == "Солнечный") {
        this.chose = [];
        this.chose = this.solnechniy;
      } else {
        this.chose = [];
      }
    }
  },
  methods: {
    change() {
      this.showInfo = !this.showInfo;
    }
  }
};
</script>

<style scoped>
header {
  background-color: #babfc7;
  text-align: center;
}

header a {
  display: block;
}
.topmenu:after {
  content: "";
  display: table;
  clear: both;
}

.topmenu > li {
  width: 25%;
  float: left;
  position: relative;
  font-family: "Open Sans", sans-serif;
}

.topmenu > li > a {
  text-transform: uppercase;
  font-size: 14px;
  font-weight: bold;
  color: #5e5e5e;
  padding: 15px 30px;
  min-width: 124px;
}

.topmenu li a:hover {
  color: rgb(15, 12, 2);
}

.submenu-link:after {
  content: "\f107";
  font-family: "FontAwesome";
  color: inherit;
  margin-left: 10px;
}

.submenu {
  background: #9fa3a9;
  position: absolute;
  left: 0;
  top: 100%;
  z-index: 5;
  width: 180px;
  opacity: 0;
  transform: scaleY(0);
  transform-origin: 0 0;
  transition: 0.5s ease-in-out;
}

.submenu a {
  color: white;
  text-align: left;
  padding: 12px 15px;
  font-size: 13px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.submenu li:last-child a {
  border-bottom: none;
}

.topmenu > li:hover .submenu {
  opacity: 1;
  transform: scaleY(1);
}
nav {
  display: table;
  margin: 0 auto;
}

nav ul {
  list-style: none;
  margin: 0;
}
</style>

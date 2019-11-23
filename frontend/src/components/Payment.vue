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
            <select class="form-control" id="exampleInputEmail1" v-model="adress">
              <option v-for="item in chose" :key="chose.indexOf(item)">{{
                item
              }}</option>
            </select>
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Введите дом</label>
            <select class="form-control" id="exampleInputEmail1" v-model="home">
              <option v-for="item in hati" :key="hati.indexOf(item)">{{
                item
              }}</option>
            </select>
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Введите квартиру</label>
            <select class="form-control" id="exampleInputEmail1">
              <option v-for="item in kv" :key="kv.indexOf(item)">{{
                item
              }}</option>
            </select>
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
      adress: null,
      home: null,
      surgut: ["Ленина", "Маяковского", "Мира", "Губкина", "Чехова"],
      whiteyar: ["Совхозная", "Фадеева", "Лесная", "Некрасова"],
      langepas: ["Звездный проезд", "Комсомольская", "Минская", "Мира"],
      lyantor: ["Магистральная", "Брусничный", "Дружбы Народов", "Кедровый"],
      solnechniy: ["Космонавтов", "Молодежная", "Советская", "Строителей"],
      
      
      hatalenina:['18/1','22','24/3','59'],
      hatamayak:['7','9','9/1','16'],
      hatamira:['3','4','4/1','6'],
      hatagubka:['14','15','16','18'],
      hatacheh:['1','9'],

      kvlen18:['1','2','3','4'],
      kvlen22:['1','2','3','4'],
      kvlen24_3:['1','2','3','4'],
      kvlen59:['3','4','5','6'],

      kvmay7:['1','2','3','4'],
      kvmay9:['1','2','3','4'],
      kvmay9_1:['1','2','3','4'],
      kvmay16:['1','10','11','13'],

      kvmir3:['1','2','3','4'],
      kvmir4:['1','2','3','4'],
      kvmir4_1:['1','2','3','4'],
      kvmir6:['2','3','4','5'],

      kvguba14:['1','2','3','4'],
      kvguba15:['1','2','3','4'],
      kvguba16:['1','2','3','4'],
      kvguba18:['1','2','3','4'],

      kvcheh1:['1','2','3','4'],
      kvcheh9:['1','2','3','4'],

      chose: [],
      hati: [],
      kv: [],
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
    },
    adress() {
      if (this.adress == "Ленина") {
        this.hati = [];
        this.hati = this.hatalenina;
      } else if (this.adress == "Маяковского") {
        this.hati = [];
        this.hati = this.hatamayak;
      } else if (this.adress == "Мира") {
        this.hati = [];
        this.hati = this.hatamira;
      } else if (this.adress == "Губкина") {
        this.hati = [];
        this.hati = this.hatagubka;
      } else if (this.adress == "Чехова") {
        this.hati = [];
        this.hati = this.hatacheh;
      } else {
        this.hati = [];
      }
    },
    home() {
      if (this.home == "18/1") {
        this.kv = [];
        this.kv = this.kvlen18;
      } else if (this.home == "22") {
        this.kv = [];
        this.kv = this.kvlen22;
      }
        else if (this.home == "24/3") {
        this.kv = [];
        this.kv = this.kvlen24_3;
      } else if (this.home == "59") {
        this.kv = [];
        this.kv = this.kvlen59;
      } else if (this.home == "7") {
        this.kv = [];
        this.kv = this.kvmay7;
      } else if (this.home == "9") {
        this.kv = [];
        this.kv = this.kvmay9;
      } 
       else if (this.home == "9/1") {
        this.kv = [];
        this.kv = this.kvmay9_1;
      } 
       else if (this.home == "16") {
        this.kv = [];
        this.kv = this.kvmay16;
      } 
       else if (this.home == "3") {
        this.kv = [];
        this.kv = this.kvmir3;
      } 
      else if (this.home == "4") {
        this.kv = [];
        this.kv = this.kvmir4;
      } 
      else if (this.home == "4/1") {
        this.kv = [];
        this.kv = this.kvmir4_1;
      } 
      else if (this.home == "6") {
        this.kv = [];
        this.kv = this.kvmir6;
      } 
       else if (this.home == "14") {
        this.kv = [];
        this.kv = this.kvguba14;
      } 
       else if (this.home == "15") {
        this.kv = [];
        this.kv = this.kvguba15;
      } 
       else if (this.home == "16") {
        this.kv = [];
        this.kv = this.kvguba16;
      } 
       else if (this.home == "18") {
        this.kv = [];
        this.kv = this.kvguba18;
      } 
        else if (this.home == "1") {
        this.kv = [];
        this.kv = this.kvcheh1;
      } 
        else if (this.home == "9") {
        this.kv = [];
        this.kv = this.kvcheh9;
      } 
      else {
        this.kv = [];
      }
    },
  methods: {
    change() {
      this.showInfo = !this.showInfo;
    }
  },
  },
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
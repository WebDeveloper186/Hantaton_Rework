<template>
  <div class="main">
    <header>
      <nav>
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
    <div class="map">
      <img
        @click="click"
        src="https://sun9-62.userapi.com/c856128/v856128327/1791cf/5WyuTmUML_k.jpg"
        alt="Карта"
        style="z-index:1"
      />
      <ul>
        <li v-for="point in points" :key="point[points.indexOf(point)]">
          <img
            :id="point.index"
            style="display:block; z-index:999; position: absolute; width:40px; heigth: 40px "
            :style="{
              top: point.top,
              left: point.left
            }"
            :left="point.left"
            :src="point.icon"
            @click="showInfo(point.index)"
          />
        </li>
      </ul>

      <img id="marker" style="display:none; z-index:999" :top="topCoords" />
    </div>
    <div class="icons">
      <ul v-for="icon in icons" :key="icons.indexOf(icon)">
        <li style="inline-block">
          <button
            type="button"
            class="btn btn-link"
            @click="changeIcon(icon.icon)"
          >
            <img :src="icon.icon" class="icon" />
          </button>
          <p>{{ icon.name }}</p>
        </li>
      </ul>
    </div>
    <div class="popup" v-if="showPopup == true" style="width:250px">
      <form id="order">
        <div v-if="test == false">
          <div class="form-group">
            <label for="exampleInputEmail1">Ваше имя</label>
            <input class="form-control" v-model="name" />

            <label for="exampleInputEmail1">Описание проблемы</label>
            <input class="form-control" v-model="description" />
          </div>
          <button type="text" class="btn btn-primary" @click="save">
            Отправить
          </button>
          <button
            type="text"
            class="btn btn-danger"
            style="margin-left: 60px"
            @click="closess"
          >
            X
          </button>
        </div>

        <div class="info" v-else style="z-index:999; left:35%; top:50%">
          <div class="form-group">
            <label for="exampleInputEmail1">Ваше имя</label>
            <input class="form-control" readonly v-model="info[0].name" />

            <label for="exampleInputEmail1">Описание проблемы</label>
            <input
              class="form-control"
              readonly
              v-model="info[0].description"
            />
          </div>
          <button type="text" class="btn btn-primary" @click="close">
            Закрыть
          </button>
        </div>
      </form>
    </div>
    <div
      v-if="alert == true"
      class="alert alert-danger"
      style="z-index:999; position: absolute; top:0; left:34%; width: 35%; height: 72px"
      role="alert"
    >
      <p style="padding-left:45px">
        Выбирете тип иконки, которую хотите разместить
      </p>
      <div
        class="btn btn-link"
        style="color:red; margin-bottom:5px;
    font-size: 25px;"
        @click="alert = false"
      >
        X
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Map",
  data() {
    return {
      test: false,
      alert: false,
      pop: false,
      showPopup: false,
      points: [],
      topCoords: 0,
      icons: this.$store.state.icons,
      size: 40,
      select: undefined,
      index: 0,
      name: "",
      description: "",
      info: []
    };
  },
  methods: {
    click(e) {
      var image = document.getElementById("marker");
      if (this.select != undefined) {
        this.show();
        image.height = this.size;
        image.width = this.size;
        image.style.display = "none";
        image.style.position = "absolute";
        image.style.top = e.clientY - this.size / 2 + "px";
        image.style.left = e.clientX - this.size / 2 + "px";
      } else {
        this.alert = true;
      }
    },
    changeIcon(icon) {
      var image = document.getElementById("marker");
      this.select = icon;
      image.src = icon;
    },
    show() {
      this.showPopup = true;
    },
    save() {
      var image = document.getElementById("marker");
      this.pop = true;
      this.showPopup = false;
      this.index += 1;
      var object = {
        index: this.index,
        top: image.style.top,
        left: image.style.left,
        icon: this.select,
        name: this.name,
        description: this.description
      };
      this.points.push(object);
      this.pop = false;
      this.name = "";
      this.description = "";
    },
    showInfo(index) {
      this.info.push(this.points[index - 1]);
      this.test = true;
    },
    close() {
      this.test = false;
    },
    closess() {
      document.getElementsByClassName("popup").style.display = "none";
    }
  }
};
</script>

<style scoped>
* {
  text-decoration: none;
}
img {
  position: relative;
}
p {
  display: inline-block;
  padding-left: 10px;
}
li {
  list-style-type: none;
}
.icons {
  position: absolute;
  top: 100px;
  right: 100px;
}
.icon {
  width: 40px;
  height: 40px;
}

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
.popup {
  padding: 25px;
  position: absolute;
  top: 35%;
  left: 35%;
  z-index: 999;
  width: 200px;
  border-radius: 10px;
  background-color: lightgray;
}
</style>

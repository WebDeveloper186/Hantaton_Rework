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
            <a href="/contacts">Контакты</a>
          </li>
        </ul>
      </nav>
    </header>
    <div class="media">
      <img src="https://hackathon.uriit.ru/upload/resize_cache/iblock/703/600_600_1/team4877aa5bcabe77dc8540bb005972a92f.png" class="mr-3">
      <div class="media-body">
        <h5 class="mt-0">Список разработчиков</h5>
        <ol>
          <li>Капитан команды - Сазонов Савелий</li>
          <li>Прокофьев Александр</li>
          <li>Чернов Дмитрий</li>
          <li>Таран Юлия</li>
          <li>Воротников Артём</li>
          <li>Хусаинов Сергей</li>
          <li>Лепнинских Александр</li>
        </ol>
      </div>
    </div>
    </div>
  
</template>

<script>
export default {
  name: "Index"
};
</script>

<style scoped >
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
.media {
  background: #ffffff;
  width: 80%;
  margin-top: 40px;
  margin-left: 200px;
  border-bottom: 3px solid black;
  border-left: 3px solid black;
  border-top: 3px solid black;
  border-right: 3px solid black;
  box-shadow: 0 0 100px rgba(0, 0, 0, 0.5) !important;
}
</style>
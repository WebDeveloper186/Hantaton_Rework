<template>
<div>
    <header>
          <nav>
            <h2>Единый сайт для оплаты ЖКУ</h2>
            <ul class="topmenu">
              <li><a href="/">Главная</a></li>
              <li><a href="/about" class="submenu-link" target="_blank">Обращения</a>
                <ul class="submenu">
                  <li><a href="/history">1</a></li>
                  <li><a href="/service">2</a></li>
                  <li><a href="/soglasie" target="_blank">3</a></li>
                </ul>
              </li>
              <li><a href="/contacts">ФЫАВ</a></li>
              <li><a href="/login">Контакты</a></li>
            </ul>
          </nav>
        </header>
        
  <form>
  <div class="login" style="margin: 200px;padding-left: 400px;">
    <div class="col-3" style="background-color: black;border-radius: 33px; padding-bottom: 15px">
      <div class="form-group">
        <label for="exampleInputEmail1">Введите адрес</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Введите дом</label>
        <input type="number" class="form-control" id="exampleInputPassword1">
      </div>
      <div class="form-group">
        <label for="exampleInputEmail">Введите квартиру</label>
        <input type="email" class="form-control" id="exampleInputEmail" aria-describedby="emailHelp">
      </div>
      <button type="submit" class="btn btn-primary" style="margin-left: 30px" href="/" >Узнать платеж</button>
    </div>
  </div>
  </form>
</div>
  
</template>

<script>
export default {
  name: "Payment"
};
</script>

<style scoped>
body{
  background-color: black;
}

/* шапка */
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

.topmenu>li {
  width: 25%;
  float: left;
  position: relative;
  font-family: 'Open Sans', sans-serif;
}

.topmenu>li>a {
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
  transition: .5s ease-in-out;
}

.submenu a {
  color: white;
  text-align: left;
  padding: 12px 15px;
  font-size: 13px;
  border-bottom: 1px solid rgba(255, 255, 255, .1);
}

.submenu li:last-child a {
  border-bottom: none;
}

.topmenu>li:hover .submenu {
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
/* шапка */

</style>
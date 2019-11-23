<template>
  <div class="main">
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
          />
        </li>
      </ul>

      <img id="marker" style="display:none; z-index:999" :top="topCoords" />
    </div>
    <div class="icons">
      <ul v-for="icon in icons" :key="icons.indexOf(icon)">
        <li style="inline-block">
          <button type="text" @click="changeIcon(icon.icon)">
            <img :src="icon.icon" class="icon" />
          </button>
          <p>{{ icon.name }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Map",
  data() {
    return {
      points: [],
      topCoords: 0,
      icons: this.$store.state.icons,
      size: 40,
      select: undefined,
      index: 0
    };
  },
  methods: {
    click(e) {
      var image = document.getElementById("marker");
      if (this.select != undefined) {
        image.height = this.size;
        image.width = this.size;
        image.style.display = "none";
        image.style.position = "absolute";
        image.style.top = e.clientY - this.size / 2 + "px";
        image.style.left = e.clientX - this.size / 2 + "px";
        this.index += 1;
        var object = {
          index: this.index,
          top: image.style.top,
          left: image.style.left,
          icon: this.select
        };
        this.points.push(object);
      } else {
        alert("Выбирете тип иконки, которую хотите разместить");
      }
    },
    changeIcon(icon) {
      var image = document.getElementById("marker");
      this.select = icon;
      image.src = icon;
    }
  }
};
</script>

<style scoped>
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
  top: 10px;
  right: 100px;
}
.icon {
  width: 40px;
  height: 40px;
}
</style>

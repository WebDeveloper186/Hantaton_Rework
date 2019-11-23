<template>
  <div class="main">
    <div class="map"><img @click="click" src="" alt="Карта" /></div>
  </div>
</template>

<script>
export default {
  name: "Map",
  data() {
    return {};
  },
  methods: {
    click(e) {
        
    }
  }
};
</script>

<style scoped>
.ymap-container {
  height: 720px;
}
.red {
  color: red;
}
</style>

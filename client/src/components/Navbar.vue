<template>
  <div class="navbar">
    <div v-for="route in routes"
         class="navbar-item"
         :key="route.to"
         :class="{'navbar-active': $route.path === route.to}">
      <router-link :to="route.to">{{route.name}}</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'navbar',
  data: function () {
    return {
      routes: [
        {name: 'Login', to: '/login'},
        {name: 'Tasks', to: '/tasks'}
      ]
    }
  }
}
</script>

<style lang="less" scoped>
@import "../assets/styles.less";

/* navbar */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  overflow: hidden;
  background-color: @color-dark;

  box-shadow: 0 6px 15px 0 rgba(0, 0, 0, 0.35);
}

.navbar-item {
  float: left;
}

.navbar-item a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.navbar-item a:hover {
  color: @color-dark;
  background-color: @color-light;
}

.navbar-active {
  background-color: #333;
  color: white;
}
</style>

<template>
  <div id="navbar">
    <div class="navbar-left">
    <div v-for="route in routes"
         class="navbar-item"
         :key="route.to"
         :class="{'navbar-active': $route.path === route.to}">
      <router-link :to="route.to">{{route.name}}</router-link>
    </div>
    </div>

    <div class="navbar-right">
      <div v-if="isLoggedIn" class="navbar-item"><router-link to="/logout">Logout</router-link></div>
      <div v-else class="navbar-item" :class="{'navbar-active': $route.path === '/login'}"><router-link to="/login">Login</router-link></div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'navbar',
  data: function () {
    return {
      routes: [
        {name: 'Tasks', to: '/tasks'},
        {name: 'Team', to: '/team'},
        {name: 'Archive', to: '/archive'}
      ]
    }
  },

  computed: {
    ...mapGetters(['isLoggedIn'])
  }
}
</script>

<style lang="less" scoped>
@import "../assets/styles.less";

/* navbar */
#navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  overflow: hidden;
  background-color: @color-dark;

  font-family: "Lucida Sans Typewriter", "Lucida Console", Monaco, "Bitstream Vera Sans Mono", monospace;
  box-shadow: 0 6px 15px 0 rgba(0, 0, 0, 0.35);
}

.navbar-left {
  float: left;
}

.navbar-right {
  float: right;
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
  font-size: 14pt;
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

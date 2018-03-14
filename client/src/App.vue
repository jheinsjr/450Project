<template>
  <div id="app">
    <div class="navbar">
      <div v-for="route in routes"
                   class="navbar-item"
                   :key="route.to"
                   :class="{active: $route.path === route.to}">
        <router-link :to="route.to">{{route.name}}</router-link>
      </div>
    </div>

    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      routes: [
        {name: 'login', to: '/login'},
        {name: 'tasks', to: '/tasks'}
      ]
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

h1, h2, h3, h4, h5, h6, body {
  margin: 0;
}

.navbar {
  overflow: hidden;
  background-color: #333;
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
  background-color: #111;
}

.active {
  background-color: #111;
}

.pane {
  border: 1px solid black;
  background: #999;
  border-radius: 2px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.pane-header {
  border-bottom: 1px solid black;
  padding: 10px;
}

.input {
  border: 1px solid black;
  border-radius: 2px;
  padding: 5px;
}

.btn {
  border: 1px solid black;
  border-radius: 2px;
  padding: 5px 10px 5px 10px;
  text-decoration: none;
}

.btn:hover {
  background: lightcyan;
}
</style>

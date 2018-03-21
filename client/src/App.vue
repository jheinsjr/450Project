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
</style>

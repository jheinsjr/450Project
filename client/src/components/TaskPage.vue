<template>
  <div>
    <h1>Tasks</h1>

    <ul>
      <li v-for="task in this.$store.state.tasks" :key="task.id">
        {{ task.name }}
      </li>
    </ul>

    <button @click="updateTasks()">Update</button>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: 'task-page',
  data: function () {
    return {
    }
  },

  methods: {
    ...mapActions({
      updateTasks: 'UPDATE_TASKS'
    })
  },

  created: function () {
    if (this.$store.getters.isLoggedIn) {
      this.updateTasks()
    } else {
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>

</style>

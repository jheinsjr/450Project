<template>
  <div style="margin-top: 70px">
    <h1>Tasks</h1>

    <ul>
      <li v-for="task in $store.state.tasks.taskList" :key="task.id">
        <task :task-name="task.name"/>
      </li>
    </ul>

    <button class="btn" @click="updateTasks()">Update</button>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'task-page',
  data () {
    return {
    }
  },

  methods: {
    ...mapActions({
      updateTasks: 'UPDATE_TASKS'
    })
  },

  computed: {
    ...mapGetters(['isLoggedIn'])
  },

  created () {
    if (this.isLoggedIn) {
      this.updateTasks()
    } else {
      // this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
</style>

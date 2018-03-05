<template>
  <div>
    <h1>Tasks</h1>

    <ul v-if="displayTasks">
      <li v-for="task in tasks" :key="task.id">
        {{ task.name }}
      </li>
    </ul>
    <div v-else>{{alternativeMessage}}</div>
  </div>
</template>

<script>
export default {
  name: 'task-page',
  data: function () {
    return {
      tasks: [],
      displayTasks: false,
      alternativeMessage: ''
    }
  },

  created: function () {
    let url = 'http://127.0.0.1:8080/api/get_tasks'
    this.axios.get(url)
      .then(response => {
        if (response.data.status === 'success') {
          this.tasks = response.data.tasks
          this.displayTasks = true
        } else {
          this.alternativeMessage = response.data.reason
          this.tasks = []
          this.displayTasks = false
        }
      }).catch(() => {
        this.alternativeMessage = 'Error connecting to server'
        this.tasks = []
        this.displayTasks = false
      })
  }
}
</script>

<style scoped>

</style>

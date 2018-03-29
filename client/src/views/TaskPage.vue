<template>
  <div style="margin-top: 70px">
    <h1>Tasks</h1>

    <div class="task-pane">
      <task
      v-for="task in $store.state.tasks.taskList"
      :key="task.id"
      :task-name="task.name"/>
    </div>

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

<style lang="less" scoped>
.task-pane {
  width: 300px;
  background-color: gray;
}
</style>

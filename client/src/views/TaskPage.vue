<template>
  <!--
  Maybe just a general purpose task create and view page.
  -->

  <div id="task-page">
    <h1>Tasks</h1>

    <div class="task-pane">
      <task
      v-for="task in taskList"
      :key="task.id"
      :task="task"/>
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
      taskList: [
        {id: 1, status: 'In Progress', name: 'Task 1', date: new Date('8/13/2018')},
        {id: 2, status: 'Complete', name: 'Task 2', date: new Date('October 13, 2018')},
        {id: 3, status: 'In Progress', name: 'Task 3', date: new Date('October 13, 2018')},
        {id: 4, status: 'Complete', name: 'Task 4', date: new Date('October 13, 2018')},
        {id: 5, status: 'In Progress', name: 'Task 5', date: new Date('October 13, 2018')},
        {id: 6, status: 'In Progress', name: 'Task 6', date: new Date('October 13, 2018')},
        {id: 7, status: 'Complete', name: 'Task 7', date: new Date('October 13, 2018')},
        {id: 8, status: 'In Progress', name: 'Task 8', date: new Date('October 13, 2018')},
        {id: 9, status: 'Complete', name: 'Task 9', date: new Date('October 13, 2018')},
        {id: 10, status: 'In Progress', name: 'Task 10', date: new Date('October 13, 2018')}
      ]
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
  #task-page {
    margin-top: 70px;
  }

  .task-pane {
    margin: auto;
    width: 300px;
    height: 300px;
    overflow-y: scroll;
    border: solid 1px black;
  }
</style>

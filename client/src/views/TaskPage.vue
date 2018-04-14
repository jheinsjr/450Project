<template>
  <!--
  Maybe just a general purpose task create and view page.
  -->

  <div id="task-page">
    <h1>Tasks</h1>
    <task-list :task-list="taskList" />
    <button class="btn" @click="updateTasks()">Update</button>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
import dummy_data from '../util/dummy_tasks'

export default {
  name: 'task-page',
  data () {
    return {
      taskList: dummy_data
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
</style>

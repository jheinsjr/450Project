<template>
  <div id="archive-page">
    <task-list
      :task-list="taskList"
      :controls="false"
      :archive="true"
    />
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'
  import Task from '../util/task'


  export default {
    name: "ArchivePage",

    data() {
      return {
        taskList: []
      }
    },

    created () {
      if (!this.isLoggedIn) {
        this.$router.push('/welcome')
      } else {
        this.updateTasks()
      }
    },

    methods: {
      async updateTasks () {
        const response = await this.axios.get('tasks')

        if (response.data.status === 'success') {
          this.taskList = response.data.tasks.map(x => new Task(x))
        }
      }
    },

    computed: {
      ...mapGetters(['isLoggedIn'])
    }
  }
</script>

<style lang="less" scoped>

  #archive-page {
    margin-top: 70px;
  }

</style>

<template>
  <!--
  Maybe just a general purpose task create and view page.
  -->

  <div id="task-page">
    <task-list :task-list="taskList" @spawn-edit="spawnEdit" />
    <!--<button class="btn" @click="updateTasks()">Update</button>-->
    <transition name="fade">
      <div class="edit-overlay" v-if="editing !== null">
        <task-edit @submit-edit="submitEdit" @cancel-edit="cancelEdit" :task="editing" pane-title="Task Edit"/>
      </div>
    </transition>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
import dummy_data from '../util/dummy_tasks'

export default {
  name: 'task-page',
  data () {
    return {
      taskList: dummy_data,
      editing: null
    }
  },

  methods: {
    ...mapActions({
      updateTasks: 'UPDATE_TASKS'
    }),

    spawnEdit (task) {
      this.editing = task.clone()
    },

    submitEdit(task) {
      alert(`Submitting task: ${task.id}`)
      this.editing = null
    },

    cancelEdit () {
      this.editing = null
    }
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

  .edit-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background-color: rgba(0, 0, 0, 0.6);
  }

  .fade-enter-active, .fade-leave-active {
    transition: all 0.3s ease;
    opacity: 100%;
  }
  /* .expand-enter defines the starting state for entering */
  /* .expand-leave defines the ending state for leaving */
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
</style>

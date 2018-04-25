<template>
  <div id="task-pane">
    <div id="pane-header">
      <h1>Tasks</h1>
      <button id="task-create-btn" class="btn primary" v-if="showTaskCreate" @click="$emit('spawn-create')">Create Task</button>
    </div>
    <div class="control">
      Filter:
      <input type="text" class="input" v-model="filterBy">

      Sort by:
      <select title="sortBy" v-model="sortBy">
        <option value="title">Name</option>
        <option value="creationDate">Date</option>
      </select>
    </div>

    <div id="list-area">
      <task
        v-for="task in sortedList"
        :key="task.id"
        :task="task"
        :show-admin="true"
        :expand="selectedId === task.id"
        @selected="setSelection(task.id)"
      />
    </div>
  </div>
</template>

<script>
import sorting from '../util/sorting'

export default {
  name: 'TaskList',
  props: [
    'taskList',
    'showTaskCreate'
  ],

  data () {
    return {
      sortBy: 'title',
      filterBy: '',
      selectedId: -1
    }
  },

  methods: {
    setSelection (id) {
      this.selectedId = (this.selectedId === id) ? -1 : id
    }
  },

  computed: {
    filteredList () {
      const fb = this.filterBy.toLowerCase()
      return this.taskList.filter(t => t.title.toLowerCase().startsWith(fb))
    },

    sortedList () {
      let taskCopy = this.filteredList.slice() // make a copy
      taskCopy.sort(sorting.compareValues(this.sortBy))
      return taskCopy
    }
  }
}
</script>

<style lang="less" scoped>
  @import "../assets/styles.less";

  h1 {
    margin: 10px;
  }

  #pane-header {
    position: relative;
  }

  #task-pane {
    .pane;
    margin: auto;
    width: 80%;
  }

  #task-create-btn {
    position: absolute;
    top: 0;
    right: 7px;
  }

  .control {
    margin: 20px;
  }

  #list-area {
    height: 100%;
    overflow-y: auto;
  }
</style>

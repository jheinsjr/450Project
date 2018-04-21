<template>
  <div class="task-pane">
    <div class="pane-header"><h1>Tasks</h1></div>
    <div class="control">
      Filter:
      <input type="text" v-model="filterBy">

      Sort by:
      <select title="sortBy" v-model="sortBy">
        <option value="title">Name</option>
        <option value="creationDate">Date</option>
      </select>
    </div>

    <div class="list-area">
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
  props: ['taskList'],

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

  .title {
    padding: 10px;
    font-size: 22pt;
    border-bottom: 1px solid black;
  }

  .control {
    margin: 20px;
  }

  .list-area {
    height: 100%;
    overflow-y: auto;
  }

  .task-pane {
    .pane;
    margin: auto;
    width: 80%;
  }

</style>

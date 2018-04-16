<template>
  <div class="task-pane">
    <div>Tasks</div>
    Sort by:
    <select title="sortBy" v-model="sortBy">
      <option value="title">Name</option>
      <option value="creationDate">Date</option>
    </select>

    <div class="list-area">
      <task
        v-for="task in sortedList"
        :key="task.id"
        :task="task"
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
      selectedId: -1
    }
  },

  methods: {
    setSelection (id) {
      this.selectedId = (this.selectedId === id) ? -1 : id
    }
  },

  computed: {
    sortedList () {
      let taskCopy = this.taskList.slice() // make a copy
      taskCopy.sort(sorting.compareValues(this.sortBy))
      return taskCopy
    }
  }
}
</script>

<style lang="less" scoped>
  @import "../assets/styles.less";

  .list-area {

  }

  .task-pane {
    .pane;
    margin: auto;
    width: 80%;
    height: 300px;
    overflow-y: auto;
  }

</style>

<template>
  <div id="task-pane">
    <div id="pane-header">
      <h1>Tasks</h1>
      <button id="task-create-btn" class="btn primary" v-if="controls && $store.state.login.isAdmin"
              @click="$emit('spawn-create')"
      >Create Task</button>
    </div>
    <div class="control">
      Filter:
      <input type="text" class="input" v-model="filterBy">

      Sort by:
      <select title="sortBy" v-model="sortBy">
        <option value="name">Name</option>
        <option value="date">Date</option>
        <option value="author">Author</option>
        <option value="status">Status</option>
      </select>

      Order:
      <select title="order" v-model="sortOrder">
        <option value="asc">Asc</option>
        <option value="desc">Desc</option>
      </select>
    </div>

    <div id="list-area">
      <task
        v-for="task in sortedList"
        :key="task.id"
        :task="task"
        :show-admin="$store.state.login.isAdmin"
        :expand="selectedId === task.id"
        :controls="controls"
        @selected="setSelection(task.id)"
        @refresh="$emit('refresh')"
      />
    </div>
  </div>
</template>

<script>
import sorting from '../util/sorting'

const sortingFunctions = {
  'name': x => x.title,
  'date': x => x.creationDate,
  'author': x => x.createdBy.name,
  'status': x => x.status
};

export default {
  name: 'TaskList',
  props: [
    'taskList',
    'controls',
    'archive'
  ],

  data () {
    return {
      sortBy: 'name',
      sortOrder: 'asc',
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
      return this.taskList.filter(t =>
        t.title.toLowerCase().startsWith(fb) &&
        this.archive === (t.status === 'Completed')
      )
    },

    sortedList () {
      let taskCopy = this.filteredList.slice() // make a copy
      taskCopy.sort(sorting.compareValues(sortingFunctions[this.sortBy], this.sortOrder))
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

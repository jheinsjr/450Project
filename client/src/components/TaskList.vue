<template>
  <div class="task-pane">
    <task
      v-for="task in taskList"
      :key="task.id"
      :task="task"/>
  </div>
</template>

<script>
export default {
  name: 'TaskList',
  props: ['taskList']
}
</script>

<style lang="less" scoped>

  .task-pane {
    margin: auto;
    width: 300px;
    height: 300px;
    overflow-y: scroll;
    border: solid 1px black;
  }

</style>

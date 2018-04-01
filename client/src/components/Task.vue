<template>
  <div class="task">
    <span class="task-title">{{task.name}}</span>
    <span class="task-date">{{formatDate(task.date)}}</span>
  </div>
</template>

<script>
export default {
  name: 'task',
  props: [
    'task'
  ],

  methods: {
    formatDate (date) {
      return date.getDay() + '/' + date.getMonth() + '/' + date.getFullYear()
    }
  }
}
</script>

<style lang="less" scoped>
  @import "../assets/styles.less";

  @border-color: rgb(147, 155, 146);

  .task {
    text-align: left;
    border-right: solid 1px @border-color;
    height: 40px;
  }

  .task:not(:last-child) {
    border-bottom: solid 1px @border-color;
  }

  .task-title {
    margin: 4px;
    font-weight: bold;
  }

  .task-date {
    margin: 4px;
    float: right;
  }

</style>

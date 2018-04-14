<template>
  <div class="task">
    <div class="task-title" @click="$emit('selected')">{{task.title}}</div>
    <span class="task-status">Status: {{task.status}}</span>
    <span class="task-date">{{formatDate(task.creationDate)}}</span>

    <transition name="expand">
      <div v-if="expand" class="extra">
        Esdfasdf
        asdfasdf
        asdfasdfasd
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'task',

  props: [
    'task',
    'expand'
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
    padding: 5px;
  }

  .task:not(:last-child) {
    border-bottom: solid 1px @border-color;
  }

  .task-title {
    font-weight: bold;
  }

  .task-date {
    float: right;
  }

  .task-status {
    margin-left: 5px;
  }

  .extra {
    height: 80px;
  }

  /* always present */
  .expand-enter-active, .expand-leave-active {
    transition: all 0.3s ease;
    height: 80px;
    overflow: hidden;
  }
  /* .expand-enter defines the starting state for entering */
  /* .expand-leave defines the ending state for leaving */
  .expand-enter, .expand-leave-to {
    height: 0;
    opacity: 0;
  }
</style>

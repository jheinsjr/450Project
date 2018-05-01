<template>
  <div class="task">
    <div class="main-content">
      <div>
        <div class="title" @click="$emit('selected')">{{task.title}}</div>
        <div class="date">Created On: {{formatDate(task.creationDate)}}</div>
        <div class="author">Author: {{task.createdBy.name}}</div>
      </div>
      <div class="status">Status: {{task.status}}</div>
    </div>

    <transition name="expand">
      <div v-if="expand" class="expanded-content">
        <div class="description">{{task.description}}</div>
        <div class="controls">
          <button class="btn success join-task" @click="setStatus">Join Task</button>
          <button v-if="showAdmin" @click="$parent.$emit('spawn-edit', task)" class="btn primary edit-task">Edit Task</button>
          <button v-if="showAdmin" class="btn danger" @click="removeTask">Delete</button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'task',

  props: [
    'task',
    'expand',
    'showAdmin'
  ],

  methods: {
    formatDate (date) {
      return date.getDay() + '/' + date.getMonth() + '/' + date.getFullYear()
    },

    async removeTask () {
      await this.axios.delete(`task/${this.task.id}`)
      this.$emit("refresh")
    },

    async setStatus () {
      await this.axios.post(`status/${this.task.id}`, {'status_id': 2})
      this.$emit("refresh")
    }
  }
}
</script>

<style lang="less" scoped>
  @import "../assets/styles.less";

  @border-color: rgb(147, 155, 146);

  .task {
    text-align: left;
  }

  .task:not(:last-child) {
    border-bottom: solid 1px @border-color;
  }

  .main-content {
    margin: 10px;
  }

  .title {
    display: inline;
    font-weight: bold;
    cursor: pointer;
  }

  .author {
    display: inline;
    float: right;
    margin-right: 20px;
  }

  .date {
    display: inline;
    float: right;
  }

  .status {
    display: inline;
    margin-left: 5px;
  }

  .description {
    display: inline-block;
  }

  .expanded-content {
    height: 80px;
    margin: 5px 10px 10px 10px;
  }

  .controls {

  }

  /* Animations */
  .expand-enter-active, .expand-leave-active {
    transition: all 0.3s ease;
    height: 80px;
    overflow: hidden;
  }
  /* .expand-enter defines the starting state for entering */
  /* .expand-leave defines the ending state for leaving */
  .expand-enter, .expand-leave-to {
    height: 0;
    margin: 0;
    opacity: 0;
  }
</style>

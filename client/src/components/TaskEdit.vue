<template>
  <div class="edit-pane">
    <div class="close-icon" @click="$emit('cancel-edit')">
      <font-awesome-icon class="icon" icon="times"/>
    </div>
    <div class="pane-header"><h3>{{paneTitle}}</h3></div>

    <div class="input-grid">
      <label for="title" id="title-label">Title:</label>
      <input id="title" v-model="task.title" class="input" type="text">

      <label for="description" id="description-label">Description:</label>
      <textarea id="description" v-model="task.description" class="input"></textarea>
    </div>
    <button id="cancel-btn" class="btn danger" @click="$emit('cancel-edit')">Cancel</button>
    <button id="save-btn" class="btn success" @click="$emit('submit-edit', task)">Save</button>
  </div>
</template>

<script>
export default {
  name: 'TaskEdit',
  props: [
    'pane-title',
    'task'
  ]
}
</script>

<style lang="less" scoped>
  @import "../assets/styles.less";

  #save-btn {

  }

  .edit-pane {
    .pane;
    margin-top: 150px;
    margin-left: auto;
    margin-right: auto;

    width: 500px;
    height: 300px;
  }

  .close-icon {
    cursor: pointer;
    float: right;
    width: 25px;
    height: 25px;
    background-color: #e3e3e3;
  }

  .close-icon:hover {
    background-color: #cccccc;
  }

  .icon {
    margin: 5px;
  }
</style>

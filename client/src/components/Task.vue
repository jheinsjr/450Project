<template>
  <div class="task">
    {{taskName}}
  </div>
</template>

<script>
export default {
  name: 'task',
  props: {
    taskName: String
  }
}
</script>

<style lang="less" scoped>
@import "../assets/styles.less";

.task {
  display: inline;
  background-color: red;
}



</style>

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

<style scoped>
.task {
  display: inline;
}
</style>

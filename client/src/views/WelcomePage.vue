<template>
  <!--
  This is the first page some sees when they come to the site before they login.
  Maybe just a link to the login and the name of the project.
  -->

  <div id="welcome">
    <div>Welcome to BRADMAN.</div>
    <div>Please login to get started</div>
  </div>
</template>

<script>
  export default {
    name: "WelcomePage"
  }
</script>

<style lang="less" scoped>
  #welcome {
    margin-top: 300px;
  }
</style>

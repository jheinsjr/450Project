<template>
  <div></div>
</template>

<script>
export default {
  name: 'LogoutPage',
  created () {
    this.$store.dispatch('LOGOUT').then(
      () => this.$router.push('/welcome')
    )
  }
}
</script>

<style scoped>

</style>

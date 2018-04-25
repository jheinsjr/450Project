<template>
  <div></div>
</template>

<script>
export default {
  name: 'LogoutPage',
  async created () {
    await this.$store.dispatch('LOGOUT')
    this.$router.push('/welcome')
  }
}
</script>

<style scoped>

</style>

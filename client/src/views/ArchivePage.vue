<template>
  <div id="archive-page">
    Archive
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "ArchivePage",

    created () {
      if (!this.isLoggedIn) {
        this.router.push('/welcome')
      }
    },

    computed: {
      ...mapGetters(['isLoggedIn'])
    }
  }
</script>

<style scoped>

</style>

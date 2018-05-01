<template>
  <div id="team-page">
    <div id="team-pane" class="pane">
      <div id="team-list" v-for="t in team" :key="t">
        <div>{{t}}</div>
      </div>
    </div>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "TeamPage",

    data() {
      return {
        team: ['One', 'Two', 'Three']
      }
    },

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

<style lang="less" scoped>
  @import "../assets/styles.less";

  #team-pane {
    margin: 150px auto auto auto;
    width: 300px;
  }
</style>

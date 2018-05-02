<template>
  <div id="team-page">
    <div id="team-pane" class="pane">
      <div id="team-list" v-for="t in team" :key="t.id">
        <div>{{t.name}}</div>
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
        team: []
      }
    },

    methods: {
      async updateTeam () {
        try {
          const response = await this.axios.get('team')
          const data = response.data
          if (data.status === 'success') {
            this.team = data.team
          } else {
            this.router.push('/logout')
          }
        } catch (err) {
          alert('Server Error.')
        }
      }
    },

    created () {
      if (!this.isLoggedIn) {
        this.$router.push('/welcome')
      } else {
        this.updateTeam()
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

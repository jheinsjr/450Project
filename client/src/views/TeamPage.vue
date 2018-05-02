<template>
  <div id="team-page">
    <div id="team-pane" class="pane">
      <div class="pane-header">
        <h2>Team</h2>
      </div>

      <table id="team-list">
        <tr>
          <th>Name</th>
          <th>Username</th>
          <th>Admin</th>
        </tr>
        <tr v-for="t in team" :key="t.id">
          <td>{{t.name}}</td>
          <td>{{t.username}}</td>
          <td><font-awesome-icon :icon="iconFor(t.admin)" /></td>
        </tr>
      </table>
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
      },

      iconFor (adminId) {
        if (adminId === '0'){
          return ['far', 'square']
        }
        return ['far', 'check-square']
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
    width: 600px;
  }

  #team-list {
    text-align: left;
    margin: 5px;
  }

  th, td {
    padding: 5px;
  }
</style>

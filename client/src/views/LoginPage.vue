<template>
  <div class="login-pane pane">
    <div class="pane-header">
      <h2>Login</h2>
    </div>
    <div class="input-grid">
      <label for="username-input">Login:</label>
      <input
        v-model="username"
        id="username-input"
        type="text"
        class="input"
        @keyup.enter="login">

      <label for="password-input">Password:</label>
      <input
        v-model="password"
        id="password-input"
        type="password"
        class="input"
        @keyup.enter="login">
    </div>
    <div>
      <button class="btn" @click="login">login</button>
    </div>
    <div>
      <router-link to="/create_account">Don't have an account?</router-link>
    </div>
    <div class="error">{{ $store.state.login.errorMsg }}</div>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'LoginPage',

  data () {
    return {
      username: '',
      password: ''
    }
  },

  methods: {
    ...mapActions({loginAction: 'LOGIN'}),

    login () {
      let data = {'username': this.username, 'password': this.password}
      this.loginAction(data)
    }
  },

  computed: {
    ...mapGetters(['isLoggedIn'])
  },

  watch: {
    isLoggedIn (newValue) {
      if (newValue) {
        this.$router.push('tasks')
      }
    }
  }
}
</script>

<style lang="less" scoped>
.login-pane {
  margin: 100px auto auto auto;
  width: min-content;
  padding-bottom: 20px;
}

.input-grid {
  display: grid;
  grid-gap: 5px;
  grid-template-columns: 1fr 250px;
  align-items: center;
  padding: 20px 20px 5px 20px;
}

.input-grid label {
  text-align: right;
}

.error {
  color: red;
}
</style>

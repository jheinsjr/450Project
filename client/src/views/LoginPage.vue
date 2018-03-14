<template>
  <div class="login-pane pane">
    <div class="pane-header">
      <h2>Login</h2>
    </div>
    <div class="input-grid">
      <label for="username-input">Login:</label>
      <input id="username-input" type="text" v-model="username" class="input" @keyup.enter="login">

      <label for="password-input">Password:</label>
      <input id="password-input" type="password" v-model="password" class="input" @keyup.enter="login">

      <div>
        <button class="btn" @click="login">login</button>
      </div>
    </div>

    <div class="error">{{$store.state.login.errorMsg}}</div>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'login-page',

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

  watch: {
    isLoggedIn (newValue) {
      if (newValue) {
        this.$router.push('tasks')
      }
    }
  },

  computed: {
    ...mapGetters(['isLoggedIn'])
  }
}
</script>

<style scoped>
.login-pane {
  margin: 50px auto auto auto;
  width: 400px;
}

.input-grid {
  display: grid;
  grid-gap: 5px;
  grid-template-columns: 1fr 2fr;
  align-items: center;
  margin: 15px;
}

.input-grid label {
  text-align: right;
}

.error {
  color: red;
}
</style>

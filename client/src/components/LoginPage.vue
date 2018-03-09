<template>
  <div class="login-pane">
    <h1>Login</h1>

    <label for="username-input">Login:</label>
    <input id="username-input" type="text" v-model="username" @keyup.enter="login" :class="{ 'input-error': usernameMsg.length !== 0 }">
    <div>{{usernameMsg}}</div>

    <label for="password-input">Password:</label>
    <input id="password-input" type="password" v-model="password" @keyup.enter="login" :class="{ 'input-error': passwordMsg.length !== 0 }">
    <div>{{passwordMsg}}</div>

    <div>
      <button @click="login">login</button>
    </div>

    <!-- <router-link v-if="success" to="/tasks">View Tasks</router-link> -->
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'login-page',

  data: function () {
    return {
      username: '',
      password: '',
      runOnce: false
    }
  },

  methods: {
    ...mapActions({loginAction: 'LOGIN'}),

    login: function () {
      if (this.validate()) {
        let data = {'username': this.username, 'password': this.password}
        this.loginAction(data)
      }
    },

    validate: function () {
      this.runOnce = true
      return this.usernameMsg.length === 0 && this.passwordMsg.length === 0
    }
  },

  watch: {
    isLoggedIn: function (newValue) {
      if (newValue) {
        this.$router.push('tasks')
      }
    }
  },

  computed: {
    ...mapGetters(['isLoggedIn']),

    usernameMsg: function () {
      if (this.runOnce && this.username.length === 0) {
        return 'Please enter a valid username.'
      } else {
        return ''
      }
    },
    passwordMsg: function () {
      if (this.runOnce && this.password.length === 0) {
        return 'Please enter a valid password.'
      } else {
        return ''
      }
    }
  }
}
</script>

<style scoped>
.input-error {
  border: 1px solid red;
}

.login-pane {
  display: grid;
  width: 400px;
}
</style>

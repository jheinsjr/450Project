<template>
  <div class="login-pane">
    <h1>Login</h1>

    <label for="username-input">Login:</label>
    <input id="username-input" type="text" v-model="username" :class="{ 'input-error': usernameMsg.length !== 0 }">
    <div>{{usernameMsg}}</div>

    <label for="password-input">Password:</label>
    <input id="password-input" type="password" v-model="password" :class="{ 'input-error': passwordMsg.length !== 0 }">
    <div>{{passwordMsg}}</div>

    <div>
      <button @click="loggin">login</button>
    </div>

    <div>{{generalMsg}}</div>

    <router-link v-if="success" to="/tasks">View Tasks</router-link>
  </div>
</template>

<script>
export default {
  name: 'login-page',

  data: function () {
    return {
      username: '',
      password: '',
      success: false,
      generalMsg: '',
      runOnce: false
    }
  },

  methods: {
    loggin: function () {
      if (this.validate()) {
        let url = 'http://127.0.0.1:8080/api/login'
        let data = {'username': this.username, 'password': this.password}
        this.axios.post(url, data)
          .then(response => {
            if (response.data.status === 'success') {
              this.success = true
              this.generalMsg = `You logged in as ${data.username}`
            } else {
              this.generalMsg = response.reason
              this.success = false
            }
          })
          .catch(function (reason) {
            this.generalMsg = 'server error'
            this.success = false
          }).finally(() => {
            this.runOnce = true
          })
      }
    },

    validate: function () {
      this.runOnce = true
      return this.usernameMsg.length === 0 && this.passwordMsg.length === 0
    }
  },

  computed: {
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

<template>
  <div>
    <div class="pane account-pane">
      <div class="pane-header">
        <h2>
          Create Account
        </h2>
      </div>

      <div class="input-grid">
        <label for="firstName">First Name: </label>
        <input v-model="firstName" type="text" id="firstName" class="input" :class="{ error: errors.firstName }">

        <label for="lastName">Last Name: </label>
        <input v-model="lastName" type="text" id="lastName" class="input" :class="{ error: errors.lastName }">

        <label for="username">Account Name: </label>
        <input v-model="username" type="text" id="username" class="input" :class="{ error: errors.username }">

        <label for="password">Password</label>
        <input v-model="passwordA" type="password" id="password" class="input" :class="{ error: errors.passwordA }">

        <label for="passwordConfirm">Retype Password</label>
        <input v-model="passwordB" type="password" id="passwordConfirm" class="input" :class="{ error: errors.passwordB }">
      </div>

      <div>
        <button @click="create_account()" class="btn primary">Create Account</button>
      </div>

      <div>
        <router-link to="/login">Already have an account?</router-link>
      </div>

      <div v-for="error in errors.messages" :key="error" class="error">{{error}}</div>

    </div>
  </div>
</template>

<script>
import validation from '../util/validation'

export default {
  name: 'create-account-page',

  data: function () {
    return {
      firstName: '',
      lastName: '',
      username: '',
      passwordA: '',
      passwordB: '',
      errors: {messages: [], stop: true}
    }
  },

  methods: {
    async create_account () {
      this.errors = this.validate()

      if (!this.errors.stop) {
        try {
          const { data } = await this.axios.post('create_account',
            {
              'firstName': this.firstName,
              'lastName': this.lastName,
              'username': this.username,
              'password': this.passwordA
            })

          if (data.status === 'success') {
            this.$router.push('/login')
          } else {
            this.errors = { messages: data.message, stop: false }
          }
        } catch (e) {
          alert("Error connecting to server.")
        }
      }
    },

    validate () {
      let errors = { messages: [], stop: false }

      if (validation.validateEmpty(this.firstName)) {
        errors.firstName = true
        errors.stop = true
      }

      if (validation.validateEmpty(this.lastName)) {
        errors.lastName = true
        errors.stop = true
      }

      if (validation.validateUsername(this.username)) {
        errors.username = true
        errors.stop = true
      }

      if (validation.validatePassword(this.passwordA)) {
        errors.passwordA = true
        errors.stop = true
      } else if (this.passwordA !== this.passwordB) {
        errors.passwordB = true
        errors.stop = true
      }

      return errors
    }
  }
}
</script>

<style lang="less" scoped>
  @import "../assets/styles.less";

  .account-pane {
    margin: 100px auto auto auto;
    padding-bottom: 25px;
    width: 450px;
  }

</style>

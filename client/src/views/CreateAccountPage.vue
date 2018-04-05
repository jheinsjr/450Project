<template>
  <div>
    <div class="pane account-pane">
      <div class="pane-header">
        <h2>
          Create Account
        </h2>
      </div>

      <div class="input-grid">
        <label for="name">Account Name: </label>
        <input v-model="username" type="text" id="name" class="input">

        <label for="password">Password</label>
        <input v-model="passwordA" type="password" id="password" class="input">

        <label for="passwordConfirm">Retype Password</label>
        <input v-model="passwordB" type="password" id="passwordConfirm" class="input">
      </div>

      <div>
        <button @click="create_account()" class="btn">Create Account</button>
      </div>

      <div>
        <router-link to="/login">Already have an account?</router-link>
      </div>

      <div v-for="error in errorList" :key="error" class="error">{{error}}</div>

    </div>
  </div>
</template>

<script>
import validation from '../util/validation'

export default {
  name: 'create-account-page',

  data: function () {
    return {
      username: '',
      passwordA: '',
      passwordB: '',
      errorList: []
    }
  },

  methods: {
    async create_account () {
      this.errorList = this.validate()

      if (this.errorList.length === 0) {
          const { data } = await this.axios.post('create_account', { 'username': this.username, 'password': this.passwordA})

          if (data['status'] === 'success') {
            this.$router.push('/login')
          } else {
            this.errorList = [data.message]
          }
      }
    },

    validate () {
      let errors = []


      if (validation.validateUsername(this.username)) {
        errors.push('Username dosn\'t validate.')
      }

      if (validation.validatePassword(this.passwordA)) {
        errors.push('Password dosn\'t validate.')
      } else if (this.passwordA !== this.passwordB) {
        errors.push('Passwords must match')
      }

      return errors
    }
  }
}
</script>

<style lang="less" scoped>
  @import "../assets/styles.less";

  .account-pane {
    margin: 150px auto auto auto;
    padding-bottom: 25px;
    width: 450px;
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
</style>

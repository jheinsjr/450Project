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
    create_account () {
      this.errorList = this.validate()
    },

    validate () {
      let errors = []

      if (this.username.length === 0) {
        errors.push('Username can not be blank')
      }

      if (this.passwordA.length === 0) {
        errors.push('Password can not be black')
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

<template>
  <div>
    <div class="pane account-pane">
      <div class="pane-header">
        <h2>
          New Account
        </h2>
      </div>

      <div class="input-grid">
        <label for="name">Account Name: </label>
        <input type="text" id="name" class="input">

        <label for="password">Password</label>
        <input type="password" id="password" class="input">

        <label for="passwordConfirm">Retype Password</label>
        <input type="password" id="passwordConfirm" class="input">

        <button class="btn">Create Account</button>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'create-account-page'
}
</script>

<style scoped>
  .account-pane {
    margin: 50px auto auto auto;
    width: 450px;
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
</style>

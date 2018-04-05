const usernameRegex = /^[a-z][a-z0-9]*$/i
const passwordRegex = /^[a-z0-9]+$/i

export default {
  validateUsername (username) {
    return !usernameRegex.test(username)
  },

  validatePassword (password) {
    return !passwordRegex.test(password)
  }
}

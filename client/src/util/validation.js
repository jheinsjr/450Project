const usernameRegex = /^[a-z][a-z0-9!@#$%^&*]{5,11}$/i
const passwordRegex = /^[a-z0-9!@#$%^&*]{6,}$/i
const nonEmptyRegex = /^.*\S.*$/

export default {
  validateUsername (username) {
    return !usernameRegex.test(username)
  },

  validatePassword (password) {
    return !passwordRegex.test(password)
  },

  validateEmpty (something) {
    return !nonEmptyRegex.test(something)
  }
}

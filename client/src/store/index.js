import Vue from 'vue'
import Vuex from 'vuex'

// This is admittedly complex, it's all about application state.
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login: {
      username: '',
      isAdmin: false,
      errorMsg: ''
    },
    tasks: {
      taskList: [],
      errorMsg: ''
    }
  },

  getters: {
    isLoggedIn (state) {
      return state.login.username.length !== 0
    }
  },

  mutations: {
    LOGIN_SUCCESS (state, username) {
      state.login.username = username
      state.login.errorMsg = ''
    },
    LOGIN_FAILED (state, response) {
      state.login.username = ''
      state.login.errorMsg = response
    },
    LOGOUT_SUCCESS (state) {
      state.login.username = ''
      state.login.errorMsg = ''
    },
    TASK_UPDATE (state, {tasks}) {
      state.tasks.taskList = tasks
      state.tasks.errorMsg = ''
    },
    TASK_UPDATE_FAILED (state, response) {
      state.tasks.taskList = []
      state.tasks.errorMsg = response
    }
  },
  actions: {
    async LOGIN ({commit}, data) {
      const response = await Vue.axios.post('login', data)

      if (response.data.status === 'success') {
        commit('LOGIN_SUCCESS', data.username)
      } else {
        commit('LOGIN_FAILED', response.data.message)
      }
    },
    async LOGOUT ({commit}) {
      await Vue.axios.get('logout')

      commit('LOGOUT_SUCCESS')
    },
    async UPDATE_TASKS ({commit}) {
      const response = await Vue.axios.get('tasks')

      if (response.data.status === 'success') {
        commit('TASK_UPDATE', response.data)
      } else {
        commit('TASK_UPDATE_FAILED', response.data.message)
      }
    }
  },
  strict: true
})

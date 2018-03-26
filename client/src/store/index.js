import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login: {
      username: '',
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
    LOGIN_SUCCESS (state, {username}) {
      state.login.username = username
      state.login.errorMsg = ''
    },
    LOGIN_FAILED (state, response) {
      state.login.username = ''
      state.login.errorMsg = response
    },
    TASK_UPDATE (state, {tasks}) {
      state.tasks.taskList = tasks
      state.tasks.errorMsg = ''
    },
    TASK_UPDATE_FAILED (state, response) {
      state.tasks = []
      state.tasks.errorMsg = response
    }
  },
  actions: {
    LOGIN ({commit}, data) {
      api.login(data,
        () => commit('LOGIN_SUCCESS', data),
        (response) => commit('LOGIN_FAILED', response)
      )
    },
    UPDATE_TASKS ({commit}) {
      api.get_tasks({},
        (response) => commit('TASK_UPDATE', response),
        (response) => commit('TASK_UPDATE_FAILED', response)
      )
    }
  }
})

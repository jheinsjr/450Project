import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: '',
    tasks: []
  },

  getters: {
    isLoggedIn: state => {
      return state.username.length !== 0
    }
  },

  mutations: {
    LOGIN_SUCCESS (state, {username}) {
      state.username = username
    },
    LOGIN_FAILED (state) {
      state.username = ''
    },
    TASK_UPDATE (state, {tasks}) {
      state.tasks = tasks
    },
    TASK_UPDATE_FAILED (state) {
      state.tasks = []
    }
  },
  actions: {
    LOGIN ({commit, state}, data) {
      api.login(data,
        () => commit('LOGIN_SUCCESS', data),
        () => commit('LOGIN_FAILED')
      )
    },
    UPDATE_TASKS ({commit, state}, data) {
      api.get_tasks({},
        (response) => commit('TASK_UPDATE', response),
        (response) => commit('TASK_UPDATE_FAILED', response)
      )
    }
  }
})

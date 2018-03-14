import Vue from 'vue'
import Router from 'vue-router'
import LoginPage from '@/views/LoginPage'
import TaskPage from '@/views/TaskPage'
import CreateAccount from '@/views/CreateAccountPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginPage
    },
    {
      path: '/create_account',
      name: 'CreateAccount',
      component: CreateAccount
    },
    {
      path: '/tasks',
      name: 'Tasks',
      component: TaskPage
    }
  ]
})

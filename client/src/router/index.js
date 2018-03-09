import Vue from 'vue'
import Router from 'vue-router'
import LoginPage from '@/components/LoginPage'
import TaskPage from '@/components/TaskPage'

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
      path: '/tasks',
      name: 'Tasks',
      component: TaskPage
    }
  ]
})

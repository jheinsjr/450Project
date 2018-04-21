import Vue from 'vue'
import Router from 'vue-router'
import LoginPage from '../views/LoginPage'
import LogoutPage from '../views/LogoutPage'
import TaskPage from '../views/TaskPage'
import TeamPage from '../views/TeamPage'
import CreateAccount from '../views/CreateAccountPage'
import ArchivePage from '../views/ArchivePage'

//Setting up are urls
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
      path: '/logout',
      name: 'Logout',
      component: LogoutPage
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
    },
    {
      path: '/team',
      name: 'Team',
      component: TeamPage
    },
    {
      path: '/archive',
      name: 'Archive',
      component: ArchivePage
    }
  ]
})

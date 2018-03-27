// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
import store from './store'

import fontawesome from '@fortawesome/fontawesome'
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'
import { faSpinner } from '@fortawesome/fontawesome-free-solid'

import './assets/styles.less'

import App from './App'
import Task from './components/Task'
import Navbar from './components/Navbar'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)

//fa
fontawesome.library.add(faSpinner)

//components
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component('task', Task)
Vue.component('navbar', Navbar)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})

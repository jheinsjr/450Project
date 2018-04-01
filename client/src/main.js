// This code is automatically called at the start of the application
// Basically setting everything up.

import Vue from 'vue'
// Axios is for making requests to the server
import axios from 'axios'
import VueAxios from 'vue-axios'
// virtual routing
import router from './router'
// global application state
import store from './store'

// This assets/style.less file is the global css rules, importing it apples them everywhere
import './assets/styles.less'
// App is are root level component
import App from './App'
// Font Awesome setup
import Icons from './assets/icons'
// Register all the components for global use
import Components from './components'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)

// Initialize our other config files
Icons.init()
Components.init()

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})

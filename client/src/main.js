// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
import store from './store'

import './assets/styles.less'
import App from './App'
import Icons from './assets/icons'
import Components from './components'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)

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

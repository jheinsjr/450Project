import Vue from 'vue'
import fontawesome from '@fortawesome/fontawesome'
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'
// Import any icons you need here and add theme to the library down bellow
// Font awesome has a excellent support for Vuejs, check out the documentation
import { faSpinner } from '@fortawesome/fontawesome-free-solid'

export default{
  init () {
    fontawesome.library.add(faSpinner)
    Vue.component('font-awesome-icon', FontAwesomeIcon)
  }
}

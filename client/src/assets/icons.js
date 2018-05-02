import Vue from 'vue'
import fontawesome from '@fortawesome/fontawesome'
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'
// Import any icons you need here and add theme to the library down bellow
// Font awesome has a excellent support for Vuejs, check out the documentation
import { faTimes, faHome, faAddressBook, faHistory } from '@fortawesome/fontawesome-free-solid'
import { faSquare, faCheckSquare } from '@fortawesome/fontawesome-free-regular'

export default{
  init () {
    fontawesome.library.add(faTimes, faHome, faAddressBook, faHistory, faSquare, faCheckSquare)
    Vue.component('font-awesome-icon', FontAwesomeIcon)
  }
}

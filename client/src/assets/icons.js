import Vue from 'vue'
import fontawesome from '@fortawesome/fontawesome'
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'
import { faSpinner } from '@fortawesome/fontawesome-free-solid'

export default{
  init () {
    fontawesome.library.add(faSpinner)
    Vue.component('font-awesome-icon', FontAwesomeIcon)
  }
}

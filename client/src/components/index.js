import Vue from 'vue'
import Navbar from './Navbar'
import Task from './Task'
import TaskEdit from './TaskEdit'

export default {
  components: [
    Navbar,
    Task,
    TaskEdit
  ],

  init () {
    this.components.forEach(c => Vue.component(c.name, c))
  }
}

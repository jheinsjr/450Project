import Vue from 'vue'
import Navbar from './Navbar'
import Task from './Task'
import TaskEdit from './TaskEdit'
import TaskList from './TaskList'

export default {
  init () {
    // register the components so they can be used.
    Vue.component(Navbar.name, Navbar)
    Vue.component(Task.name, Task)
    Vue.component(TaskEdit.name, TaskEdit)
    Vue.component(TaskList.name, TaskList)
  }
}

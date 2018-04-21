
export default class Task {
  constructor(task) {
    this.id = task.id
    this.title = task.title
    this.description = task.description
    this.status = task.status
    this.creationDate = new Date(task.creationDate)
    this.updatedDate = (task.updatedDate === null)? null : new Date(task.updatedDate)
    this.createdBy = task.createdBy
    this.updatedBy = task.updatedBy
  }

  clone() {
    return new Task(this)
  }
}

const DEFAULT_STATUS = 'DEFAULT_STATUS'


export default class Task {
  constructor(task) {
    if (task === undefined) {
      this.id = -1
      this.title = ''
      this.description = ''
      this.status = DEFAULT_STATUS
      this.creationDate = Date.now()
      this.updatedDate = null
      this.createdBy = {id: -1, name: 'PERSON'}
      this.updatedBy = null
    } else {
      this.id = task.id
      this.title = task.title
      this.description = task.description
      this.status = task.status
      this.creationDate = new Date(task.creationDate)
      this.updatedDate = (task.updatedDate === null) ? null : new Date(task.updatedDate)
      this.createdBy = task.createdBy
      this.updatedBy = task.updatedBy
    }
  }

  clone() {
    return new Task(this)
  }
}

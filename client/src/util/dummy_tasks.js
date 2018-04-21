import Task from './task'

export default [
  new Task({
    id: 0,
    title: 'Finish UI Planing Doc',
    description: 'To give the other developers a clear idea of what their doing.',
    status: 'not-started',
    creationDate: new Date('2018-06-01'),
    updatedDate: null,
    createdBy: {id: 0, name: 'fred'},
    updatedBy: null
  }),
  new Task({
    id: 1,
    title: 'Polish Css',
    description: 'You know this drill.',
    status: 'started',
    creationDate: new Date('2018-01-02'),
    updatedDate: null,
    createdBy: {id: 1, name: 'bob'},
    updatedBy: null
  }),
  new Task({
    id: 2,
    title: 'Design Database Tables',
    description: 'You know this drill.',
    status: 'not-started',
    creationDate: new Date('2018-08-01'),
    updatedDate: null,
    createdBy: {id: 0, name: 'fred'},
    updatedBy: null
  })
]

from database.session import rest_api
from flask_restful import Resource, reqparse
from database.session import db
from database.tables import User

dummy_data = [
    {
        'id': 0,
        'title': 'Finish UI Planing Doc',
        'description': 'To give the other developers a clear idea of what their doing.',
        'status': 'not-started',
        'creationDate': '2018-06-01',
        'updatedDate': None,
        'createdBy': {'id': 0, 'name': 'fred'},
        'updatedBy': None
    },
    {
        'id': 1,
        'title': 'Polish Css',
        'description': 'You know this drill.',
        'status': 'started',
        'creationDate': '2018-01-02',
        'updatedDate': None,
        'createdBy': {'id': 1, 'name': 'bob'},
        'updatedBy': None
    },
    {
        'id': 2,
        'title': 'Design Database Tables',
        'description': 'You know this drill.',
        'status': 'not-started',
        'creationDate': '2018-08-01',
        'updatedDate': None,
        'createdBy': {'id': 0, 'name': 'fred'},
        'updatedBy': None
    }
]


def push_change(task):
    if task['id'] == -1:
        task['id'] = len(dummy_data)
    else:
        for i, t in enumerate(dummy_data):
            if t['id'] == task['id']:
                dummy_data[i] = task
                return

    dummy_data.append(task)


# The whole task list
class TaskList(Resource):
    def get(self):
        return {"status": "success", "tasks": dummy_data}


# An individual task
class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("task", type=dict)

    def post(self):
        args = self.parser.parse_args()

        push_change(args.task)

        return {"status": "success"}


rest_api.add_resource(TaskList, '/api/tasks')
rest_api.add_resource(Task, '/api/task')

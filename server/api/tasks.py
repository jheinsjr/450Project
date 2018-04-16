from database.session import rest_api
from flask_restful import Resource, reqparse
from database.tables import User

dummy_data = [
    {"id": 1, "status": 'In Progress', "name": 'Task 1', "date": '8/13/2018'}
]


class TaskList(Resource):
    def get(self):
        return {"status": "success", "tasks": dummy_data}


rest_api.add_resource(TaskList, '/api/task-list')

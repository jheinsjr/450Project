from database.session import rest_api
from flask_restful import Resource, reqparse, fields, marshal
from database.session import db
from sqlalchemy.exc import SQLAlchemyError

_task_fields = {
    'id': fields.Integer(attribute='Task_ID'),
    'title': fields.String(attribute='Title'),
    'description': fields.String(attribute='Description'),
    'status': fields.Integer(attribute='Status_ID'),
    'creationDate': fields.String(attribute='Creation_TS'),
    'updatedDate': fields.String(attribute='Update_DT'),
    'createdBy': {'id': fields.Integer(attribute='Created_by'), 'name': fields.String(attribute='First_Name')}
}


def push_change(task):
    if task['id'] == -1:
        db.engine.execute("""
        INSERT INTO Task
        (Title, Description, Status_ID, Creation_TS, Created_by)
        VALUES
        (:title, :description, 1, '2018-04-27 16:03:01', 1)
        """, task)
    else:
        db.engine.execute("""
        UPDATE Task SET
        Title = :title, Description = :description
        WHERE Task_ID = :id
        """, task)


# The whole task list
class TaskList(Resource):
    query = db.text("""
    SELECT * FROM Task JOIN Employee E on Task.Created_by = E.Employee_ID
    """)

    def get(self):
        task_list = db.engine.execute(self.query).fetchall()
        task_marshal = marshal(task_list, _task_fields)

        return {"status": "success", "tasks": task_marshal}


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

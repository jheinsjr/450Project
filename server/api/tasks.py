from database.session import rest_api
from flask_restful import Resource, reqparse, fields, marshal
from database.session import db
from flask import session
from sqlalchemy.exc import SQLAlchemyError

_task_fields = {
    'id': fields.Integer(attribute='Task_ID'),
    'title': fields.String(attribute='Title'),
    'description': fields.String(attribute='Description'),
    'status': fields.String(attribute='Status'),
    'creationDate': fields.String(attribute='Creation_TS'),
    'updatedDate': fields.String(attribute='Update_DT'),
    'createdBy': {'id': fields.Integer(attribute='Created_by'), 'name': fields.String(attribute='Full_Name')}
}


def push_change(task):
    if task['id'] == -1:
        db.engine.execute("""
        INSERT INTO Task
        (Title, Description, Status_ID, Creation_TS, Created_by)
        VALUES
        (:title, :description, 1, CURRENT_TIMESTAMP, :created_by)
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
    SELECT Task_ID, Title, Task.Description, S.Description as Status, Creation_TS, Update_DT, E.Employee_ID,
    E.First_Name as Full_Name
    FROM Task
    JOIN Employee E on Task.Created_by = E.Employee_ID
    JOIN Status S on Task.Status_ID = S.Status_ID
    """)

    def get(self):
        task_list = db.engine.execute(self.query).fetchall()
        task_marshal = marshal(task_list, _task_fields)

        return {"status": "success", "tasks": task_marshal}


# An individual task
class TaskID(Resource):
    def delete(self, id):
        db.engine.execute("""
        DELETE FROM Task WHERE Task_ID = ?
        """, id)

        return {"status": "success"}


class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("task", type=dict)

    def post(self):
        args = self.parser.parse_args()
        task = args.task
        user = session.get("user")

        if user is not None:
            task['created_by'] = user['user_id']
            push_change(task)
            return {"status": "success"}
        else:
            return {"status": "failed", "reason": "not logged in"}


class TaskStatus(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("status_id", type=int)

    def post(self, task_id):
        args = self.parser.parse_args()

        db.engine.execute("""
        UPDATE Task
        SET Status_ID = ?
        WHERE
        Task_ID = ?
        """, args['status_id'], task_id)

        return {"status": "success"}


rest_api.add_resource(TaskList, '/api/tasks')
rest_api.add_resource(TaskID, '/api/task/<int:id>')
rest_api.add_resource(Task, '/api/task')
rest_api.add_resource(TaskStatus, '/api/status/<int:task_id>')
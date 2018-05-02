from database.session import rest_api
from flask_restful import Resource, reqparse, fields, marshal
from database.session import db
from flask import session


class Team(Resource):
    _team_fields = {
        'id': fields.Integer(attribute='Employee_ID'),
        'username': fields.String(attribute='Username'),
        'name': fields.String(attribute='Full_Name'),
        'admin': fields.String(attribute='Admin')
    }

    def get(self):
        if session['user'] is None:
            return {'status': 'failed', 'reason': 'not logged in'}

        team = db.engine.execute("""
        SELECT Employee_ID, First_Name || ' ' || Last_Name as Full_Name, Username, Admin FROM Employee
        """).fetchall()

        return {'status': 'success', 'team': marshal(team, self._team_fields)}


rest_api.add_resource(Team, '/api/team')

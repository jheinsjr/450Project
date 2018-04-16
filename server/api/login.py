from flask import session
from flask_restful import Resource, reqparse
from sqlalchemy.exc import SQLAlchemyError
from database.session import db
from database.tables import User


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", required=True, type=str)
    parser.add_argument("password", required=True, type=str)

    def post(self):
        args = self.parser.parse_args()

        user = User.query.\
            filter(User.name == args["username"]).\
            first()

        if user is not None and args["password"] == user.password:
            session["user"] = user.name
            return {"status": "success"}
        else:
            return {"status": "failed"}


class Logout(Resource):
    def get(self):
        user = session.get("user")
        if user is not None:
            session.pop("user")
            return {"status": "success"}
        else:
            return {"status": "failed", "reason": "not logged in"}


class CreateAccount(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", required=True, type=str)
    parser.add_argument("password", required=True, type=str)

    def post(self):
        args = self.parser.parse_args()

        try:
            db.add(User(name=args["username"], password=args["password"]))
            db.commit()
            return {"status": "success"}
        except SQLAlchemyError:
            db.rollback()
            return {"status": "failed"}


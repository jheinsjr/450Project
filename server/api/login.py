from flask import session
from flask_restful import Resource, reqparse
from sqlalchemy.exc import SQLAlchemyError
from database.session import db, rest_api


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", required=True, type=str)
    parser.add_argument("password", required=True, type=str)

    def post(self):
        args = self.parser.parse_args()

        user = db.engine.execute("SELECT * FROM Employee where Username = ?", args.username).first()
        # user = User.query.\
        #    filter(User.name == args["username"]).\
        #    first()

        if user is not None and args.Password == user.password:
            session.user = user.name
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
            #db.add(User(name=args.username, password=args.password))
            #db.commit()
            db.engine.execute("INSERT INTO Employee (First_Name, Last_Name, Admin, Username, Password) VALUES"
                              "('PLACEHOLDER', 'PLACEHOLDER', 0, ?, ?)", args.username, args.password)
            return {"status": "success"}
        except SQLAlchemyError:
            db.rollback()
            return {"status": "failed"}


rest_api.add_resource(Login, '/api/login')
rest_api.add_resource(Logout, '/api/logout')
rest_api.add_resource(CreateAccount, '/api/create_account')

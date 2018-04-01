from flask import session
from flask_restful import Resource, reqparse

dummy_user_data = {
    "bob": {
        "password": "1234",
        "tasks": [
            {"id": 0, "name": "do that thing"},
            {"id": 1, "name": "do the other thing"}
        ]
    },
    "fred": {
        "password": "1234",
        "tasks": [
            {"id": 2, "name": "do what fred dose best"},
            {"id": 3, "name": "very important task for fred"}
        ]
    }
}


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", required=True, type=str)
    parser.add_argument("password", required=True, type=str)

    def post(self):
        args = self.parser.parse_args()
        user = dummy_user_data.get(args["username"])
        if user is not None and args["password"] == user["password"]:
            session["user"] = args["username"]
            return {"status": "success"}
        else:
            return {"status": "failed"}

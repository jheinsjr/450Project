import requests
from flask import Flask, request, jsonify, session
app = Flask(__name__)#, static_folder="../client/dist", static_url_path="")
app.secret_key = b'\xc9\x82:\xf6\x9c\x993\x83\xa5\xa3e\xda\x9f\xb8\xf7\x86\xe0\xaeSd\x147K4'

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


@app.route('/api/login', methods=["POST"])
def api_login():
    request_data = request.json
    username = request_data["username"]
    password = request_data["password"]

    user = dummy_user_data.get(username)
    if username in dummy_user_data is not None and user["password"] == password:
        result = {"status": "success"}
        session["user"] = username
    else:
        result = {"status": "failed"}

    return jsonify(result), 200


@app.route('/api/get_tasks', methods=["GET"])
def api_get_tasks():
    user = session.get("user")
    if user is not None:
        user_data = dummy_user_data.get(user)
        if user_data is not None:
            result = {"status": "success", "tasks": user_data["tasks"]}
        else:
            result = {"status": "failed", "reason": "User data could not be found"}
    else:
        result = {"status": "failed", "reason": "Not logged in"}

    return jsonify(result), 200


@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def root(path):
    # in debug mode it forwards all none api calls to the nodejs server
    # in production we should just server the static files
    if app.debug:
        return requests.get('http://localhost:5000/{}'.format(path)).text
    return app.send_static_file(path)


if __name__ == "__main__":
    app.run(port=8080, debug=True)

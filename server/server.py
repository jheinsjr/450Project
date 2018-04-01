import requests
from flask import Flask, jsonify, session
from flask_restful import Api
from api.login import Login, Logout
from api.tasks import TaskList

app = Flask(__name__)#, static_folder="../client/dist", static_url_path="")
app.secret_key = b'\xc9\x82:\xf6\x9c\x993\x83\xa5\xa3e\xda\x9f\xb8\xf7\x86\xe0\xaeSd\x147K4'
api = Api(app)
api.add_resource(Login, '/api/login')
api.add_resource(Logout, '/api/logout')
api.add_resource(TaskList, '/api/task-list')


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

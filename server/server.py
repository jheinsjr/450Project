import requests
import sys
from flask import Flask
from flask_restful import Api
from database.session import db
from api.login import Login, Logout, CreateAccount
from api.tasks import TaskList


def launch(debug):
    if debug:
        app = Flask(__name__)
    else:
        app = Flask(__name__, static_folder='../client/dist', static_url_path='')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.secret_key = b'\xc9\x82:\xf6\x9c\x993\x83\xa5\xa3e\xda\x9f\xb8\xf7\x86\xe0\xaeSd\x147K4'
    db.init_app(app)

    api = Api(app)
    api.add_resource(Login, '/api/login')
    api.add_resource(Logout, '/api/logout')
    api.add_resource(CreateAccount, '/api/create_account')
    api.add_resource(TaskList, '/api/task-list')

    if debug:
        @app.route('/', defaults={'path': 'index.html'})
        @app.route('/<path:path>')
        def root(path):
            return requests.get('http://localhost:5000/{}'.format(path)).text

        app.run(port=8080, debug=True)
    else:
        @app.route('/')
        def root():
            return app.send_static_file('index.html')

        app.run(port=80)

    return app


if __name__ == '__main__':
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    else:
        mode = 'debug'

    if mode == 'debug':
        launch(True)
    elif mode == 'production':
        launch(False)

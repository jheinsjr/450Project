import requests
import sys
from flask import Flask
from database.session import db, rest_api

from database.setup import init_db
import api.tasks # must keep
import api.login # must keep


def launch(mode):
    if mode != 'production':
        app = Flask(__name__)
    else:
        app = Flask(__name__, static_folder='../client/dist', static_url_path='')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = b'\xc9\x82:\xf6\x9c\x993\x83\xa5\xa3e\xda\x9f\xb8\xf7\x86\xe0\xaeSd\x147K4'

    db.init_app(app)
    rest_api.init_app(app)

    if mode == "setup":
        init_db(app)
    elif mode == "production":
        @app.route('/')
        def root():
            return app.send_static_file('index.html')

        app.run(port=80)
    else:
        @app.route('/', defaults={'path': 'index.html'})
        @app.route('/<path:path>')
        def root(path):
            return requests.get('http://localhost:5000/{}'.format(path)).text

        app.run(port=8080, debug=True)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        m = sys.argv[1]
    else:
        m = 'debug'
    
    launch(m)

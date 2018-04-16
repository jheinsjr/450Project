from database.session import db
from database.tables import *


def init_db(app):
    with app.app_context():
        db.create_all()

        # data
        db.session.add(User(name="fred", password="1234"))
        db.session.add(User(name="bob", password="4321"))
        db.session.commit()

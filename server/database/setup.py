from database.session import db
from database.tables import *


def init_db(app):
    db.create_all(app=app)

    # data
    db.add(User(name="fred", password="1234"))
    db.add(User(name="bob", password="4321"))
    db.commit()

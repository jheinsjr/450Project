from database.session import db
from database.tables import *


def init_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        execute_file(db.engine, "./sql_files/scheme.sql")
        execute_file(db.engine, "./sql_files/insert1.sql")

        # db.engine.execute("INSERT INTO Status(Description) VALUES (?)", "Not Started")
        # data
        #db.session.add(User(name="fred", password="1234"))
        #db.session.add(User(name="bob", password="4321"))
        db.session.commit()


def execute_file(engine, sql_file):
    with open(sql_file, 'r') as file,\
            engine.connect() as connection:
        cursor = connection.connection.cursor()
        text = file.read()
        cursor.executescript(text)
        cursor.close()


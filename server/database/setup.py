
from database.session import db


def init_db(app):
    with app.app_context():
        execute_file(db.engine, "./sql_files/scheme.sql")
        execute_file(db.engine, "./sql_files/insert1.sql")

        # db.engine.execute("INSERT INTO Status(Description) VALUES (?)", "Not Started")
        # data
        #db.session.add(Employee(firstName="fred", lastName="miller", admin=True, username="fhm88", password="test"))
        #db.session.commit()


def execute_file(engine, sql_file):
    with open(sql_file, 'r') as file,\
            engine.connect() as connection:
        cursor = connection.connection.cursor()
        text = file.read()
        cursor.executescript(text)
        cursor.close()



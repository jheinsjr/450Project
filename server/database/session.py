from flask_sqlalchemy import SQLAlchemy
# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
# engine = create_engine("mysql+pymysql://tasks:1234@localhost/tasks")
#engine = create_engine("sqlite:///database.db")

#get_db = sessionmaker(bind=engine)
#Base = declarative_base()

db = SQLAlchemy()

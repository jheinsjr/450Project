from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
engine = create_engine("mysql+pymysql://tasks:1234@localhost/tasks")

DB = sessionmaker()
DB.configure(bind=engine)
Base = declarative_base()



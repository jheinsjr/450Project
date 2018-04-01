from sqlalchemy import Column, String, Integer
from database.session import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20),)
    password = Column(String(20))

from database.session import engine, Base

Base.metadata.create_all(engine)

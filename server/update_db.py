from database.session import engine, DB, Base
from database.tables import User

meta = Base.metadata
db = DB()

# clear db
meta.drop_all(engine)
# add tables
meta.create_all(engine)

# add date
db.add_all([
    User(name="fred", password="1234"),
    User(name="bob", password="4321")
])

db.commit()

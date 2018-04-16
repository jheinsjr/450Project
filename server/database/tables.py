from database.session import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))

    def __repr__(self):
        return "<User(name='%s', password='%s')>" % (self.name, self.password)


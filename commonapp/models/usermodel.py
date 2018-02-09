from pythonsite import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    gender = db.Column(db.String(1),nullable=False,default='男')
    phone = db.Column(db.String(11),nullable=False,default=None)
    email = db.Column(db.String(120),nullable=False)

    def __repr__(self):
        return '<User %r>' % (self.name)
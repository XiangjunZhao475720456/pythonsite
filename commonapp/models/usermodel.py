from flask_login import AnonymousUserMixin
from flask_login._compat import unicode

from pythonsite import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    phone = db.Column(db.String(11), nullable=False, default=None)
    gender = db.Column(db.String(1),nullable=False,default='男')
    email = db.Column(db.String(120),nullable=False)

    def __init__(self,name,phone,gender,email):
        self.name = name
        self.phone = phone
        self.gender = gender
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

    def is_authenticated(self):
        '''Check the user whether logged in.'''

        if isinstance(self,AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        """Check the user whether pass the activation process."""
        return True

    def is_anonymous(self):
        """Check the user's login status whether is anonymous."""
        if isinstance(self,AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        """Get the user's uuid from database."""
        return unicode(self.id)


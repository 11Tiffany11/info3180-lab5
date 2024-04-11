# Add any model classes for Flask-SQLAlchemy here
from . import db
from sqlalchemy import Integer, DateTime
import datetime

class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(1000))
    poster = db.Column(db.String(120))
    created_at= db.Column(db.DateTime, default=datetime.datetime.utcnow)


    def __init__(self, title, description, poster):

        super().__init__()
        
        self.title = title
        self.description = description
        self.poster = poster
        

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support



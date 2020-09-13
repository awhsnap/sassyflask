from .extensions import db 
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    modified_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)


    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.filter_by(id=id).one_or_none()

    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return self.id
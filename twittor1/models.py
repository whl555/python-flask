
from sqlalchemy import ForeignKey
from twittor1 import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128), unique=True, index=True)
    email = db.Column(db.String(128))
    tweets = db.relationship('Tweet', backref='author', lazy='dynamic')

    def __repr__(self):
        return "id={}, username={}, password={}, email={}".format(
            self.id, self.username, self.password, self.email
        )


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(150))
    createTime = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return "content={}, create at {}".format(
            self.content,
            self.createTime
        )

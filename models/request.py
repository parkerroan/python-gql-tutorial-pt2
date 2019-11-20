from db import db
import time
from models.user import UserModel
from datetime import datetime, timezone


class RequestModel(db.Model):
    __tablename__ = 'requests'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    url_link = db.Column(db.String)
    created = db.Column(db.DateTime(timezone=True))
    updated = db.Column(db.DateTime(timezone=True))

    user = db.relationship("UserModel", back_populates = "user_requests")

    def __init__(self, **data):
        self.user_id = data.get('user_id')
        self.url_link = data.get('url_link')
        self.created = datetime.now(timezone.utc)
        self.updated = datetime.now(timezone.utc)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
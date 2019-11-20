from db import db
import os
from datetime import datetime, timezone

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    created = db.Column(db.DateTime(timezone=True))
    updated = db.Column(db.DateTime(timezone=True))

    user_requests = db.relationship(
        "RequestModel", back_populates="user", cascade="all,delete")

    def __init__(self, **data):
        self.email = data.get('email')
        self.created = datetime.now(timezone.utc)
        self.updated = datetime.now(timezone.utc)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
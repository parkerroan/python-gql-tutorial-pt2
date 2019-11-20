from app import app
from db import db
from models.request import RequestModel
from models.user import UserModel

db.init_app(app)

with app.app_context():
    db.create_all()
    parker = UserModel(email='user@email.com')
    req = RequestModel(url_link='https://google.com')
    req.user = parker
    db.session.add(parker)
    db.session.add(req)
    db.session.commit()

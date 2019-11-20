from flask import Flask
from flask_restful import Api
from resources.qr import QR

from flask_graphql import GraphQLView
from schemas.schema import schema
import os

app = Flask(__name__)
api = Api(app)

# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.route("/health")
def healthcheck():
    return "Healthy Endpoint"

api.add_resource(QR, '/qr')

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5001, debug=True)
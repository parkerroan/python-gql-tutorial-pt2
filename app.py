from flask import Flask
from flask_restful import Api
from resources.qr import QR

app = Flask(__name__)
api = Api(app)


@app.route("/health")
def healthcheck():
    return "Healthy Endpoint"

api.add_resource(QR, '/qr')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001, debug=True)
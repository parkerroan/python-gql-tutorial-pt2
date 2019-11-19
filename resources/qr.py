from flask_restful import Resource, reqparse
from flask import send_file
import logging
import qrcode
import io, base64

parser = reqparse.RequestParser()
parser.add_argument('url', type=str, required=True)

class QR(Resource):
    def post(self):
        data = parser.parse_args()
        img = qrcode.make(data.get('url'))
        byte_img = io.BytesIO()
        img.save(byte_img,'PNG')
        byte_img.seek(0)
        return send_file(byte_img,
                attachment_filename='qr_image.png',
                mimetype='image/png')

#!/usr/bin/env python

from flask import Flask
from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse

from config import Config
from mongo_access import MongoAccess

app = Flask(__name__)
api = Api(app)


class GetPaste(Resource):
    def get(self, paste_path):
        mongo = MongoAccess()
        try:
            return mongo.get_paste(paste_path), 200
        except IndexError:
            return {'not found': paste_path}, 404


class NewPaste(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str)
        args = parser.parse_args()
        text = args['text']
        mongo = MongoAccess()
        paste_path = mongo.create_paste(text)
        return {
            'paste_path': paste_path,
            'text': text
        }, 200


api.add_resource(NewPaste, '/pastes/')
api.add_resource(GetPaste, '/pastes/<string:paste_path>')

if __name__ == '__main__':
    app.run(
        host=Config().get_service_host(),
        port=Config().get_service_port(),
        debug=True
    )

#!/usr/bin/env python

from flask import Flask
from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse

from config import Config
from read_api import ReadAPI
from write_api import WriteAPI

app = Flask(__name__)
api = Api(app)

class GetPaste(Resource):
    def get(self, paste_id):
        read_api = ReadAPI()
        response, status_code = read_api.get_paste(paste_id)
        return response, status_code


class GetAllPastes(Resource):
    def get(self):
        read_api = ReadAPI()
        response, status_code = read_api.get_all_pastes()
        return response, status_code


class NewPaste(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str)
        args = parser.parse_args()
        text = args['text']
        write_api = WriteAPI()
        response, status_code = write_api.create_paste(text)
        return response, status_code


api.add_resource(NewPaste, '/pastes/')
api.add_resource(GetAllPastes, '/pastes/')
api.add_resource(GetPaste, '/pastes/<string:paste_id>')

if __name__ == '__main__':
    app.run(
        host=Config().get_host_number(),
        port=Config().get_port_number(),
        debug=True
    )

#!/usr/bin/env python

from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse

from app import app
from app import api
from app import db
from sql_access import get_paste
from sql_access import get_all_pastes
from sql_access import cache_random_shit
from sql_access import create_paste
from paste_id_creator import PasteIdCreator

from config import Config

class GetPaste(Resource):
    def get(self, paste_id):
        paste = get_paste(paste_id)
        if paste is None:
            return {'not_found': paste_id}, 404
        else:
            return {'paste_id': paste.paste_id, 'paste_path': paste.paste_path}, 200


class GetAllPastes(Resource):
    def get(self):
        pastes = [{'paste_id': p.paste_id, 'paste_path': p.paste_path} for p in get_all_pastes()]
        return {'pastes': pastes}, 200


class CreatePaste(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('paste_path', type=str)
        args = parser.parse_args()
        paste_path = args['paste_path']
        collides = True
        creator = PasteIdCreator()
        while collides:
            new_id = creator.create_paste_id()
            paste = get_paste(new_id)
            if paste is None:
                collides = False
        create_paste(new_id, paste_path)
        return {'paste_id': new_id}, 200


api.add_resource(GetAllPastes, '/pastes/')
api.add_resource(GetPaste, '/pastes/<string:paste_id>')
api.add_resource(CreatePaste, '/pastes/')


if __name__ == '__main__':
    db.create_all()
    app.run(
        host=Config().get_host_number(),
        port=Config().get_port_number(),
        debug=True
    )

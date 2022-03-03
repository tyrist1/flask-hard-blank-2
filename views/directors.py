from flask import  request
from flask_restx import  Resource, Namespace

import service
from dao.model.director import DirectorSchema

director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_Directors = service.director.get_all()
        res = DirectorSchema( many=True ).dump(all_Directors)
        return res, 200

@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, bid):
        b=service.director.get.one(bid)
        sm_d = DirectorSchema().dump(b)
        return sm_d, 200


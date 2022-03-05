from flask import  request
from flask_restx import  Resource, Namespace
from implemented import genre_service

from dao.model.genre import GenreSchema


genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_directors = genre_service.get_all ()
        return GenreSchema.dump ( all_directors ), 200

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = service.genre.get_all()
        res = GenreSchema( many=True ).dump(all_genres)
        return res, 200

@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, bid):
        b=service.genre.get.one(bid)
        sm_d = GenreSchema().dump(b)
        return sm_d, 200


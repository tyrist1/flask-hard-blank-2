from flask import  request
from flask_restx import  Resource, Namespace

import service
from dao.model.movie import MovieSchema
from service.movie import MovieService
from setup_db import db

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MoviesView(Resource):
    def get_all(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id" : director,
            "genre_id" : genre,
            "year" : year,
        }
        ms = MovieService(db.session)
        all_movies =ms.get_all()
        res = MovieSchema( many=True ).dump(all_movies)
        return res, 200

    '''def post(self):
        req_json = request.json
        movie = service.movie.create(req_json)
        return  "", 201, {"location": f"/movies/{movie.id}"}'''
@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get_one(self, bid):
        b=service.movie.get.one(bid)
        sm_d = MovieSchema().dump( b )
        return sm_d, 200

    # def put(self, bid):
    #     req_json = request.json
    #     if "id" not in req_json:
    #         req_json["id"] = bid
    #         service.movie.update ( req_json)
    #
    #     return "", 204
    #
    # def delete(self, bid):
    #     service.delete( bid)
    #     return "", 204
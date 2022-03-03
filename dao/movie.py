from dao.model.movie import Movie

class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_one (self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        return self.session.query(Movie).all()
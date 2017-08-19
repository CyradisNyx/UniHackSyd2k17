from flask_restful import Resource, abort, reqparse
from apiStuff import db, models


class Article(Resource):
    """Article Resource."""

    def get(self, id):
        """Get Article Info."""
        return {"article name": "Article name lolz",
                "article text": "article text here"}

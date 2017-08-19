"""Flask-RESTful Resource."""

from flask import jsonify
from flask_restful import Resource, abort
from apiStuff import db


class Article(Resource):
    """Article Resource."""

    def get(self, id):
        """Get Article Info."""
        return {"article name": "Article name lolz",
                "article text": "article text here"}

    def put(self):
        """Create new Article."""
        abort(404)


class Articles(Resource):
    """Multiple Articles Endpoint."""

    def get(self):
        """Return all the articles."""
        data = {"article1": {"title": "Charlottesville mayor: I changed my mind about Confederate monuments",
                            "text": "example piece of text 1.",
                            "rating": 5,
                            "source": "cnn",
                            "event": "Charlottesville",
                            "date": "19 Aug 2017",
                },
                "article2": {"title": "Charlottesville and the politics of fear",
                            "text": "example piece of text 2.",
                            "rating": 6,
                            "source": "conversation",
                            "event": "Charlottesville",
                            "date": "19 Aug 2017",
                },
                "article3": {"title": "Charlottesville and the politics of fear",
                            "text": "example piece of text 3.",
                            "rating": 4,
                            "source": "9news",
                            "event": "Charlottesville",
                            "date": "19 Aug 2017"}}
        return jsonify(data)


class Event(Resource):
    """Event Resource."""

    def get(self, id):
        """Get Event info."""
        return {"event name": "event name",
                "other stuff": "other stuff"}

    def put(self):
        """Create new Event."""
        abort(404)

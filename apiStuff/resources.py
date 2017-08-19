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
        data = {"article1": {"title": "title", "text": "text"}, "article2": {"title": "title", "text": "text"}}
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

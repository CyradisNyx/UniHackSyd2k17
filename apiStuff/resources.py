"""Flask-RESTful Resource."""

from flask import jsonify
from flask_restful import Resource, abort
from apiStuff import db, models


class Article(Resource):
    """Article Resource."""

    def get(self, id):
        """Get Article Info."""
        temp = models.Article.query.get(id)
        if temp is None:
            abort(404)
        return jsonify(temp.toDict())

    def put(self):
        """Create new Article."""
        abort(404)


class Articles(Resource):
    """Multiple Articles Endpoint."""

    def get(self):
        """Return all the articles."""
        data = {}
        for i in range(3):
            data.add(models.Article.query.get(id).toDict())
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

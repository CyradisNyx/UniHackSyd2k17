"""Flask-RESTful Resource."""

from flask import jsonify, g
from flask_restful import Resource, abort
from apiStuff import db, models, auth
from webargs import fields
from webargs.flaskparser import use_kwargs, parser


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


class AddUser(Resource):
    """User Resources."""

    user_args = {
        'email': fields.Str(required=True),
        'username': fields.Str(required=True),
        'password': fields.Str(required=True),
    }

    @use_kwargs(user_args)
    def post(self, email, username, password):
        """Make New User."""
        newUser = models.User(email, username, password)
        db.session.add(newUser)
        db.session.commit()


class GetUser(Resource):
    """Get User Data."""

    @auth.login_required
    def get(self, id):
        """Get ID."""
        user = models.User.query.get(id)
        if not user:
            abort(400)
        return jsonify({'username': user.username})


class Token(Resource):
    """Generate and return Auth Token."""

    @auth.login_required
    def get(self):
        """Generate Auth Token."""
        token = g.user.generate_auth_token(600)
        return jsonify({'token': token.decode('ascii'), 'duration': 600})


@auth.verify_password
def verify_password(username_or_token, password):
    """First try to authenticate by token."""
    user = models.User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = models.User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@parser.error_handler
def handle_request_parsing_error(err):
    """
    Webarg error handler.

    Uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(422, errors=err.messages)

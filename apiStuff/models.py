"""Define Database Model Structures."""
from apiStuff import db, app


class Article(db.Model):
    """
    Article DB Model.

    Table of article information.

    Args:
        source_url (str): source to scrape from

    Attributes:
        article_id (int): Integer representation/primary key
        title (str): title of article
        rating (int): left/right leaning
        event (db.Relationship): Instance of Event
        source (str): Company/Site Source
        source_url (str): Link to article
    """

    __tablename__ = "article"
    article_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    event = db.Column(db.Integer, db.ForeignKey('event.event_id'))

    def __init__(self, source_url):
        """Lol init stuff."""
        pass

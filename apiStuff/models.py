"""Define Database Model Structures."""
from apiStuff import db, app, helpers


class Article(db.Model):
    """
    Article DB Model.

    Table of article information.

    Args:
        source_url (str): source to scrape from
        event (Event): Event object article is part of

    Attributes:
        article_id (int): Integer representation/primary key
        title (str): title of article
        rating (int): left/right leaning
        event (db.Relationship): Instance of Event
        source (str): Company/Site Source
        source_url (str): Link to article
        date (DateTime): Date of article posting
        content (text): Text field containing article
    """

    __tablename__ = "article"
    article_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    event = db.relationship("Event")
    source = db.Column(db.String(20))
    source_url = db.Column(db.String(80))
    content = db.Column(db.Text)

    def __init__(self, source_url, event):
        """Assign Variables."""
        self.source_url = source_url
        self.event = event

        scrapeData = helpers.scrape(source_url)


class Event(db.Model):
    """
    Event db Model.

    Table of Event information.

    Args:
        idek

    Attributes:
        event_id (int): Integer representation/primary_key
        title (str): title of event
        date (str): date of creation (date of event)
        articles (db.Relationship): related articles
    """

    __tablename__ = "event"
    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    date = db.Column(db.DateTime)
    articles = db.relationship("Article", backref="event", lazy="dynamic")

    def __init__(self):
        """Assign Variables."""
        pass

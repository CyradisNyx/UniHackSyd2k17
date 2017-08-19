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
    source = db.Column(db.String(20))
    source_url = db.Column(db.String(80))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __init__(self, source_url, event=None):
        """Assign Variables."""
        self.source_url = source_url
        if event is not None:
            event.append(self)

        scrapeData = helpers.scrape(source_url)
        self.title = scrapeData['title']
        self.source = scrapeData['source']
        self.content = scrapeData['content']

        # self.rating = helpers.get_rating(self.article_id)

    def toDict(self):
        """Representation of object lol."""
        return {self.article_id: {
            "title": self.title,
            "rating": self.rating,
            "content": self.content
        }}


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

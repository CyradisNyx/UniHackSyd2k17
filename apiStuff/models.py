"""Define Database Model Structures."""
from apiStuff import db, app, helpers, scraping
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)


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
    title = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    source = db.Column(db.String(20))
    source_url = db.Column(db.String(80), unique=True)
    content = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __init__(self, source_url, scrapeData=None, event=None):
        """Assign Variables."""
        self.source_url = source_url
        if event is not None:
            event.append(self)
        if scrapeData is None:
            scrapeData = scraping.article_scrape_conversation(source_url)
        self.title = scrapeData['title']
        self.source = scrapeData['source']
        self.content = scrapeData['content']

        self.rating = helpers.get_rating(self.content)

    def toDict(self):
        """Representation of object lol."""
        return {self.article_id: {
            "title": self.title,
            "date": self.date,
            "source": self.source,
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
        keywords (str): comma separated list (as string) of named entity keywords
    """

    __tablename__ = "event"
    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    date = db.Column(db.DateTime)
    articles = db.relationship("Article", backref="event", lazy="dynamic")
    keywords = db.Column(db.String(200))

    def __init__(self, keywords):
        """Assign Variables."""
        self.keywords = keywords

    def toDict(self):
        """Representation of Object."""
        articledict = {}
        for article in self.articles:
            articledict[article.article_id] = article.title
        return {self.event_id: {
            "keywords": self.keywords,
            "articles": articledict
        }}


class User(db.Model):
    """
    User db model.

    Table of user information.

    Args:
        pass

    Attributes:
        user_id (int): Integer representation/primary key
        username (str): Unique username
        email (str): Unique email
        profile_pic (str): path to profile picture
    """

    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(128))
    profile_pic = db.Column(db.String(100))

    def __init__(self, email, username, pwd):
        """Assign Variables."""
        self.username = username
        self.email = email
        self.hash_password(pwd)

    def hash_password(self, pwd):
        """Encrypt pwd and save hashed version."""
        self.password_hash = pwd_context.encrypt(pwd)

    def verify_password(self, pwd):
        """Return Boolean if pwd matches hash."""
        return pwd_context.verify(pwd, self.password_hash)

    def generate_auth_token(self, expiration=600):
        """Generate Auth Token."""
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'user_id': self.user_id})

    @staticmethod
    def verify_auth_token(token):
        """Verify Auth Token Provided."""
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['user_id'])
        return user

"""Define Database Model Structures."""
from apiStuff import db, app


class Article(db.Model):
    """
    Article DB Model.

    Table of article information.

    Args:
        source_url (str): source to scrape from

    Attributes:
        title (str): title of article
        .....
    """

    __tablename__ = "article"

    def __init__(self, source_url):
        """Lol init stuff."""
        pass

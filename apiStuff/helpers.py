"""Helper Variables and Functions."""

import numpy as np
from apiStuff import db, models
import indicoio


def get_rating(content):
    """Generate rating for content text."""
    indicoio.config.api_key = '11214320f4b6ce1e81f46ed4a570c7e0'
    x = indicoio.political(content)
    rating = (x['Liberal'] / (x['Liberal'] + x['Conservative'])) * 10
    return (rating)


def genDB():
    """Fill Database."""
    temp = models.Article('0')
    db.session.add(temp)
    db.session.commit()
    temp = models.Article('1')
    db.session.add(temp)
    db.session.commit()
    temp = models.Article('2')
    db.session.add(temp)
    db.session.commit()
    pass

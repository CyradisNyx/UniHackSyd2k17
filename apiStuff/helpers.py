"""Helper Variables and Functions."""

import numpy as np
from apiStuff import db, models
import indicoio


def get_rating(id):
    """Generate rating for content text."""
    indicoio.config.api_key = '11214320f4b6ce1e81f46ed4a570c7e0'
    x = indicoio.political(models.Article.query.get(id).content)
    rating = (x['Liberal'] / (x['Liberal'] + x['Conservative'])) * 10
    return (rating)


def scrape(url):
    """
    Scraper function.

    Take url string, and returns dictionary of values, matched with
    field names in models.py
    """
    if url == '0':
        return {"title": "Charlottesville mayor: I changed my mind about Confederate monuments",
                "source": "cnn",
                "content": "random article text here"}
    elif url == '1':
        return {"title": "Charlottesville and the politics of fear",
                "source": "conversation",
                "content": "example piece of text 2."}
    else:
        return {"title": "Charlottesville and the politics of fear",
                "source": "9news",
                "content": "example piece of text 3."}
    pass


def genDB():
    """Fill Database with random info."""
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

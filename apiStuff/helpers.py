"""Helper Variables and Functions."""
from apiStuff import models, db


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
    for i in range(3):
        temp = models.Article(str(i))
        db.session.add(temp)
        db.session.commit()
    pass

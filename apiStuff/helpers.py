"""Helper Variables and Functions."""

import numpy as np
from apiStuff import db, models
import indicoio
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree


def get_rating(content):
    """Generate rating for content text."""
    indicoio.config.api_key = '11214320f4b6ce1e81f46ed4a570c7e0'
    x = indicoio.political(content)
    rating = (x['Liberal'] / (x['Liberal'] + x['Conservative'])) * 10
    return (rating)


def get_continuous_chunks(text):
    """Named Entity Recognition."""
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    return continuous_chunk


def jaccard_similarity(query, document):
    """Determine similarity of two documents."""
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union)


def makeEvent(article):
    """Figure out whether or not to make new Event."""
    events = models.Event.query.all()
    temp_token = get_continuous_chunks(article.content)

    for event in events:
        if jaccard_similarity(temp_token,
                              event.keywords.split(',')) > 0.4:
            event.articles.append(article)
            db.session.add(event)
            db.session.add(article)
            db.session.commit()
            return
    newEvent = models.Event(",".join(temp_token), article.title)
    print(newEvent.title)
    newEvent.articles.append(article)
    db.session.add(newEvent)
    db.session.add(article)
    db.session.commit()
    return

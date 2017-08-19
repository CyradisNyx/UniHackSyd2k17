"""Helper Variables and Functions."""

import numpy as np
from apiStuff import db, models

import indicoio
def get_rating(article):
	indicoio.config.api_key = '11214320f4b6ce1e81f46ed4a570c7e0'
	x = (indicoio.political())
	rating = (x['Liberal']/(x['Liberal'] + x['Conservative'])) * 10
	return (rating)
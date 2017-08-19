"""Various Scraping Functions for each website."""
import requests
from bs4 import BeautifulSoup
from apiStuff import models, db


def scrape(article_url):
    """Determine which website function needs to be used, run, and return."""
    if article_url.split('.')[1] == "conversation":
        return article_scrape_conversation(article_url)


def scrape_all():
    """Build database by scraping each site, and generating events/articles."""
    curr_urls = site_scrape_conversation()
    for url in curr_urls:
        temp = models.Article(url, article_scrape_conversation(url))
        db.session.add(temp)
        db.session.commit()


def site_scrape_conversation():
    """Mass Site Scraper for conversation.com ."""
    site_url = ['http://theconversation.com/au', 'http://theconversation.com']

    r = requests.get(site_url[0])
    soup = BeautifulSoup(r.text, "html.parser")
    topic_urls = []
    article_urls = []

    # Scrape Main Site for Topic URLs
    for topic in soup.find_all('section', id="topics"):
        for line in topic.find_all('a', href=True):
            if line.text.strip():
                topic_urls.append(site_url[1] + line['href'])

    # Scrape Each Topic for Article URL
    for topic in topic_urls[1:]:
        r = requests.get(topic)
        soup = BeautifulSoup(r.text, 'html.parser')
        article = soup.find('h2').find('a')
        if article.text.strip():
            article_urls.append(site_url[0] + article['href'])

    return article_urls


def article_scrape_conversation(site_url):
    """Scrape Individual Article."""
    pass

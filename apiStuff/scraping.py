"""Various Scraping Functions for each website."""
import requests
from bs4 import BeautifulSoup
from apiStuff import models, db


def scrape(article_url):
    """Determine which website function needs to be used, run, and return."""
    pass


def scrape_all():
    """Build database by scraping each site, and generating events/articles."""
    curr_urls = site_scrape_abc()
    for url in curr_urls:
        # Generate Event Stuff Here, and pass into temp
        temp = models.Article(url, article_scrape_abc(url))
        db.session.add(temp)
        db.session.commit()

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
            article_urls.append(site_url[1] + article['href'])

    return article_urls


def article_scrape_conversation(site_url):
    """Scrape Individual Article."""
    r = requests.get(site_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    output = {'title': "",
              'source': "Conversation",
              'content': ""}

    for text in soup.find_all('title'):
        output['title'] = text.get_text()

    for text in soup.find_all('div', itemprop='articleBody'):
        for line in text.find_all('p'):
            output['content'] += line.get_text()

    return output


def site_scrape_abc():
    """Mass Site Scraper for ABC News."""
    site_url = ['http://www.abc.net.au/news/', 'http://www.abc.net.au']
    r = requests.get(site_url[0])
    soup = BeautifulSoup(r.text, 'html.parser')
    article_urls = []

    # scrapes the main site for topic urls.
    for topic in soup.find_all('li', class_='doctype-article'):
        if topic.find('h3'):
            topic = topic.find('h3').find('a')
            article_urls.append(site_url[1] + topic['href'])

    return article_urls[:7]


def article_scrape_abc(site_url):
    """Scrape Individual Article."""
    r = requests.get(site_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    output = {'title': "",
              'source': "ABC News",
              'content': ""}
    termination_string = 'Topics:'

    for text in soup.find_all('div', class_='article section'):
        for line in text.find_all('h1'):
            output['title'] = line.get_text()

    for text in soup.find_all('div', class_='article section'):
        for line in text.find_all('p'):
            output['content'] += line.get_text()

    end_index = output['content'].index(termination_string)
    output['content'] = output['content'][:end_index].rstrip()

    return output


def site_scrape_breitbart():
    """Mass Site Scraper for Breitbart."""
    pass


def article_scrape_breitbart(site_url):
    """Scrape Individual Article."""
    pass


def site_scrape_fox():
    """Mass Site Scraper for Fox."""
    pass


def article_scrape_fox(site_url):
    """Scrape Individual Article."""
    pass


def site_scrape_washpo():
    """Mass Site Scraper for Washington Post."""
    pass


def article_scrape_washpo(site_url):
    """Scrape Individual Article."""
    r = requests.get(site_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    output = {'title': "",
              'source': "Washington Post",
              'content': ""}
    termination_string = 'Read more'

    for text in soup.find_all('title'):
        output['title'] = text.get_text()

    for text in soup.find_all('div', itemprop='articleBody'):
        for line in text.find_all('p'):
            output['content'] += line.get_text()

    end_index = output['content'].index(termination_string)
    output['content'] = output['content'][:end_index].rstrip()

    return output


# NOT WORKING
def site_scrape_nine():
    """Mass Site Scraper for 9 News."""
    site_url = ['http://www.9news.com.au/national', 'http://www.9news.com']
    r = requests.get(site_url[0])
    soup = BeautifulSoup(r.text, 'html.parser')
    article_urls = []

    for topic in soup.find_all('article'):
        topic = topic.find('div')
        topic = topic.find('a')
        if topic:
            article_urls.append(topic['href'])

    print(article_urls)
    return article_urls


def article_scrape_nine(site_url):
    """Scrape Individual Article."""
    r = requests.get(site_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    output = {'title': "",
              'source': "Nine News",
              'content': ""}

    for text in soup.find_all('title'):
        output['title'] = text.get_text()

    for text in soup.find_all('div', itemprop='article__body-croppable'):
        for line in text.find_all('p'):
            output['content'] += line.get_text()

    return output

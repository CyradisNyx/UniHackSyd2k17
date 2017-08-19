import requests
from bs4 import BeautifulSoup

def conversation_site_scraper(site_url):
	r = requests.get(site_url[0])
	soup = BeautifulSoup(r.text, 'html.parser')
	topic_urls = []
	article_urls = []

	# scrapes the main site for topic urls.
	for topic in soup.find_all('section', id = 'topics'):
		for line in topic.find_all('a', href = True):
			if line.text.strip():
				topic_urls.append(site_url[1] + line['href'])
	
	# scrapes each topic for one article url.
	for topic in topic_urls[1:]:
		r = requests.get(topic)
		soup = BeautifulSoup(r.text, 'html.parser')
		article = soup.find('h2').find('a')
		if article.text.strip():
			article_urls.append(site_url[0] + article['href'])
	return article_urls




site = 'Conversation'
site_url = ['http://theconversation.com/au', 'http://theconversation.com']
article_urls = conversation_site_scraper(site_url)
print(article_urls)



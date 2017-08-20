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
			article_urls.append(site_url[1] + article['href'])
	return (article_urls)

def news9_site_scraper(site_url):
	r = requests.get(site_url[0])
	soup = BeautifulSoup(r.text, 'html.parser')
	article_urls = []

	# scrapes the main site for article urls.
	for topic in soup.find_all('article'):
		topic = topic.find('div')
		topic = topic.find('a')
		if topic:
			article_urls.append(topic['href'])
	return (article_urls)

def abc_site_scraper(site_url):
	r = requests.get(site_url[0])
	soup = BeautifulSoup(r.text, 'html.parser')
	article_urls = []

	# scrapes the main site for topic urls.
	for topic in soup.find_all('li', class_ = 'doctype-article'):
		if topic.find('h3'):
			topic = topic.find('h3').find('a')
			article_urls.append(site_url[1] + topic['href'])
	return article_urls[:7]
			
			
def fox_site_scraper():
	site_url = ['http://www.foxnews.com/', 'http://www.foxnews.com/']
	r = requests.get(site_url[0])
	soup = BeautifulSoup(r.text, 'html.parser')
	article_urls = []

	# scrapes the main site for topic urls.
	for topic in soup.find_all('div', id = 'doc'):
		for section in topic.find_all('section', id = 'latest'):
			for article in section.find_all('a'):
				article_urls.append(article['href'])
	return (article_urls[:7])



#site = 'Conversation'
#site_url = ['http://theconversation.com/au', 'http://theconversation.com']
#article_urls = conversation_site_scraper(site_url)
#print(article_urls)

site = '9news'
site_url = ['http://www.9news.com.au/national', 'http://www.9news.com']
article_urls = news9_site_scraper(site_url)
for article in article_urls:
	print (article +'\n')

#site = 'abc'
#site_url = ['http://www.abc.net.au/news/', 'http://www.abc.net.au']
#article_urls = abc_site_scraper(site_url)
#for article in article_urls:
#	print (article +'\n')

#article_urls = fox_site_scraper()
#for article in article_urls:
#	print (article +'\n')



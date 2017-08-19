import requests
from bs4 import BeautifulSoup

url = 'http://www.9news.com.au/national/2017/08/19/22/05/all-blacks-humble-wallabies-again'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

title = ''
contents = ''

for text in soup.find_all('title'):
	title = text.get_text()

for text in soup.find_all('div', class_ = 'article__body-croppable'):
	for line in text.find_all('p'):
		article = line.get_text()
		contents += article

output = {'Title': title, 'Source': '9 News', 'Content': contents}
print(output)
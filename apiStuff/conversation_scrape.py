import requests
from bs4 import BeautifulSoup

url = 'http://theconversation.com/charlottesville-and-the-politics-of-fear-82443'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

title = ''
contents = ''

for text in soup.find_all('title'):
	title = text.get_text()

for text in soup.find_all('div', itemprop = 'articleBody'):
	for line in text.find_all('p'):
		article = (line.get_text())
		contents += (article)

output = {'Title': title, 'Source': 'The Conversation', 'Content': contents}
print(output)
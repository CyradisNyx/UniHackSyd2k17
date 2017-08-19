import requests
from bs4 import BeautifulSoup

url = 'http://theconversation.com/charlottesville-and-the-politics-of-fear-82443'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for text in soup.find_all('div', itemprop = 'articleBody'):
	for line in text.find_all('p'):
		print(line.get_text())
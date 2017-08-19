import requests
from bs4 import BeautifulSoup



url = 'http://www.9news.com.au/world/2017/08/19/02/35/majority-of-trumps-arts-council-quits-over-charlottesville-rally-comments'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for text in soup.find_all('div', class_ = 'article__body-croppable'):
	for line in text.find_all('p'):
		print(line.get_text())
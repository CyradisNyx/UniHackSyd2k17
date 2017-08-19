import requests
from bs4 import BeautifulSoup

url = 'https://www.washingtonpost.com/news/retropolis/wp/2017/06/23/six-nazi-spies-were-executed-in-d-c-white-supremacists-gave-them-a-memorial-on-federal-land/?tid=a_inl&utm_term=.260c11052e84'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

title = ''
contents = ''

for text in soup.find_all('title'):
	title = text.get_text()

termination_string = 'Read more'
for text in soup.find_all('article', itemprop = 'articleBody'):
	for line in text.find_all('p'):
		article = (line.get_text())
		contents += (article)
	
end_index = contents.index(termination_string)
contents = contents[:end_index].rstrip()
	

output = {'Title': title, 'Source': 'Washington Post', 'Content': contents}
print(output)


	
import requests
from bs4 import BeautifulSoup


url = 'http://www.abc.net.au/news/2017-08-14/charlottesville-white-supremacist-counter-protests/8804600'
r = requests.get(url)

title = ''
contents = ''
termination_string = 'Topics:'
soup = BeautifulSoup(r.text, 'html.parser')

for text in soup.find_all('div', class_ = 'article section'):
	for line in text.find_all('h1'):
		title = line.get_text()

for text in soup.find_all('div', class_ = 'article section'):
	for line in text.find_all('p'):
		article = (line.get_text())
		contents += (article)

end_index = contents.index(termination_string)
contents = contents[:end_index].rstrip()
print(contents)
print()

output = {'Title': title, 'Source': 'ABC', 'Content': contents}
print(output)


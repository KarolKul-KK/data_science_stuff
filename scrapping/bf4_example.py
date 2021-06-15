from bs4 import BeautifulSoup
import requests


url = ("https://raw.githubusercontent.com/joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.p.text.split()
print(first_paragraph)

first_paragraph_id = soup.p['id']
print(first_paragraph_id)

first_paragraph_id_2 = soup.p.get('id')
print(first_paragraph_id_2)

all_paragraphs = soup.find_all('p')
print(all_paragraphs)

paragraphs_with_ids = [p for p in soup('p') if p.get('id')]
print(paragraphs_with_ids)

important_paragraphs = soup('p', {'class' : 'important'})
print(important_paragraphs)

important_paragraphs_2 = soup('p', 'important')
print(important_paragraphs_2)

important_paragraphs_3 = [p for p in soup('p')
                            if 'important' in p.get('class', [])]
print(important_paragraphs_3)
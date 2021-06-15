import re
from bs4 import BeautifulSoup
import requests


url = "https://www.house.gov/representatives"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")

all_urls = [a['href']
                for a in soup('a')
                if a.has_attr('href')]

print(len(all_urls))


regex = r"^https?://.*\.house\.gov/?$"

assert re.match(regex, 'http://joel.house.gov')
assert re.match(regex, 'https://joel.house.gov')
assert re.match(regex, "http://joel.house.gov/")
assert re.match(regex, "https://joel.house.gov/")
assert not re.match(regex, 'joel.house.gov')
assert not re.match(regex, "http://joel.house.com")
assert not re.match(regex, "https://joel.house.gov/biography")

good_urls = [url for url in all_urls if re.match(regex, url)]

print(len(good_urls))

#delete duplicates
good_urls = list(set(good_urls))

print(len(good_urls))
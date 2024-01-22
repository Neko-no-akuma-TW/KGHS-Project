from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.ly.gov.tw/Pages/List.aspx?nodeid=37075"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req).read().decode('utf-8')

bsObj = BeautifulSoup(response, 'html.parser')
a = bsObj.find('section', {'id': 'six-legislatorListBox'}).findAll("a",
                                                                      {"data-toggle": "tooltip"})
for item in a:
    name = item.find('div', {'class': 'legislatorname'}).get_text().strip()
    party = item.findAll('div')[2].get_text().strip()
    area = item.findAll('div')[3].get_text().strip()
    print(name, party, area)
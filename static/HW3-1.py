from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://web.ee.ntu.edu.tw/teacher_index_all.php"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req).read().decode('utf-8')

bsObj = BeautifulSoup(response, 'html.parser')
a = bsObj.find('div', {'id': 'display_type1'}).findAll("div", {"style": "background:#F0FBFD; width:100%; "})
for item in a:
    item = item.find("div", {"class": "teacher_list_intro"})
    name = item.find("a").get_text().strip()
    title = item.findAll("td")[1].get_text().strip()
    title2 = item.findAll("td")[2].get_text().strip()
    email = item.findAll('img')[0]['alt'].strip()
    print(name[-3:], email, title, title2[3:])
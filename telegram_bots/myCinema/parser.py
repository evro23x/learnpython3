from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
html_doc = urlopen('http://python-3.ru').read()
f = open('parsed_page', 'w')
f.write(str(html_doc))
f.close()

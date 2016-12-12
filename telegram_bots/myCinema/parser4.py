from bs4 import BeautifulSoup
from urllib.request import urlopen


html_doc = urlopen('https://www.afisha.ru/msk/cinema/').read()
soup = BeautifulSoup(html_doc, "lxml")


# print(soup)


# print(soup.find('ul', 'b-dropdown-common-fixed'))


for li in soup.find('ul', {'class': 'b-dropdown-common-fixed'}).findAll('li'):
    print(li.findAll('a'))

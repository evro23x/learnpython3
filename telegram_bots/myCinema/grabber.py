from bs4 import BeautifulSoup
from urllib.request import urlopen

#получаем контент страницы
html_doc = urlopen('https://www.afisha.ru/msk/cinema/').read()
soup = BeautifulSoup(html_doc, "lxml")

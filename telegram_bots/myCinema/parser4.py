from bs4 import BeautifulSoup
from urllib.request import urlopen

#получаем контент страницы
html_doc = urlopen('https://www.afisha.ru/msk/cinema/').read()
soup = BeautifulSoup(html_doc, "lxml")

# парсим список станци метро для получения привязки к ним кт
for li in soup.find('ul', {'class': 'b-dropdown-common-fixed'}).findAll('li'):
    # ссылка на метро формата - //www.afisha.ru/msk/cinema/cinema_list/aviamotornaya/
    # print(li.find('a')['href'])
    # название метро - Авиамоторная
    print("Станция метро: {}".format(li.find('a').contents[0]))
    # link_to_metro = li.find('a')['href']
    metro_to_cinema = BeautifulSoup(urlopen('https:' + li.find('a')['href']).read(), 'lxml')
    for div_cinema in metro_to_cinema.find('div', {'class': 'b-places-list'}).findAll('h3'):
        # https://www.afisha.ru/msk/schedule_cinema_place/3652/
        # ссылка на кт формата - //www.afisha.ru/msk/cinema/34317/
        # print(div_cinema.find('a')['href'])
        # название кт - Летний кт на ВДНХЛетний кт на ВДНХ
        print("Название кинотеатра: {}".format(div_cinema.find('a').contents[0]))

        # собираем правильную ссылку на рассписание кт с учетом его id
        pattern_url_table = 'https://www.afisha.ru/msk/schedule_cinema_place/'
        url_cinema = div_cinema.find('a')['href']
        id_cinema = url_cinema[url_cinema[0:-1].rfind('/') + 1:-1]
        url_table = pattern_url_table + id_cinema + '/'
        link_to_cinema = BeautifulSoup(urlopen(url_table).read(), 'lxml')

        for div_film in link_to_cinema.find('div', {'class': 'b-theme-schedule'}).findAll('tr', {'class': 's-votes-hover-area'}):
            print(div_film.find('div', {'class': 'clearfix'}).find('a').contents[0])
            print(div_film.find('div', {'class': 'time-inside line'}).findAll('span'))
            # print(div_film.findAll(match_class(["feeditemcontent", "cxfeeditemcontent"])))

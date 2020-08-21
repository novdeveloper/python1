import requests
from bs4 import BeautifulSoup

URL = 'https://www.callmewine.com/vini-C1.htm'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0', 'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
HOST = 'https://www.callmewine.com/vini-C1'

URL2_RED = 'https://www.vino75.com/en/vino/rosso'
URL2_WHITE = 'https://www.vino75.com/en/vino/bianco'
URL2_SPARKLING = 'https://www.vino75.com/en/vino/spumante'
HEADERS2 = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0', 'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
HOST2 = 'https://www.vino75.com/en'


def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_ = 'nav__item')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1



def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'products-list__item')
    vini = []
    for item in items:
        vini.append({
                'title': item.find('a', class_ = 'prodotto-listato__link prodotto-listato__hide').get_text(strip = True),
                'link': HOST + item.find('a', class_ = 'prodotto-listato__link prodotto-listato__hide').get('href'),
                })
    return vini
    


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        vini = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(URL, params = {'page': page})
            vini.extend(get_content(html.text))
        print(vini)
        print(len(vini))
            #vini = get_content(html.text)
            
    else:
        print('error')







parse()
#html2 = requests.get("https://www.callmewine.com/kike-cantine-fina-2019-P23593.htm").text
#soup2 = BeautifulSoup(html2, 'html.parser')
#caratteristiche = soup2.find_all('div', class_ = 'prodotto__descrizione__content formatted-content')
#print(caratteristiche)
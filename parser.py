import requests
from bs4 import BeautifulSoup

URL = 'https://status.ecwid.com/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='component-container border-color')

    status_list = []
    for item in items:
        status_list.append({
            'title': item.find('span', class_='name').get_text(strip=True),
            'status': item.find('span', class_='component-status').get_text(strip=True),
        })
    return status_list


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        status_list = get_content(html.text)
        for status in status_list:
            print(status['title'] + ': ' + status['status'])
    else:
        print('Error')


parse()

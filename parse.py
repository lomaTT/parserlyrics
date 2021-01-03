import requests
from bs4 import BeautifulSoup

URL = 'https://www.amalgama-lab.com/songs/n/neighbourhood/stargazing.html'                     # URL of page, which we want to parse
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'accept': '*/*'} # this line accept two very important arguments


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_pages_count(html):                                                                      # if number of pages 2+
    pass


def get_content(html):                                                                          # get text of users music
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='string_container')
    text = []
    for item in items:
        text.append({
            'line': item.find('div', class_='original').get_text('\n', strip=True)
        })
    print(text)

def parse():                                                                                    # main function
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('ERROR')


parse()
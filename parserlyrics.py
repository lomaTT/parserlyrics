import requests
from bs4 import BeautifulSoup
import parsermain

URL = 'https://www.amalgama-lab.com/songs/' + parsermain.first_letter
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0', 'content-type': 'text/html; charset=windows-1251'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

html = get_html(URL)

def get_link(link_string):
    link_string = str(link_string)[9::]
    correct_link = []
    n = 0
    for i in range(len(link_string)):
        if link_string[i] != '>':
            n = n + 1
        else:
            break
    correct_link = link_string[:n - 1:]
    return correct_link


def get_list_of_groups(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('div', class_='band_name_pict')
    list_of_groups = []
    for item in items:
        list_of_groups.append({
            'group': item.find('a').get_text(),
            'link':  get_link(item.find('a'))
        })
    print('Below you can see list of groups, what we have in our database.')
    for group in list_of_groups:
        print(group['group'])
    name_of_necessary_group = input('Please, choose one of them and write here: ')
    print('Loading...\n')
    link_of_necessary_group = ''
    for group in list_of_groups:
        if name_of_necessary_group == group['group']:
            link_of_necessary_group = group['link']
            break
    link_of_necessary_group = URL + link_of_necessary_group[8::]
    return link_of_necessary_group



def parse():
    if html.status_code == 200:
        get_list_of_groups(html)
    else:
        print('ERROR')

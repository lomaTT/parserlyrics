import requests
from bs4 import BeautifulSoup
import parsermain

URL = 'https://www.amalgama-lab.com/songs/' + parsermain.group_name[0:1:]
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0', 'content-type': 'text/html; charset=windows-1251'}

group_link = ''

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


def get_group_link(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('div', class_='band_name_pict')
    list_of_groups = []
    link_of_necessary_group = ''
    group_link = ''
    isFind = False
    for item in items:
        list_of_groups.append({
            'group': item.find('a').get_text(),
            'link':  get_link(item.find('a'))
        })
    for group in list_of_groups:
        if parsermain.group_name == group['group'].lower():
            link_of_necessary_group = group['link']
            print('Finded!')
            isFind = True
            break
    while isFind == False:
        for group in list_of_groups:
            print(group['group'])
        print('We have not this group in our database, try again :(')
        parsermain.group_name = input('Above you can see list of groups with similar starting letter, please. Choose one: ').lower()
        for group in list_of_groups:
            if parsermain.group_name == group['group'].lower():
                link_of_necessary_group = group['link']
                print('Finded!')
                isFind = True
                break
        

    link_of_necessary_group = URL + link_of_necessary_group[8::]
    group_link = link_of_necessary_group
    return group_link



def parse():
    if html.status_code == 200:
        get_group_link(html)
    else:
        print('ERROR')

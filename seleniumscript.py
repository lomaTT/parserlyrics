from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import parserlyrics

options = Options()
options.add_argument('--headless')
browser = webdriver.Firefox(options=options)
browser.get(parserlyrics.get_group_link(parserlyrics.html))

ul = browser.find_elements_by_tag_name('ul')
list_of_songs = []
links = []
songs_and_links = []
isSongFinded = False

for i in ul[8].text.split('\n'):
    list_of_songs.append(i)
for i in list_of_songs:
    links.append(browser.find_element_by_link_text(i).get_attribute('href'))
for i in range(len(list_of_songs)):
    songs_and_links.append({
        'name_of_song': list_of_songs[i],
        'link_of_song': links[i]
    })
for song in songs_and_links:
    print(song['name_of_song'])
print('Above you can see list of songs, what we have in our database')
necessary_song = input('Print name of song, lyrics of what you want see: ')
if necessary_song == 'C':
    print('See you next time ;)')
    exit()
link_of_necessary_song = ''
while isSongFinded == False:
    for song in songs_and_links:
        if necessary_song.lower() == song['name_of_song'].lower():
            link_of_necessary_song = song['link_of_song']
            isSongFinded = True
            print('Finded!')
            break
    if (isSongFinded == False):
        necessary_song = input('Unfortunately, we have not this track in our database, or your input was incorrent. Try again: ' ).lower()
print('Loading...\n')
browser.quit()

link_of_necessary_song = parserlyrics.get_html(link_of_necessary_song)

def find_lyrics(link):
    soup = BeautifulSoup(link.text, 'html.parser')
    lyrics_all = soup.find_all('div', class_='string_container')
    lyrics = []
    for i in lyrics_all:
        lyrics.append({
            'english version': i.find('div', class_='original').get_text(strip='\n'),
            'russian version': i.find('div', class_='translate').get_text(strip='\n')
        })
    answer = ''
    max_length_eng = int(0)
    while (answer != 'Y') and answer != 'N' and answer != 'C':
        answer = input('Wanna see russian translation? (Y/N): ')
    if answer == 'Y':
        for i in lyrics:
            if len(i['english version']) > max_length_eng:
                max_length_eng = len(i['english version'])
        for i in lyrics:
            print(i['english version'], (max_length_eng - len(i['english version'])) * ' ', i['russian version'])
    elif answer == 'N':
        for i in lyrics:
            print(i['english version'])
    else:
        print('See you next time! ;)')
        exit()
        


find_lyrics(link_of_necessary_song)
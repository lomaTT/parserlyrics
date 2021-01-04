# main program of script
import requests
from bs4 import BeautifulSoup

print('WARNING: If you want to stop script - input C in any question.')
group_name = (input('Write group name, which you want to find (for example: A or 0): ')).lower()
if group_name == 'c':
    print('See you next time ;)')
    exit()
if (group_name[:4:]) == 'the ':
    group_name = group_name[4::] + ', ' + 'the'

print('Loading...\n')
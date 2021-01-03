# main program of script
import requests
from bs4 import BeautifulSoup

group_name = (input('Write group name, which you want to find (for example: A or 0): ')).lower()
if (group_name[:4:]) == 'the ':
    group_name = group_name[4::] + ', ' + 'the'

print('Loading...\n')
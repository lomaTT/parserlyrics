# main program of script
import requests
from bs4 import BeautifulSoup

first_letter = (input('Write first letter of number group name, which you want to find, if name contains "The", ignore it (for example: A or 0): ')).lower()
print('Loading...\n')
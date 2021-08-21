from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests

itung = 0

# Setting up
html = requests.get('https://www.imdb.com/title/tt6334354/?ref_=adv_li_tt').text
web = bs(html, 'html.parser')

# Get director
director = web.find(
    'a', class_ = 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
print(director.text)

# Get writer
writer = web.find_all(
    'a', class_ = 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
print(writer[1].text)
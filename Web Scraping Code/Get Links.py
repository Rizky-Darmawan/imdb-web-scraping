import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

test = []

# Setting up
html_text = requests.get('https://www.imdb.com/search/title/?title_type=feature&genres=action&start=1&explore=genres')
soup = BeautifulSoup(html_text.text, 'lxml')

# Find container and filter conditions
containers = soup.find_all('div', class_ = 'lister-item mode-advanced')
for container in containers :
    condition1 = container.find('span', class_ = 'certificate')

    if condition1 is not None :
        condition2 = container.p.b

        if condition2 is None :
            link = container.h3.a['href']
            test.append(link)


driver = webdriver.Edge('C:/Users/Abc/Documents/Edge Driver/msedgedriver.exe')
for coba in test :
    driver.get('https://www.imdb.com/' + coba)
    time.sleep(1)



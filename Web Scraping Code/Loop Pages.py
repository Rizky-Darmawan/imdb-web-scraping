from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

pages = []
test = []
no_page = 1
while no_page <= 51 :
    pages.append(no_page)
    no_page += 50

# Loop pages
for page in pages :

    # Setting up
    html_text = requests.get('https://www.imdb.com/search/title/?title_type=feature&genres=action&start=' + str(page) + '&explore=genres')
    time.sleep(4)
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
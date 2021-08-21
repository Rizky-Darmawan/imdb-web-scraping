from bs4 import BeautifulSoup as bs
import requests

# Setting up
html = requests.get('https://www.imdb.com/title/tt6334354/?ref_=adv_li_tt').text
web = bs(html, 'html.parser')

# Get title
title_container = web.find('div', class_ = 'TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt')
title = title_container.h1.text
print(title)

# Get year
year = title_container.a.text
print(year)

# Get duration
duration = title_container.find_all('li', class_ = 'ipc-inline-list__item')
duration = duration[2].text
print(duration)

# Get imdb rating
imdb_container = web.find(
    'div', class_ = 'RatingBar__RatingContainer-sc-85l9wd-0 hNqCJh TitleBlock__HideableRatingBar-sc-1nlhx7j-4 bhTVMj')
imdb = imdb_container.span.text
print(imdb)

# Get user review
review_container = web.find('div', class_ = 'Hero__WatchContainer__Video-kvkd64-5 lbieXL')
user = review_container.find_all('span', class_ = 'score')
user = user[0].text
print(user)

# Get critic review
critic = review_container.find_all('span', class_ ='score')
critic = critic[1].text
print(critic)

# Get metacore
meta = review_container.find('span', class_ = 'score-meta').text
print(meta)

# Get director and writer container
dw_container = web.find('div', {'data-testid' : 'title-pc-wide-screen'})

# Get director
director_container = dw_container.find_all('li', class_ = 'ipc-metadata-list__item')
director_container = director_container[0]
director = director_container.a.text
print(director)

# Get writer
writer_container = dw_container.find_all('li', class_ = 'ipc-metadata-list__item')
writer_container = writer_container[1]
writer = writer_container.a.text
print(writer)

# Get studio
detail_container = web.find('div', {'data-testid' : 'title-details-section'})
studio_container = detail_container.find('li', {'data-testid' : 'title-details-companies'})
studio = studio_container.ul.a.text
print(studio)

# Get money container
money_container = web.find('div', {'data-testid' : 'title-boxoffice-section'})

# Get budget
try:
    budget_container = money_container.find('li', {'data-testid' : 'title-boxoffice-budget'})
    budget = budget_container.li.span.text
    budget = budget.replace('(estimated)', '')
    print(budget)
except:
    print('No data')
    pass

# Get us gross
try:
    us_container = money_container.find('li', {'data-testid' : 'title-boxoffice-grossdomestic'})
    us = us_container.li.span.text
    print(us)
except:
    print('No data')
    pass

# Get world gross
try:
    world_container = money_container.find('li', {'data-testid' : 'title-boxoffice-cumulativeworldwidegross'})
    world = world_container.li.span.text
    print(world)
except:
    print('No data')
    pass

# Get aspect ratio
spec_container = web.find('div', {'data-testid' : 'title-techspecs-section'})
aspect_container = spec_container.find('li', {'data-testid' : 'title-techspec_aspectratio'})
aspect = aspect_container.ul.span.text
print(aspect)


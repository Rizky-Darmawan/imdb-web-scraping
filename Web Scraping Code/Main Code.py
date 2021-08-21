from bs4 import BeautifulSoup
import requests
import time
from random import randint
import pandas as pd

# Empty list
pages = []
links = []

# Empty datasets
movie_titles = []
release_date = []
mpaa_rating = []
runtime = []
metascores_rating = []
imdb_rating = []
user_reviews = []
critic_reviews = []
director_names = []
writer_names = []
studios = []
movie_budget = []
us_sales = []
world_sales = []
tech_specs = []

# Monitor
web_pages = 0

# Creating pages list
no_page = 1
while no_page <= 5001 :
    pages.append(no_page)
    no_page += 50

# Loop pages
for page in pages :

    # Setting up
    html_text = requests.get(
        'https://www.imdb.com/search/title/?title_type=feature&genres=action&start=' + str(page) + '&explore=genres')

    # Report monitoring
    web_pages += 1
    print(f'Page {str(web_pages)} retrieved')
    time.sleep(randint(4, 8))

    # Parse html
    soup = BeautifulSoup(html_text.text, 'lxml')

    # Find container and filter conditions
    containers = soup.find_all('div', class_='lister-item mode-advanced')
    for container in containers:
        condition1 = container.find('span', class_='certificate')

        if condition1 is not None:
            condition2 = container.p.b

            if condition2 is None:
                link = container.h3.a['href']
                links.append(link)

    # Report links retrieved
    print(f'{len(links)} links retrieved')
    print('-------------------------------------------------------------------------------------')

# Report datasets snatching
print('')
print('SNATCHING DATASETS')
print('')

# Setting up data snatching
num_link = 0
for link in links :
    error = 0
    num_link += 1
    web_pages = requests.get('https://www.imdb.com/' + link).text
    print(f'Snatching data from link {num_link}')

    # Pause and parse
    time.sleep(randint(3, 7))
    web = BeautifulSoup(web_pages, 'html.parser')

    # Get title
    try:
        title_container = web.find('div', class_='TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt')
        title = title_container.h1.text
        movie_titles.append(title)
        num_title = 1
    except:
        movie_titles.append('')
        num_title = 0
        error += 1
        pass

    # Get year
    try:
        title_container = web.find('div', class_='TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt')
        year = title_container.a.text
        release_date.append(year)
        num_year = 1
    except:
        release_date.append('')
        num_year = 0
        error += 1
        pass

    # Get MPAA
    try:
        title_container = web.find('div', class_='TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt')
        mpaa = title_container.find_all('li', class_='ipc-inline-list__item')
        mpaa = mpaa[1].span.text
        mpaa_rating.append(mpaa)
        num_mpaa = 1
    except:
        mpaa_rating.append('')
        num_mpaa = 0
        error += 1
        pass

    # Get duration
    try:
        title_container = web.find('div', class_='TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt')
        duration = title_container.find_all('li', class_='ipc-inline-list__item')
        duration = duration[2].text
        runtime.append(duration)
        num_duration = 1
    except:
        runtime.append('')
        num_duration = 0
        error += 1
        pass

    # Get imdb rating
    try:
        imdb_container = web.find(
            'div', class_='RatingBar__RatingContainer-sc-85l9wd-0 hNqCJh TitleBlock__HideableRatingBar-sc-1nlhx7j-4 bhTVMj')
        imdb = imdb_container.span.text
        imdb_rating.append(imdb)
        num_imdb = 1
    except:
        imdb_rating.append('')
        num_imdb = 0
        error += 1
        pass

    # Get user review
    try:
        review_container = web.find('div', class_='Hero__WatchContainer__Video-kvkd64-5 lbieXL')
        user = review_container.find_all('span', class_='score')
        user = user[0].text
        user_reviews.append(user)
        num_user = 1
    except:
        user_reviews.append('')
        num_user = 0
        error += 1
        pass

    # Get critic review
    try:
        review_container = web.find('div', class_='Hero__WatchContainer__Video-kvkd64-5 lbieXL')
        critic = review_container.find_all('span', class_='score')
        critic = critic[1].text
        critic_reviews.append(critic)
        num_critic = 1
    except:
        critic_reviews.append('')
        num_critic = 0
        error += 1
        pass

    # Get metascore
    try:
        review_container = web.find('div', class_='Hero__WatchContainer__Video-kvkd64-5 lbieXL')
        meta = review_container.find('span', class_='score-meta').text
        metascores_rating.append(meta)
        num_meta = 1
    except:
        metascores_rating.append('')
        num_meta = 0
        error += 1
        pass

    # Get director and writer container
    dw_container = web.find('div', {'data-testid': 'title-pc-wide-screen'})

    # Get director
    try:
        director_container = dw_container.find_all('li', class_='ipc-metadata-list__item')
        director_container = director_container[0]
        director = director_container.li.a.text
        director_names.append(director)
        num_director = 1
    except:
        director_names.append('')
        num_director = 0
        error += 1
        pass

    # Get writer
    try:
        writer_container = dw_container.find_all('li', class_='ipc-metadata-list__item')
        writer_container = writer_container[1]
        writer = writer_container.li.a.text
        writer_names.append(writer)
        num_writer = 1
    except:
        writer_names.append('')
        num_writer = 0
        error += 1
        pass

    # Get studio
    try:
        detail_container = web.find('div', {'data-testid': 'title-details-section'})
        studio_container = detail_container.find('li', {'data-testid': 'title-details-companies'})
        studio = studio_container.ul.a.text
        studios.append(studio)
        num_studio = 1
    except:
        studios.append('')
        num_studio = 0
        error += 1
        pass

    # Get money container
    money_container = web.find('div', {'data-testid': 'title-boxoffice-section'})

    # Get budget
    try:
        budget_container = money_container.find('li', {'data-testid': 'title-boxoffice-budget'})
        budget = budget_container.li.span.text
        budget = budget.replace('(estimated)', '')
        movie_budget.append(budget)
        num_budget = 1
    except:
        movie_budget.append('')
        num_budget = 0
        error += 1
        pass

    # Get us gross
    try:
        us_container = money_container.find('li', {'data-testid': 'title-boxoffice-grossdomestic'})
        us = us_container.li.span.text
        us_sales.append(us)
        num_us = 1
    except:
        us_sales.append('')
        num_us = 0
        error += 1
        pass

    # Get world gross
    try:
        world_container = money_container.find('li', {'data-testid': 'title-boxoffice-cumulativeworldwidegross'})
        world = world_container.li.span.text
        world_sales.append(world)
        num_world = 1
    except:
        world_sales.append('')
        num_world = 0
        error += 1
        pass

    # Get aspect ratio
    try:
        spec_container = web.find('div', {'data-testid': 'title-techspecs-section'})
        aspect_container = spec_container.find('li', {'data-testid': 'title-techspec_aspectratio'})
        aspect = aspect_container.ul.span.text
        tech_specs.append(aspect)
        num_spec = 1
    except:
        tech_specs.append('')
        num_spec = 0
        error += 1
        pass

    # Report data snatched
    a = num_title + num_year + num_mpaa + num_duration + num_imdb + num_user + num_critic + num_meta + num_director + num_writer + num_studio + num_budget + num_us + num_world + num_spec
    print(f'{a} data snatched')
    print(f'{error} data empty')
    print('-------------------------------------------------------------------------------------')
    print('')

# Check datasets
print('')
print('TOTAL DATA RETRIEVED')
print(f'Titles = {len(movie_titles)}')
print(f'Release date = {len(release_date)}')
print(f'MPAA =  {len(mpaa_rating)}')
print(f'Runtime =  {len(runtime)}')
print(f'Metascores =  {len(metascores_rating)}')
print(f'IMDB =  {len(imdb_rating)}')
print(f'User reviews =  {len(user_reviews)}')
print(f'Critic reviews =  {len(critic_reviews)}')
print(f'Directors =  {len(director_names)}')
print(f'Writers =  {len(writer_names)}')
print(f'Studios =  {len(studios)}')
print(f'Budget =  {len(movie_budget)}')
print(f'US gross =  {len(us_sales)}')
print(f'World gross =  {len(world_sales)}')
print(f'Aspect ratio =  {len(tech_specs)}')

# Saving data
df = pd.DataFrame({
    'Titles' : movie_titles, 'Released' : release_date, 'MPAA' : mpaa_rating, 'Runtime' : runtime,
    'Metascores' : metascores_rating, 'IMDB' : imdb_rating, 'User Reviews' : user_reviews,
    'Critic Reviews' : critic_reviews, 'Directors' : director_names, 'Writers' : writer_names, 'Studios' : studios,
    'Budget' : movie_budget, 'US Gross' : us_sales, 'Worldwide Gross' : world_sales, 'Aspect Ratio' : tech_specs
})
df.to_csv('action_movies.csv')


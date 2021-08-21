from selenium import webdriver

itung = 0

# Setting up
driver = webdriver.Edge('C:/Users/Abc/Documents/Edge Driver/msedgedriver.exe')
driver.get('https://www.imdb.com/title/tt3228774/?ref_=hm_fanfav_tt_t_5_pd_fp1')
driver.implicitly_wait(10)

# Get director
directors = driver.find_elements_by_xpath("//a[@class = 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link']")
for director in directors :
    print(f'{itung}. {director.text}')
    itung += 1


driver.quit()
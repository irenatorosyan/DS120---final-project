import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

from pprint import pprint
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from re import search

from recipe_scrapers import scrape_me

import re




links_ = []


url = 'https://tasty.co/ingredient/all-purpose-flour'
response = requests.get(url)
page = BeautifulSoup(response.content, "html.parser")

quantity_str = str([i.text for i in page.find_all(class_ = 'text-gray-lighter xs-inline-block')])
quantity = re.findall(r'\d+', quantity_str)
quantity_ = int(quantity[0])

iter_count = quantity_//20


wd = webdriver.Chrome(ChromeDriverManager().install())
wd.get(url)

wd.maximize_window()


for a in range(iter_count):
    if a != 0:
        next_ = wd.find_element_by_xpath('//button[normalize-space()="Show more"]')
    else:
        next_ = wd.find_element_by_id('init-show-more')
    
    try:
        next_.click()
    except:
        time.sleep(3)
        
    raw_links = page.find_all('a')

    for i in raw_links:
        if search("https://tasty.co/recipe", i.get('href')):
            links_.append(i.get('href'))

            
titles_ = []
ingredients_ = []

for i in links_:
    print(i) # this is just for seeing the progress
    scraper = scrape_me(i)
    titles_.append(scraper.title())
    ingredients_.append(scraper.ingredients())
    
main_ing = [i.text for i in page.find_all(class_ = "topic-title extra-bold xs-inline-block xs-mr1")]
ing_ = main_ing * len(links_)


dict_data = {'TITLES': titles_, 'INGREDIENTS': ingredients_, 'LINKS': links_, 'MAIN INGREDIENT': ing_}
df = pd.DataFrame(data = dict_data)
print(df)




df.to_csv("all_purpose_floor.csv")

# run this if you don't have 'recipe_scrapers installed'
# !pip install recipe-scrapers

# the available functiunality of 'recipe_scrapers', do not run this
# from recipe_scrapers import scrape_me
# scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
# scraper.title()
# scraper.total_time()
# scraper.yields()
# scraper.ingredients()
# scraper.instructions()
# scraper.image()
# scraper.host()
# scraper.links()

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



titles_ = []
ingredients_ = []
links_ = []
    
def low_scrape(low_url):

    links = []

    url = low_url
    response = requests.get(url)
    page = BeautifulSoup(response.content, "html.parser")


    raw_links = page.find_all('a', class_ = "comp card")

    for i in raw_links:
        if search("https://www.simplyrecipes.com/", i.get('href')):
            if (i.get('href') != 'https://www.simplyrecipes.com/'):
                links.append(i.get('href'))
                
    print(links)
    
    for j in links:
        scraper = scrape_me(j)
        titles_.append(scraper.title())
        try:
            ingredients_.append(scraper.ingredients())
        except:
            ingredients_.append("None")
        links_.append(j)
        
        
        
def high_scrape(high_url):
    links1 = []

    url = high_url
    response = requests.get(url)
    page = BeautifulSoup(response.content, "html.parser")


    raw_links = page.find_all('a', class_ = "text-link section__title")

    for i in raw_links:
        links1.append(i.get('href'))

    for a in links1:
        low_scrape(a)
        
        

# this part was not used, because it was taking very long time and scraping by small parts was more "safe"
# def highest_scrape(highest_url):
#     links2 = []
    
#     url = highest_url
#     response = requests.get(url)
#     page = BeautifulSoup(response.content, "html.parser")
    
#     raw_links = page.find_all('a', class_ = "global-nav__sub-list-item")

#     for i in raw_links:
#         links2.append(i.get('href'))

#     for a in links2:
#         high_scrape(a)
        
# highest_scrape("https://www.simplyrecipes.com/")

high_scrape("https://www.simplyrecipes.com/breakfast-recipes-5091541")
pd.set_option('display.max_rows', 10000)
real_dict_data = {'TITLES': titles_, 'INGREDIENTS': ingredients_, 'LINKS': links_}
real_df = pd.DataFrame(data = real_dict_data)
real_df.to_csv("breakfast.csv")
real_df

high_scrape("https://www.simplyrecipes.com/lunch-recipes-5091263")
pd.set_option('display.max_rows', 10000)
real_dict_data = {'TITLES': titles_, 'INGREDIENTS': ingredients_, 'LINKS': links_}
real_df = pd.DataFrame(data = real_dict_data)
real_df.to_csv("lunch.csv")
real_df

high_scrape("https://www.simplyrecipes.com/dinner-recipes-5091433")
pd.set_option('display.max_rows', 10000)
real_dict_data = {'TITLES': titles_, 'INGREDIENTS': ingredients_, 'LINKS': links_}
real_df = pd.DataFrame(data = real_dict_data)
real_df.to_csv("dinner.csv")
real_df

high_scrape("https://www.simplyrecipes.com/dessert-recipes-5091513")
pd.set_option('display.max_rows', 10000)
real_dict_data = {'TITLES': titles_, 'INGREDIENTS': ingredients_, 'LINKS': links_}
real_df = pd.DataFrame(data = real_dict_data)
real_df.to_csv("dessert.csv")
real_df

high_scrape("https://www.simplyrecipes.com/drink-recipes-5091323")
pd.set_option('display.max_rows', 10000)
real_dict_data = {'TITLES': titles_, 'INGREDIENTS': ingredients_, 'LINKS': links_}
real_df = pd.DataFrame(data = real_dict_data)
real_df.to_csv("drinks.csv")
real_df

high_scrape("https://www.simplyrecipes.com/snacks-and-appetizer-recipes-5090762")
pd.set_option('display.max_rows', 10000)
real_dict_data = {'TITLES': titles_, 'INGREDIENTS': ingredients_, 'LINKS': links_}
real_df = pd.DataFrame(data = real_dict_data)
real_df.to_csv("snacksAndAppetizer.csv")
real_df

high_scrape("https://www.simplyrecipes.com/holiday-and-seasonal-recipes-5091321")
pd.set_option('display.max_rows', 10000)
real_dict_data = {'TITLES': titles_, 'INGREDIENTS': ingredients_, 'LINKS': links_}
real_df = pd.DataFrame(data = real_dict_data)
real_df.to_csv("holidaysAndSeasonal.csv")
real_df

high_scrape("https://www.simplyrecipes.com/recipes-by-diet-5091259")
pd.set_option('display.max_rows', 10000)
real_dict_data = {'TITLES': titles_, 'INGREDIENTS': ingredients_, 'LINKS': links_}
real_df = pd.DataFrame(data = real_dict_data)
real_df.to_csv("byDiet.csv")
real_df

high_scrape("https://www.simplyrecipes.com/recipes-by-method-5091235")
pd.set_option('display.max_rows', 10000)
real_dict_data = {'TITLES': titles_, 'INGREDIENTS': ingredients_, 'LINKS': links_}
real_df = pd.DataFrame(data = real_dict_data)
real_df.to_csv("byMethod.csv")
real_df

high_scrape("https://www.simplyrecipes.com/recipes-by-ingredients-5091192")
pd.set_option('display.max_rows', 10000)
real_dict_data = {'TITLES': titles_, 'INGREDIENTS': ingredients_, 'LINKS': links_}
real_df = pd.DataFrame(data = real_dict_data)
real_df.to_csv("byingredients.csv")
real_df

first = pd.read_csv('breakfast.csv')
second = pd.read_csv('lunch.csv')
third = pd.read_csv('dinner.csv')
fourth = pd.read_csv('dessert.csv')
fifth = pd.read_csv('drinks.csv')
sixth = pd.read_csv('snacksAndAppetizer.csv')
seventh = pd.read_csv('holidaysAndSeasonal.csv')
eighth = pd.read_csv('byDiet.csv')
ninth = pd.read_csv('byMethod.csv')
tenth = pd.read_csv('byingredients.csv')

frames = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth]
allrecipes = pd.concat(frames)
allrecipes.drop_duplicates()

allrecipes.drop_duplicates().to_csv('allrecipes.csv', index=False)
df = pd.read_csv('allrecipes.csv')
df.sort_values("TITLES", inplace = True)
df.drop_duplicates(subset = "TITLES", keep = False, inplace = True)
del df['Unnamed: 0']
df.reset_index()
df.to_csv('recipesWithoutDuplicates.csv', index = False)

# I forgot about the existance of "recipesWithoutDuplicates.csv" and later did this steps again on "allrecipes.csv". 
# That is why the file that is currently used in the matcher and recommender is called "allrecipes.csv".

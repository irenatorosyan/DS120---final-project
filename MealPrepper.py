import streamlit as st
import pandas as pd
import numpy as np
import re
import MPcodes
import base64




# Cached functions
read_and_cache_data = st.cache(pd.read_csv)

cached_data = read_and_cache_data('allrecipes.csv')
data = cached_data.copy()

st.sidebar.markdown('# Meal Prepper')
navigation = st.sidebar.radio('Navigation', ('Meal Reccomendation', 'Reccomendation System'))
userInput =[]
match_string3 = ''

st.sidebar.image('someone.png', caption=None, width=430, use_column_width=None, clamp=False, channels='RGB', output_format='auto')



##################################
#### Meal Reccomendation #########
##################################

if navigation == 'Meal Reccomendation':

    st.header('Not sure what to cook? We can help!')
    show_profile = st.checkbox('Show description')
    if show_profile:
        '''
        The data for the analysis is scraped from SimplyRecipies, an open online community.
        It contains information about all kinds of recipes, including breakfast, lunch and dinner.

        The aim of this app is to recommend recipes depending on the products that an individual has in their fridge and pantry.

        Furthermore, after collecting a certain amount of data the app will be able to suggest recipes based on the most searched ingredients by the user.
        '''
    st.image('Meal-Prepper.png', caption=None, width=200, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

    st.markdown('_'*100) # adding a breaking line


    head_count = st.slider('How many rows of data to show?', 5, 50, 5, 5)
    match_string = st.text_input("Put your ingredients seperated by commas")
    match_string= str(match_string)
    st.dataframe(MPcodes.match(match_string).head(head_count))
    st.markdown('_'*100) # adding a breaking line

    match_string1 = st.text_input("Put your ingredients seperated by commas ")
    match_string1 = str(match_string1)
    st.dataframe(MPcodes.match(match_string1).head(head_count))
    st.markdown('_'*100) # adding a breaking line

    match_string2 = st.text_input("Put your ingredients seperated by commas  ")
    match_string2 = str(match_string2)
    st.dataframe(MPcodes.match(match_string2).head(head_count))
    st.markdown('_'*100) # adding a breaking line
    

    match_string3 = st.text_input("Put your ingredients seperated by commas   ")
    match_string3 = str(match_string3)
    st.dataframe(MPcodes.match(match_string3).head(head_count))
    st.markdown('_'*100) # adding a breaking line

if match_string3:

    h = match_string + ', ' + match_string1 + ', ' + match_string2 + ', ' + match_string3
   
    history = list(h.split(','))
    
    for q in range(len(history)):
        history[q] = history[q].strip()
    
    my_dict = {i:history.count(i) for i in history}
    sorted_ = sorted(my_dict, key=my_dict.get)[::-1]
    

    str_ = ""
    for i in sorted_:
        if i != 0:
            str_ = str_ + "," + i
        if i == 0:
            str_ = i
    
    x = re.findall(" *\\w+, *\\w+", str_)[0]
    st.text("Recipes with your top 1 ingredient:")
    st.text(sorted_[0])
    st.dataframe(MPcodes.match(sorted_[0]))

    st.text("Recipes with your top 2 ingredient:")
    st.text(sorted_[1])
    st.dataframe(MPcodes.match(sorted_[1]))


    st.text("Recipes with your top 1 and top 2 ingredients:")
    st.text(x)
    st.dataframe(MPcodes.match(x))


##################################
#### Recommendation SYstem #######
##################################




if navigation == 'Reccomendation System':
    st.header('The place to find recipes for your preferances!')
    rating5 = 0
    show_profile1 = st.checkbox('If you don’t have any recipes in mind, here are some ideas for you:')
    if show_profile1:

        '''
        Zucchini Ricotta Frittata, Vegan Chocolate Pudding, Eggplant Caviar, 
        

        Mediterranean Mezze Platte, Pecan Pralines, Copycat Chipotle Guacamole,
        

        Cheesy Hamburger Pasta Skillet, Pasta With Turkey, Pasta Puttanesca.
        '''

    st.image('Meal-Prepper.png', caption=None, width=200, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

    title1 = st.text_input("Please input the title of the first recipe: ")
    rating1 = st.text_input("Please input the rating of the first recipe: ")
            
    if not re.findall('^1|2|3|4|5$', rating1):
        st.text("Dear user, please make sure that the ratings are integers from 1 to 5 inclusive")

    title2 = st.text_input("Please input the title of the second recipe: ")
    rating2 = st.text_input("Please input the rating of the second recipe: ")

    if not re.findall('^1|2|3|4|5$', rating2):
        st.text("Dear user, please make sure that the ratings are integers from 1 to 5 inclusive")

    title3 = st.text_input("Please input the title of the third recipe: ")
    rating3 = st.text_input("Please input the rating of the third recipe: ")

    if not re.findall('^1|2|3|4|5$', rating3):
        st.text("Dear user, please make sure that the ratings are integers from 1 to 5 inclusive")

    title4 = st.text_input("Please input the title of the forth recipe: ")
    rating4 = st.text_input("Please input the rating of the forth recipe: ")

    if not re.findall('^1|2|3|4|5$', rating4):
        st.text("Dear user, please make sure that the ratings are integers from 1 to 5 inclusive")

    title5 = st.text_input("Please input the title of the fifth recipe: ")
    rating5 = st.text_input("Please input the rating of the fifth recipe: ")

    if not re.findall('^1|2|3|4|5$', rating5):
        st.text("Dear user, please make sure that the ratings are integers from 1 to 5 inclusive")

    if rating5:
        
        userInput = [{'TITLES': title1, 'rating': int(rating1)}, {'TITLES': title2, 'rating': int(rating2)}, 
                    {'TITLES': title3, 'rating': int(rating3)}, {'TITLES': title4, 'rating': int(rating4)}, 
                    {'TITLES': title5, 'rating': int(rating5)}]

        st.dataframe(MPcodes.get_recommendation(userInput))





















        # userInput = [
    #         {'TITLES':'Zucchini Ricotta Frittata', 'rating':5},
    #         {'TITLES':'Vegan Chocolate Pudding', 'rating':5},
    #         {'TITLES':'Mediterranean Mezze Platte', 'rating':2},
    #         {'TITLES':"Pecan Pralines", 'rating':0},
    #         {'TITLES':'Sous Vide Sesame Chicken', 'rating':4}]

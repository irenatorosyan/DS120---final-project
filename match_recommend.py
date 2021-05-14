import pandas as pd
import numpy as np
import re

searched = []
flat_searched = []
check = 1

# ask the user to input the ingredients separeted by commas
# returnes matched recipes
def match(str_):
    df = pd.read_csv("allrecipes.csv")
    df_ = pd.read_csv("allrecipes.csv")
    i_ = 0
    splited = list(str_.split(','))
    for i in range(len(df.INGREDIENTS)):
        x = 0
        for j in splited:
            j = re.sub(' +', ' ', j)
            if j.lower() in df.INGREDIENTS[i].lower():
                x += 1
        if x == len(splited):
            df_.iloc[i_] = df.iloc[i]
            i_ += 1
    display(df_.iloc[:i_])

    print(splited)
    if(check == 1):
        searched.append(splited)
    check == 1

def history():
    for sublist in searched:
        for item in sublist:
            flat_searched.append(item)

    for j in range(len(flat_searched)):
        flat_searched[j] = re.sub(' +', ' ', flat_searched[j])
        flat_searched[j] = flat_searched[j].strip()
    return(flat_searched)

def find_reccomendation(ings):
    ings_str = ""
    for i in ings:
        if ings_str:
            ings_str = ings_str + ", " + i
        else:
            ings_str = i 
    match(ings_str)

def reccomend():
    history()
    my_dict = {i:flat_searched.count(i) for i in flat_searched}
    sorted_ = sorted(my_dict, key=my_dict.get)[::-1]

    check = 0 

    print("Recipes with your top 1 ingredient")
    find_reccomendation(sorted_[0:1])

    check = 0 

    print("Recipes with your top 2 ingredient")
    find_reccomendation(sorted_[1:2])

    check = 0 

    print("Recipes with your top 3 ingredient")
    find_reccomendation(sorted_[2:3])

    check = 0 

    print("Recipes with your top 1 and top 2 ingredients")
    find_reccomendation(sorted_[0:2])
    
#test
match("chicken, bread,   black     pepper, ham")
match("ham, chicken, pepper")
match("bread")
match("coffee")
reccomend()

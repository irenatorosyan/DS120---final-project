import pandas as pd
import numpy as np
import re

class reccomend:
    
    def __init__(self):
        self.searched = []
        self.flat_searched = []
        self.check = 1
        
    # ask the user to input the ingredients separeted by commas
    # returnes matched recipes
    def match(self, str_):
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
        if(self.check == 1):
            self.searched.append(splited)
        self.check == 1
        
    def history(self):
        for sublist in self.searched:
            for item in sublist:
                self.flat_searched.append(item)
                
        for j in range(len(self.flat_searched)):
            self.flat_searched[j] = re.sub(' +', ' ', self.flat_searched[j])
            self.flat_searched[j] = self.flat_searched[j].strip()
        return(self.flat_searched)
    
    def find_reccomendation(self,ings):
        ings_str = ""
        for i in ings:
            if ings_str:
                ings_str = ings_str + ", " + i
            else:
                ings_str = i 
        self.match(ings_str)
    
    def reccomend(self):
        self.history()
        my_dict = {i:self.flat_searched.count(i) for i in self.flat_searched}
        sorted_ = sorted(my_dict, key=my_dict.get)[::-1]
        
        self.check = 0 
        
        print("Recipes with your top 1 ingredient")
        self.find_reccomendation(sorted_[0:1])
        
        print("Recipes with your top 2 ingredient")
        self.find_reccomendation(sorted_[1:2])
        
        print("Recipes with your top 3 ingredient")
        self.find_reccomendation(sorted_[2:3])
        
        print("Recipes with your top 1 and top 2 ingredients")
        self.find_reccomendation(sorted_[0:2])
        
# examples
tom = reccomend()
tom.match("chicken, bread,   black     pepper, ham")
tom.match("ham, chicken, pepper")
tom.match("bread")
tom.match("coffee")
tom.reccomend()

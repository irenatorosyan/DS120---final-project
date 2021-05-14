#import packages
import numpy as np
import pandas as pd
import random

#read the data
recipes_df = pd.read_csv('allrecipes.csv', usecols = ["TITLES", "LINKS"])
recipes_df["recipeId"] = recipes_df.index+1
recipes_df = recipes_df[["recipeId", "TITLES", "LINKS"]]

ratings_df = pd.read_csv('ratings.csv')

# the input that was given was

userInput = [
            {'TITLES':'Zucchini Ricotta Frittata', 'rating':5},
            {'TITLES':'Vegan Chocolate Pudding', 'rating':5},
            {'TITLES':'Mediterranean Mezze Platte', 'rating':2},
            {'TITLES':"Pecan Pralines", 'rating':0},
            {'TITLES':'Sous Vide Sesame Chicken', 'rating':4}
         ] 

def get_recommendation():
    inputRecipes = pd.DataFrame(userInput)
    
    inputId = recipes_df[recipes_df['TITLES'].isin(inputRecipes['TITLES'].tolist())]
    inputRecipes = pd.merge(inputId, inputRecipes)
    
    userSubset = ratings_df[ratings_df['recipeId'].isin(inputRecipes['recipeId'].tolist())]
    
    userSubsetGroup = userSubset.groupby(['userId'])
    userSubsetGroup = sorted(userSubsetGroup,  key=lambda x: len(x[1]), reverse=True)
    userSubsetGroup = userSubsetGroup[0:100]
    
    pearsonCorrelationDict = {}

    for name, group in userSubsetGroup:

        group = group.sort_values(by='recipeId')
        inputMovies = inputRecipes.sort_values(by='recipeId')

        nRatings = len(group)

        temp_df = inputRecipes[inputRecipes['recipeId'].isin(group['recipeId'].tolist())]

        tempRatingList = temp_df['rating'].tolist()
        tempGroupList = group['rating'].tolist()

        Sxx = sum([i**2 for i in tempRatingList]) - pow(sum(tempRatingList),2)/float(nRatings)
        Syy = sum([i**2 for i in tempGroupList]) - pow(sum(tempGroupList),2)/float(nRatings)
        Sxy = sum( i*j for i, j in zip(tempRatingList, tempGroupList)) - sum(tempRatingList)*sum(tempGroupList)/float(nRatings)

        if Sxx != 0 and Syy != 0:
            pearsonCorrelationDict[name] = Sxy/np.sqrt(Sxx*Syy)
        else:
            pearsonCorrelationDict[name] = 0
            
    pearsonDF = pd.DataFrame.from_dict(pearsonCorrelationDict, orient='index')
    
    pearsonDF.columns = ['similarityIndex']
    pearsonDF['userId'] = pearsonDF.index
    pearsonDF.index = range(len(pearsonDF))
    
    topUsers=pearsonDF.sort_values(by='similarityIndex', ascending=False)[0:50]
    
    topUsersRating = topUsers.merge(ratings_df, left_on='userId', right_on='userId', how='inner')
    topUsersRating['weightedRating'] = topUsersRating['similarityIndex']*topUsersRating['rating']
    
    tempTopUsersRating = topUsersRating.groupby('recipeId').sum()[['similarityIndex','weightedRating']]
    tempTopUsersRating.columns = ['sum_similarityIndex','sum_weightedRating']
    
    recommendation_df = pd.DataFrame()
    recommendation_df['weighted average recommendation score'] = tempTopUsersRating['sum_weightedRating']/tempTopUsersRating['sum_similarityIndex']
    recommendation_df['recipeId'] = tempTopUsersRating.index
    
    recommendation_df = recommendation_df.sort_values(by='weighted average recommendation score', ascending=False)
    
    display = recipes_df.loc[recipes_df['recipeId'].isin(recommendation_df.head(20)['recipeId'].tolist())]
    
    return display
  
  
  # example
get_recommendation()


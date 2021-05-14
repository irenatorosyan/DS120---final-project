import numpy as np
import pandas as pd
import random

recipes_df = pd.read_csv('allrecipes.csv', usecols = ["TITLES", "LINKS"])
recipes_df["recipeId"] = recipes_df.index+1
recipes_df = recipes_df[["recipeId", "TITLES", "LINKS"]]
recipes_df.head()

# creating fake dataset of ratings
userId = []
triedRecipeId = []
triedRecipeLiking = []
count = 0

for user in range(1,500):
    for numberOfTriedRecipes in range(random.randint(300, 400)):
        recipe = random.randint(1, len(recipes_df["recipeId"]))
        userId.append(user)
        triedRecipeId.append(recipe)
        triedRecipeLiking.append(random.randint(0, 5))
        count += numberOfTriedRecipes

ratings_df = pd.DataFrame(list(zip(userId, triedRecipeId, triedRecipeLiking)), columns =["userId", "recipeId", "rating"]) 
ratings_df = ratings_df.drop_duplicates(["userId", "recipeId"])
ratings_df

ratings_df.to_csv('ratings.csv', index = False)

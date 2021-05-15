# DS120---final-project

## Notes 

The folder "rawData" is not used in the project. It is for reference only.

The comments and explanations of the code used in the website are present in the files "matchReccomend" and "reccomender". Other files with the extension ipynb also have comments. 

The "main" branch contains all files, the "website" branch contains only files needed for the work of the website.

## Description

The "Meal Prepper" is a tool for finding suitable recipes for the user. We used multiple approaches to suggest recipes. The steps and the methods that we used will be explained in the following paragraphs. 

We started with scraping the data from a website called "SimplyRecipes". We scraped recipes from all sections and combined the data in a single big CSV document. 
For the first approach, we take input from the user, which contains ingredients that they currently have in their fridge and pantry. We then match the ingredients to the ingredients of all recipes that we previously scraped and suggest the possible recipes that contain all ingredients as an input to the user. The output includes the name of the recipe, the ingredients, and the URL combined in a data frame. The user can also move the slider in order to choose how many recipes they want to be displayed on the website. 

For the second approach, we use the information that the user previously gave as an input to analyze which ingredients they used the most and suggest recipes based on the obtained data. The suggestions include recipes with their top one ingredient, top two ingredient, and top one and two ingredients combined ( if they are proper :) ). 

For the third approach, we ask the user to input some recipes and rate each of them based on their preferences. We later find other users with similar likings by using the Pearson correlation coefficient. Then we calculate the weighted rating for each recipe and suggest the top twenty recipes with the highest ranking. Unfortunately, as we do not have real users, the ratings are generated, thus the recommendations are not always the best.
For creating the website, we used "Streamlit" and later uploaded the website to "Heroku" to make it accessible. 

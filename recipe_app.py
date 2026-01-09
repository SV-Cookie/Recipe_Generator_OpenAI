
import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import langchain_community
from langchain_openai import ChatOpenAI 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) #ignoring deprecation warnings from langchain

template = """
You are a nutritionist and chef who takes the specifications of the user into account before genrating a recipe to the user's liking

Given the following specifications to the meal(if one or more are specified): 
Allergens(must be avoided/excluded in dish): {allergens}
Cuisine(try to be as close as possible): {cuisine}
Macros/Nutrients(must follow): {macros_nutrients}
Meal Setting: {meal_setting}
Type of Meal: {type_of_meal}

keep the meal, easy to make (not more than 30 mins can can be done using a pan or an oven or without a flame for example) and as cheap as 
possible (under 10$ per meal) while adhering to all the specifications provided

Please suggest a recipe that can be made with these conditions. Include instructions to make the make the recipe.

Recipe:
""" 

prompt = PromptTemplate.from_template(template)  #changed to take parameters direclty from template rather than keying everything

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7, max_completion_tokens=900)

recipe_generator = prompt | llm | StrOutputParser()

st.title("GPT Ramsay 🧑🏽‍🍳")

st.divider()

st.write("Tell me what you would like to have and I'll give you something delicious to eat...")


allergens = st.text_input("Any allergens to avoid? or restrictions for foods you dont want to eat (separated by commas): ")
cuisine = st.text_input("Preferred cuisine type? (e.g., Italian, Chinese, ?): ")
macros_nutrients = st.text_input("Any specific nutritional requirements or macros to consider? (e.g., high protein, low carb, high in fibre?) (separated by commas): ")
meal_setting = st.text_input("What / Who is this meal for? (post-workout-snack, breakfast to go, meal-prep, potluck?): ")
type_of_meal = st.text_input("Craving something specific?, (Noodles, Salad, Cake, Rice dish?): ")



st.divider()


if st.button("Lets Cook!"):
    if allergens or cuisine or macros_nutrients or meal_setting or type_of_meal:

        st.write("Finding my lamb sauce...")
        

        recipe = recipe_generator.invoke({"allergens" : allergens, "cuisine" : cuisine, "macros_nutrients" : macros_nutrients, "meal_setting" : meal_setting,
                                           "type_of_meal" : type_of_meal})
        st.write(recipe)
        st.warning("Note: This recipe is generated using an AI model and can be inncaurate or wrong. Always verify with a trusted doctor "
        "or consult a nutritionist for more accurate information")

    else:
        st.error("Please enter some conditions to proceed.")


#make the progress bar go to 100 after the recipe is generated then disappear 
#add a bar for allergens or dietary restrictions
#add an option for cuisine type or meal type (breakfast, lunch, dinner, snack)
#add one for nutrition facts to be specified or if not to just provide all nutrition values
#what or why are you cooking this meal?


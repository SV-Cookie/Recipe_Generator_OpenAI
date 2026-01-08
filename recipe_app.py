
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
You are a chef who creates recipes based on the ingredients provided.
Given the following ingredients: {ingredients},

Please suggest a recipe that can be made with these ingredients. Include instructions to make the make the recipe.

Recipe:
""" #what is the """ used for and what is template

prompt = PromptTemplate(
    input_variables=["ingredients"],
    template=template
)

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7, max_completion_tokens=900)

recipe_generator = prompt | llm | StrOutputParser()

st.title("GPT Ramsay 🧑🏽‍🍳")

st.divider()

st.write("Give me the ingredients you have and I'll give you something delicious to eat...")

ingredients = st.text_area("Enter the ingredients you have (separated by commas):")

st.divider()

if st.button("Lets Cook!"):
    if ingredients:

        st.progress(0.5, text = "Finding my lamb sauce...")

        recipe = recipe_generator.invoke({"ingredients" : ingredients})
        st.write(recipe)

    else:
        st.error("Please enter some ingredients to proceed.")

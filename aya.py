import replicate
import os
from dotenv import load_dotenv
import cohere
import streamlit as st

# method to get values of environment varaibles from .env file 
load_dotenv('.env')

def get_aya_response(language, text):
    cohere_api_key = os.getenv("COHERE_API_TOKEN")
    co = cohere.Client(cohere_api_key)
    response = co.generate(
    model='c4ai-aya',
    prompt=f'Translate the given text in quotes in {language}: "{text}"',
    temperature=0,
    k=1,
    stop_sequences=[],
    return_likelihoods='NONE')
    response = response.generations[0].text
    return response
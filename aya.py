import replicate
import os
from dotenv import load_dotenv
import cohere
import streamlit as st

#method to get values of environment varaibles from .env file 
load_dotenv('.env')

# #Configuring Gemini API with the API key
# replicate_api_key = os.getenv("REPLICATE_API_TOKEN")

# print(replicate_api_key)

# replicate_api = replicate.Client(api_token=replicate_api_key)

# output = replicate_api.run(
#     "zsxkib/aya-101:b2a6d6e351509d2b7a88ab9997b84344e332618fcc161f8baec88fac8a97bed6",
#     input={
#         # "prompt": "Translate to English: আমি জ্যাক এবং আমি একজন সফটওয়্যার ডেভেলপার."
#         "prompt": "Translate to Bengali: we can think of an application that will scan the directions or something written and translate and answer  the questions in native language of the user"
#     }
# )
# print(output)


def get_aya_response(language, text):
    # st.write(f'Translate the given text in quotes in {language}: "{text}"')
    cohere_api_key = os.getenv("COHERE_API_TOKEN")
    co = cohere.Client(cohere_api_key) # This is your API key
    response = co.generate(
    model='c4ai-aya',
    prompt=f'Translate the given text in quotes in {language}: "{text}"',
    # max_tokens=300,
    temperature=0,
    k=1,
    stop_sequences=[],
    return_likelihoods='NONE')
    response = response.generations[0].text
    return response
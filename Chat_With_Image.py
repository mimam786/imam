import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import aya

load_dotenv('.env')

if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'query' not in st.session_state:
    st.session_state.query = ""
if 'selected_language' not in st.session_state:
    st.session_state.selected_language = ""

api_key = os.getenv("GEMINI_API_KEY")
# print(api_key)
genai.configure(api_key=api_key)

# for model in genai.list_models():
#     print(model.name)

language_options = ('BENGALI', 'HINDI','IRISH','MALAY (STANDARD)','PERSIAN (WESTERN)','SHONA','SINHALA','SWEDISH','TAMIL','TELUGU','THAI','TURKISH','URDU','VIETNAMESE','ZULU')

def get_gemini_vision_response(query,image):
    vision_model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = vision_model.generate_content([query,image])
    else:
       response = vision_model.generate_content(image)
    return response.text

def get_gemini_text_response(chat_query):
    text_model = genai.GenerativeModel('gemini-pro')
    if chat_query!="":
       #Get Chat Response:
        chat = text_model.start_chat()
        response = chat.send_message(chat_query)
        # print(response.text)
    return response.text

uploaded_file = st.file_uploader("Upload a file", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

selected_language = st.selectbox('Choose your language of response',language_options)
query=st.chat_input("Enter your quesion here... ",key="input")
# submit=st.button("Ask")

## If ask button is clicked

if query:
    with st.chat_message("user"):
        st.write(query)
        
    gemini_response=get_gemini_vision_response(query,image)
    translated_response = aya.get_aya_response(selected_language, gemini_response)
    # st.subheader("The Response is")
    st.markdown('Response in English: '+gemini_response)
    st.markdown(f'Response in {selected_language}: '+translated_response)



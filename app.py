from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load .env file
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Choose Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")
# model = genai.GenerativeModel("gemini-1.5-pro")

def my_output(query):
    response = model.generate_content(query)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Mattie_bot")
st.header("Mattie_bot")

input_text = st.text_input("Input", key="input")
submit = st.button("Ask your query")

if submit:
    response = my_output(input_text)
    st.subheader("The Response is =")
    st.write(response)

import streamlit as st
import pandas as pd
import openai
from secrets import openai_api_key

# Load user queries from TXT file
user_queries = pd.read_csv(r"D:\project\recruite_app\user_queries.txt")

# Define a function to query GPT-4
def query_gpt4(prompt):
    openai.api_key = openai_api_key
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Create a Streamlit interface
st.title("AI Recruiter Chatbot")

# Get user input
user_input = st.text_input("Enter your query:")

# Query GPT-4 and display response
if st.button("Get Response"):
    response = query_gpt4(user_input)
    st.write(f"Chatbot Response: {response}")

openai_api_key = st.secrets ["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"]
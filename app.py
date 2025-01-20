import streamlit as st
import pandas as pd

# Load API key from Streamlit secrets
openai_api_key = st.secrets["openai_api_key"]

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
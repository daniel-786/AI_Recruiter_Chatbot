import streamlit as st
import pandas as pd
import openai

# Load API key from Streamlit secrets
openai_api_key = st.secrets["openai_api_key"]

# Load user queries from TXT file (error handling added)
try:
    user_queries = pd.read_csv(r"D:\project\recruite_app\user_queries.txt")
except FileNotFoundError:
    user_queries = pd.DataFrame(columns=["query"])
    st.warning("User queries file not found. Starting with an empty query list.")

# Define a function to query GPT-4
def query_gpt4(prompt):
    openai.api_key = openai_api_key
    try:
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"Error querying GPT-4: {e}")
        return "An error occurred while querying GPT-4."

# Create a Streamlit interface
st.title("AI Recruiter Chatbot")

# Display past user queries (optional)
st.subheader("Past User Queries")
st.write(user_queries)

# Get user input
user_input = st.text_input("Enter your query:")

# Query GPT-4 and display response
if st.button("Get Response") and user_input:
    response = query_gpt4(user_input)
    st.write(f"Chatbot Response: {response}")
else:
    st.warning("Please enter a query.")

import streamlit as st
import pandas as pd
import openai

# Load API key from Stressamlit secrets
openai_api_key = st.secrets["openai_api_key"]

# Load user queries from TXT file (error handling added)
try:
    user_queries = pd.read_csv(r"D:\project\recruite_app\user_queries.txt")
except FileNotFoundError:
    user_queries = pd.DataFrame(columns=["query"])
    st.warning("User queries file not found. Starting with an empty query list.")

# Define a function to query ChatGPT 4.0 Mini
def query_chatgpt(prompt):
    openai.api_key = openai_api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        st.error(f"Error querying ChatGPT 4.0 Mini: {e}")
        return "An error occurred while querying ChatGPT 4.0 Mini."

# Create a Streamlit interface
st.title("AI Recruiter Chatbot")

# Display past user queries (optional)
st.subheader("Past User Queries")
st.write(user_queries)

# Get user input
user_input = st.text_input("Enter your query:")

# Query ChatGPT 4.0 Mini and display response
if st.button("Get Response") and user_input:
    response = query_chatgpt(user_input)
    st.write(f"Chatbot Response: {response}")
else:
    st.warning("Please enter a query.")

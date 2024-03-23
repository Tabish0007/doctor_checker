import streamlit as st
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# Set up OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Initialize ChatOpenAI model
chat = ChatOpenAI(temperature=0)

def get_doctor_response(query):
    messages = [
        SystemMessage(content="You are a doctor AI assistant named Doctor AI. Your task is to diagnose diseases based on the provided symptoms and suggest appropriate medications."),
        HumanMessage(content=query)
    ]

    try:
        response = chat(messages)
        return response.content
    except Exception as e:
        return f"Error: {e}"

# Streamlit app
st.set_page_config(page_title="Doctor AI", page_icon="💊")
st.header("Welcome to Doctor AI 👋")

query = st.text_area("Enter your symptoms:")

if st.button("Get Diagnosis and Medication"):
    with st.spinner("Analyzing symptoms..."):
        response = get_doctor_response(query)
        st.success(response)

# Instructions
st.markdown("""
### Instructions
- Enter your symptoms in the text area.
- Click the "Get Diagnosis and Medication" button.
- The AI doctor will analyze your symptoms and provide a diagnosis along with suggested medications.
""")

# Note
st.warning("Note: This app is for informational purposes only and should not be used as a substitute for professional medical advice. Always consult a qualified healthcare provider for any medical concerns.")
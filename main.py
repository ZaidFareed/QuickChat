import streamlit as st
import openai
import os

# Theme configuration and custom styles for an attractive UI
st.set_page_config(page_title="QuickChat", layout="wide")

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY") or "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"

def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
            
        )
        return response.choices[0].message['content']
    except Exception as e:
        return str(e)

# UI elements
st.title("QuickChat")
user_input = st.text_input("Type your message:", "", placeholder="Ask me anything...")

if user_input:
    gpt_response = get_gpt_response(user_input)
    st.text_area("Response", value=gpt_response, height=200, max_chars=None, key=None)

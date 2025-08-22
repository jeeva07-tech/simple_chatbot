import streamlit as st
import google.generativeai as genai


# Setup Gemini API

genai.configure(api_key="AIzaSyA2856gIM1OlwgBzj1eikdY_0QiNcjKP8E")

# Choose model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("🤖 Simple Naruto Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Show chat history
for role, text in st.session_state["messages"]:
    if role == "user":
        st.chat_message("user").markdown(text)
    else:
        st.chat_message("assistant").markdown(text)

# User input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state["messages"].append(("user", prompt))
    st.chat_message("user").markdown(prompt)

    # Get response from Gemini
    response = model.generate_content(prompt)
    reply = response.text

    # Add bot message
    st.session_state["messages"].append(("assistant", reply))
    st.chat_message("assistant").markdown(reply)



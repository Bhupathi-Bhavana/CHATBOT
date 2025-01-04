import os
import json
import random
import streamlit as st

# Load intents.json
def load_intents(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Define a function to get a response based on user input
def chatbot_response(user_input, intents):
    user_input = user_input.lower()
    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(intent["responses"])
    return "Sorry, I didn't understand that. Can you rephrase?"

# Streamlit UI
st.set_page_config(page_title="Smart Chatbot", layout="wide")

# Center-align the title
st.markdown("<div style='text-align: center;'><h1>Chatbot Wizard 🧙‍♂️🤖</h1></div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'><h3>Welcome to the Chatbot! How can I assist you today?</h3></div>", unsafe_allow_html=True)

# Load intents from file
intents_file_path = "chatbot/intents.json"
intents = load_intents(intents_file_path)

# Initialize messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat container with messages
st.markdown("<div style='display: flex; flex-direction: column; max-height: 500px; overflow-y: auto; padding: 10px;'>", unsafe_allow_html=True)
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"<div style='text-align: right; background-color: #f0f0f0; padding: 10px; margin: 5px; border-radius: 5px;'>{message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; background-color: #d4f4dd; padding: 10px; margin: 5px; border-radius: 5px;'>{message['content']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Input box for user
user_input = st.text_area("Type your message here", "", height=60)

# Handle message sending
if st.button("Submit"):
    if user_input.strip():  # Check if the user input is not empty
        # Store the message in the session state
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get the chatbot's response
        response = chatbot_response(user_input, intents)
        st.session_state.messages.append({"role": "chatbot", "content": response})

# Footer section
st.markdown(
    "<div style='position: fixed; bottom: 10px; right: 10px; text-align: right; font-size: 14px; opacity: 0.7; transition: opacity 0.3s;' onmouseover='this.style.opacity=1' onmouseout='this.style.opacity=0.7;'>" +
    "<p>Created by <a href='https://github.com/Bhupathi-Bhavana/Implementation-Of-Chatbot-Using-NLP' target='_blank'>Bhavana Bhupathi</a></p>" +
    "</div>",
    unsafe_allow_html=True
)

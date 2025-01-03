# Smart Chatbot Wizard 🧙‍♂️🤖

Welcome to the **Smart Chatbot Wizard**! This is an interactive chatbot built using Natural Language Processing (NLP). It can respond to user input based on predefined patterns and responses, providing a fun and intelligent interaction.

## Features

<div style="border: 2px solid #4CAF50; padding: 10px; border-radius: 5px; background-color: #f0f8f0; margin-bottom: 10px;">
  <h3>Chat Interface</h3>
  <p>A clean, user-friendly interface where you can chat with the bot.</p>
</div>

<div style="border: 2px solid #4CAF50; padding: 10px; border-radius: 5px; background-color: #f0f8f0; margin-bottom: 10px;">
  <h3>Dynamic Response Generation</h3>
  <p>The chatbot provides dynamic responses based on user input.</p>
</div>

<div style="border: 2px solid #4CAF50; padding: 10px; border-radius: 5px; background-color: #f0f8f0; margin-bottom: 10px;">
  <h3>Session Management</h3>
  <p>Keeps track of the conversation history between the user and the bot.</p>
</div>

<div style="border: 2px solid #4CAF50; padding: 10px; border-radius: 5px; background-color: #f0f8f0; margin-bottom: 10px;">
  <h3>Interactive</h3>
  <p>Designed to help users with queries and provide relevant information.</p>
</div>

Steps to Run the Chatbot
Step 1: Clone the Repository
Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/Bhupathi-Bhavana/Implementation-Of-Chatbot-Using-NLP.git
Step 2: Install Dependencies
Make sure you have Python installed. Then, install the necessary dependencies by running:

bash
Copy code
pip install -r requirements.txt
Step 3: Run the Chatbot
Once the dependencies are installed, run the following command to start the chatbot app:

bash
Copy code
streamlit run app.py
This will launch the chatbot app in your browser.

Usage
Enter Your Message: Type your query or message into the text box on the left.
Submit: Press the "Submit" button to send your message to the chatbot.
Chat with the Bot: The bot will reply based on predefined responses.
Conversation History: The conversation between you and the chatbot will be displayed on the screen.
Customizing Intents
The chatbot uses an intents.json file that stores different patterns (keywords) and their corresponding responses.

You can modify the intents.json file to add new intents, patterns, and responses according to your requirements.

Sample intents.json Format:
json
Copy code
[
  {
    "intent": "greeting",
    "patterns": ["hi", "hello", "hey"],
    "responses": ["Hello! How can I assist you today?", "Hi there! How can I help you?"]
  },
  {
    "intent": "goodbye",
    "patterns": ["bye", "goodbye", "see you"],
    "responses": ["Goodbye! Have a great day!", "See you later!"]
  },
  {
    "intent": "thanks",
    "patterns": ["thanks", "thank you", "thanks a lot"],
    "responses": ["You're welcome!", "Glad I could help!", "Anytime!"]
  }
]
Structure:
Patterns: A list of input patterns (phrases) that the chatbot can recognize.
Responses: A list of responses the bot will give when it matches any of the patterns.
Technologies Used
Streamlit: For building the interactive user interface.
Python: The main programming language used to build the chatbot.
JSON: Used to store intents, patterns, and responses for easy customization.
NLP: Natural Language Processing techniques for understanding and responding to user input.
Contributions
If you would like to contribute to the project, feel free to fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Created By
Bhavana Bhupathi





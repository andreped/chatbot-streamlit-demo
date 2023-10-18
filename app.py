import json

import streamlit as st
from src.utils import download_test_data
from src.utils import load_data

# Initialize message history
st.header("Chat with André's research 💬 📚")

if "messages" not in st.session_state.keys():  # Initialize the chat message history
    st.session_state.messages = [{"role": "assistant", "content": "Ask me a question about André's research!"}]

# Load config values
with open(r"config.json") as config_file:
    config_details = json.load(config_file)


def main():
    # setup dataset
    download_test_data()
    index = load_data(config_details)
    chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

    if prompt := st.chat_input("Your question"):  # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages:  # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # If last message is not from assistant, generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message)  # Add response to message history


if __name__ == "__main__":
    main()

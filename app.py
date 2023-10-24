import os

import streamlit as st

from chatbot import redirect as rd
from chatbot.data import download_test_data
from chatbot.data import load_data

# add OpenAI API key to environemntal variables
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Initialize message history
st.header("Chat with André's research 💬 📚")

if "messages" not in st.session_state.keys():  # Initialize the chat message history
    st.session_state.messages = [{"role": "assistant", "content": "Ask me a question about André's research!"}]

def main():
    # setup logger sidebar
    #st.sidebar.text("Standard output log:")
    #_sidebar_out = st.sidebar.empty()
    #with rd.stdout(to=_sidebar_out, format='text'):
    #    print("test")

    # setup dataset
    download_test_data()
    index = load_data()
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

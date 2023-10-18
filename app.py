import json
import os

import streamlit as st
from gdown import download_folder
from llama_index import ServiceContext
from llama_index import SimpleDirectoryReader
from llama_index import VectorStoreIndex
from llama_index import set_global_service_context
from llama_index.embeddings import OpenAIEmbedding
from llama_index.llms import AzureOpenAI


# Initialize message history
st.header("Chat with André's research 💬 📚")

if "messages" not in st.session_state.keys():  # Initialize the chat message history
    st.session_state.messages = [{"role": "assistant", "content": "Ask me a question about André's research!"}]

# Load config values
with open(r"config.json") as config_file:
    config_details = json.load(config_file)


def download_test_data():
    url = "https://drive.google.com/drive/folders/1uDSAWtLvp1YPzfXUsK_v6DeWta16pq6y"
    with st.spinner(text="Downloading test data. Might take a few seconds."):
        download_folder(url, quiet=True, use_cookies=False, output="./data/")


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the provided dataset – hang tight! This may take a few seconds."):
        documents = SimpleDirectoryReader(input_dir="./data", recursive=True).load_data()
        llm = AzureOpenAI(
            model="gpt-3.5-turbo",
            engine=config_details["ENGINE"],
            temperature=0.5,
            api_key=os.getenv("OPENAI_API_KEY"),
            api_base=config_details["OPENAI_API_BASE"],
            api_type="azure",
            api_version=config_details["OPENAI_API_VERSION"],
            system_prompt="You are an expert on André's research and your job is to answer"
            "technical questions. Assume that all questions are related to"
            "André's research. Keep your answers technical and based on facts"
            " – do not hallucinate features.",
        )
        # You need to deploy your own embedding model as well as your own chat completion model
        embed_model = OpenAIEmbedding(
            model="text-embedding-ada-002",
            deployment_name=config_details["ENGINE_EMBEDDING"],
            api_key=os.getenv("OPENAI_API_KEY"),
            api_base=config_details["OPENAI_API_BASE"],
            api_type="azure",
            api_version=config_details["OPENAI_API_VERSION"],
        )
        service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)
        set_global_service_context(service_context)
        index = VectorStoreIndex.from_documents(documents)  # , service_context=service_context)
        return index


def main():
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

import os

import streamlit as st
from gdown import download_folder
from llama_index import ServiceContext
from llama_index import SimpleDirectoryReader
from llama_index import VectorStoreIndex
from llama_index import set_global_service_context
from llama_index.embeddings import OpenAIEmbedding
from llama_index.llms import AzureOpenAI


@st.cache_resource(show_spinner=False)
def download_test_data():
    # url = f"https://drive.google.com/drive/folders/uc?export=download&confirm=pbef&id={file_id}"
    url = "https://drive.google.com/drive/folders/1uDSAWtLvp1YPzfXUsK_v6DeWta16pq6y"
    with st.spinner(text="Downloading test data. Might take a few seconds."):
        download_folder(url=url, quiet=False, use_cookies=False, output="./data/")


@st.cache_resource(show_spinner=False)
def load_data(config_details):
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

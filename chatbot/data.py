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
    with st.spinner(text="Downloading test data. This might take a minute."):
        # @TODO: replace gown solution with a custom solution compatible with GitHub and
        # use st.progress to get more verbose during download
        download_folder(url=url, quiet=False, use_cookies=False, output="./data/")


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the provided dataset – hang tight! This may take a few seconds."):
        documents = SimpleDirectoryReader(input_dir="./data", recursive=True).load_data()

    with st.spinner(text="Setting up Azure OpenAI..."):
        llm = AzureOpenAI(
            model="gpt-3.5-turbo",
            engine=os.environ["ENGINE"],
            temperature=0.5,
            api_key=os.environ["OPENAI_API_KEY"],
            api_base=os.environ["OPENAI_API_BASE"],
            api_type="azure",
            api_version=os.environ["OPENAI_API_VERSION"],
            system_prompt="You are an expert on André's research and your job is to answer"
            "technical questions. Assume that all questions are related to"
            "André's research. Keep your answers technical and based on facts;"
            " do not hallucinate features.",
        )

    with st.spinner(text="Setting up OpenAI Embedding..."):
        # You need to deploy your own embedding model as well as your own chat completion model
        embed_model = OpenAIEmbedding(
            model="text-embedding-ada-002",
            deployment_name=os.environ["ENGINE_EMBEDDING"],
            api_key=os.environ["OPENAI_API_KEY"],
            api_base=os.environ["OPENAI_API_BASE"],
            api_type="azure",
            api_version=os.environ["OPENAI_API_VERSION"],
            embed_batch_size=10,  # set to low value to reduce rate limit -> may degrade response runtime
        )

    with st.spinner(text="Setting up Vector Store Index..."):
        service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)  # , chunk_size=512)
        set_global_service_context(service_context)
        index = VectorStoreIndex.from_documents(documents)  # , service_context=service_context)
        return index

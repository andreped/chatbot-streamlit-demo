import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, set_global_service_context
from llama_index.llms import AzureOpenAI
from llama_index.embeddings import OpenAIEmbedding
import json
import os
from llama_index import SimpleDirectoryReader


# Load config values
with open(r'config.json') as config_file:
    config_details = json.load(config_file)

# Initialize message history
st.header("Chat with André's research 💬 📚")

if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about André's research!"}
    ]


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the Streamlit docs – hang tight! This should take 1-2 minutes."):
        documents = SimpleDirectoryReader(input_dir="./data", recursive=True).load_data()
        llm = AzureOpenAI(
            model="gpt-3.5-turbo",
            engine="chatbot-streamlit",
            temperature=0.5,
            api_key=os.getenv("OPENAI_API_KEY"),
            api_base=config_details['OPENAI_API_BASE'],
            api_type="azure",
            api_version=config_details['OPENAI_API_VERSION'],
            system_prompt="You are an expert on the Streamlit Python library and your job is to answer technical questions. Assume that all questions are related to the Streamlit Python library. Keep your answers technical and based on facts – do not hallucinate features."
        )
        # You need to deploy your own embedding model as well as your own chat completion model
        embed_model = OpenAIEmbedding(
            model="text-embedding-ada-002",
            deployment_name="chatbot-streamlit-embedding",
            api_key=os.getenv("OPENAI_API_KEY"),
            api_base=config_details['OPENAI_API_BASE'],
            api_type="azure",
            api_version=config_details['OPENAI_API_VERSION'],
        )
        service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)
        set_global_service_context(service_context)
        index = VectorStoreIndex.from_documents(documents) #, service_context=service_context)
        return index


def main():
    index = load_data()

    chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

    if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages: # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # If last message is not from assistant, generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message) # Add response to message history


if __name__ == "__main__":
    main()

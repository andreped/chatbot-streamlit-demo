# chatbot-streamlit-demo

This application demonstrates how to setup a simple ChatBot with Azure OpenAI and StreamLit.

The ChatBot enables you to talk with your own data - in this case, to learn about André's research.

## Getting Started

These instructions were tested on a MacBook Pro with M2 chip running macOS 13.6 Ventura with Python 3.9.6.

1. Setup virtual environment and install dependencies:
```
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

2. Set OPENAI_API_KEY:
```
export OPENAI_API_KEY=<insert key here>
```

3. Create the `config.json` file and fill in the relevant info:
```
{
    "CHATGPT_MODEL":"<insert model name>",
    "OPENAI_API_BASE":"https://<insert-openai-service-name>.openai.azure.com",
    "OPENAI_API_VERSION":"<insert version>",
    "ENGINE": "<insert deployment model name>",
    "ENGINE_EMBEDDING": "<insert deployment embedding name>"
}
```

4. Launch the app:
```
streamlit run app.py
```

A Streamlit browser window should automatically open. If not, the app can be accessed at `http://localhost:8501`

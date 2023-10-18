# chatbot-streamlit-demo

This application demonstrates how to setup a simple ChatBot with [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) and [Streamlit](https://streamlit.io).

The ChatBot enables you to talk with your own data - in this case, to learn about [André's research](https://scholar.google.com/citations?user=U20zUHQAAAAJ).

## Getting Started

These instructions were tested on a MacBook Pro with M2 chip running macOS 13.6 Ventura with `Python 3.9.6`.

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

## Demonstration

Below is a snapshot on how the UI should look. A live demo may be made openly available in the future.

<img width="800" alt="Screenshot 2023-10-18 at 13 06 51" src="https://github.com/andreped/chatbot-streamlit-demo/assets/29090665/0e367153-9f0e-48d6-8059-dd060f917a97">

## License

The code in this repository is released under [MIT license](https://github.com/andreped/chatbot-streamlit-demo/blob/main/LICENSE).

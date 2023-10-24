# chatbot-streamlit-demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-app-demo.streamlit.app)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

This application demonstrates how to setup a simple ChatBot with [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service), [llama-index](https://docs.llamaindex.ai/en/stable/), and [Streamlit](https://streamlit.io).

The ChatBot enables you to talk with your own data - in this case, to learn about [André's research](https://scholar.google.com/citations?user=U20zUHQAAAAJ).

## Demo [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-app-demo.streamlit.app)

A demo is hosted publicly at Streamlit at [https://chatbot-app-demo.streamlit.app](https://chatbot-app-demo.streamlit.app).

A snapshot of the UI can be seen below:

![Screenshot 2023-10-24 at 12 02 22](https://github.com/andreped/chatbot-streamlit-demo/assets/29090665/8eebc228-07ff-4ab8-bbfd-c284f7572018)

## Development

If you wish to play around with the app locally, it requires that you provide OpenAI API key and all that fun stuff yourself.

These instructions were tested on a MacBook Pro with M2 chip running macOS 13.6 Ventura with `Python 3.9.6`.

1. Setup virtual environment and install dependencies:
```
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

2. Create the secrets file at `.streamlit/secrets.toml` file and fill in the relevant info:
```
OPENAI_API_KEY = "3cc19a1c875749c18c5e5d5a45a08f90"
CHATGPT_MODEL = "<insert model name>"
OPENAI_API_BASE = "https://<insert-openai-service-name>.openai.azure.com"
OPENAI_API_VERSION = "<insert version>"
ENGINE = "<insert deployment model name>"
ENGINE_EMBEDDING = "<insert deployment embedding name>"
```

3. Launch the app:
```
streamlit run app.py
```

A Streamlit browser window should automatically open. If not, the app can be accessed at `http://localhost:8501`

## Disclaimer

Only public PDFs were used for this demonstration. Some of André's research is sadly behind a paywall and thus we have chosen not to include the PDFs in this demo to avoid copyright issues.

## License

The code in this repository is released under [MIT license](https://github.com/andreped/chatbot-streamlit-demo/blob/main/LICENSE).

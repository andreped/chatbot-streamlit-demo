---
title: "ChatBot: learn about André's research through an AI assistant"
colorFrom: indigo
colorTo: indigo
sdk: streamlit
sdk_version: 1.27.2
app_port: 8501
emoji: 💬
pinned: false
license: mit
app_file: app.py
---

# chatbot-streamlit-demo

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
<a target="_blank" href="https://huggingface.co/spaces/andreped/chatbot-streamlit-demo"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow.svg"></a>
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-app-demo.streamlit.app)
[![CI/CD](https://github.com/raidionics/AeroPath/actions/workflows/deploy.yml/badge.svg)](https://github.com/raidionics/AeroPath/actions/workflows/deploy.yml)

This application demonstrates how to setup a simple ChatBot with [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service), [llama-index](https://docs.llamaindex.ai/en/stable/), and [Streamlit](https://streamlit.io).

The final app is also deployed on both [Streamlit](https://chatbot-app-demo.streamlit.app) and [Hugging Face Spaces](https://huggingface.co/spaces/andreped/chatbot-streamlit-demo), as well as embedded into a [personal website](https://andreped.github.io/demos/2023/chatbot/).

The ChatBot enables you to talk with your own data - in this case, to learn about [André's research](https://scholar.google.com/citations?user=U20zUHQAAAAJ).

## Demo

We have enabled live hosting through both Streamlit and Hugging Face spaces. Click on the respective badges below to access each:

#### Hugging Face Spaces <a target="_blank" href="https://huggingface.co/spaces/andreped/chatbot-streamlit-demo"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow.svg"></a>

![Screenshot 2023-10-24 at 13 44 15](https://github.com/andreped/chatbot-streamlit-demo/assets/29090665/610ed8f1-39e9-4842-ab5b-93847678812c)

#### Streamlit [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-app-demo.streamlit.app)

![Screenshot 2023-10-24 at 13 03 11](https://github.com/andreped/chatbot-streamlit-demo/assets/29090665/ba82787a-71fc-4d6c-9ae0-c11417df2841)

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

## Acknowledgements

I wish to thank [Sopra Steria](https://www.soprasteria.com) for giving me the chance to develop this web application on internal time. I also want to thank [OpenAI](https://openai.com), [Microsoft Azure](https://azure.microsoft.com/en-us), and the developers of [llama-index](https://www.llamaindex.ai), [Streamlit](https://streamlit.io), and [HuggingFace](https://huggingface.co) for making such great tools to make applications in.

## License

The code in this repository is released under [MIT license](https://github.com/andreped/chatbot-streamlit-demo/blob/main/LICENSE).

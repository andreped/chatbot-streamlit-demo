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

3. Download test data:
```
gdown https://drive.google.com/drive/folders/1uDSAWtLvp1YPzfXUsK_v6DeWta16pq6y -O ./data/ --folder
```

3. Launch the app:
```
streamlit run app.py
```

You can then access the app in your browser at `http://localhost:8501`

Alphra – AI-Powered Trade Signal Tool

How it works:
- Uses SMA crossover to generate BUY/SELL/HOLD signals
- GPT-3.5 explains signals in plain English
- Streamlit for frontend

Setup:
1. Clone repo and cd into it
2. Create virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Create .env file with:
   OPENAI_API_KEY=your_key_here
5. Run:
   streamlit run app.py

Security:
- .env is in .gitignore
- No keys or secrets are exposed
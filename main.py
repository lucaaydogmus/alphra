from dotenv import load_dotenv
import os
import openai
from data_loader import fetch_price_data
from signal_engine import sma_crossover_signal
from gpt_explainer import explain_signal

# === Step 1: Load GPT key ===
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# === Step 2: Fetch stock data ===
ticker = "AAPL"  # Change this if needed
df = fetch_price_data(ticker)

# === Step 3: Run SMA signal ===
signal = sma_crossover_signal(df)
print(f"Signal for {ticker}: {signal}")

# === Step 4: Get GPT explanation ===
explanation = explain_signal(ticker, signal)
print("Explanation:", explanation)
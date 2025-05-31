import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env at the module level
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_signal(ticker: str, signal: str, strategy: str = "SMA crossover") -> str:
    """
    Use GPT to explain the quant signal in plain English.

    :param ticker: Stock ticker (e.g., AAPL)
    :param signal: 'BUY', 'SELL', 'HOLD'
    :param strategy: Strategy name (default = SMA crossover)
    :return: Natural language explanation
    """
    prompt = f"""
You are a quantitative trading assistant. Explain the following signal clearly and concisely to a retail investor.

Ticker: {ticker}
Strategy: {strategy}
Signal: {signal}

Explain what this means, why it might have triggered, and what a user might consider doing. Avoid giving financial advice. Be clear, brief, and accurate.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error generating explanation: {e}"
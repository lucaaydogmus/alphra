import streamlit as st
from data_loader import fetch_price_data
from signal_engine import sma_crossover_signal
from gpt_explainer import explain_signal

st.set_page_config(page_title="Alphra", layout="centered")

st.title("📊 Alphra: Quant-Powered Trade Signals")
st.markdown("Enter a stock ticker to get real-time trade signals and explanations.")

# User input
symbol = st.text_input("Ticker Symbol (e.g., AAPL, TSLA):", value="AAPL")

if st.button("Analyze"):
    with st.spinner("Fetching data and analyzing..."):
        df = fetch_price_data(symbol)

        if df is not None and not df.empty:
            signal = sma_crossover_signal(df)
            explanation = explain_signal(symbol.upper(), signal)

            st.subheader(f"Signal for {symbol.upper()}: {signal}")
            st.markdown(f"**Explanation:** {explanation}")
        else:
            st.error("Failed to fetch data. Please check the ticker symbol.")
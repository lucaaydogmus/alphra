import pandas as pd

def sma_crossover_signal(df: pd.DataFrame, short_window=5, long_window=20) -> str:
    """
    Generates a simple SMA crossover signal.

    :param df: DataFrame with 'Close' prices
    :param short_window: Short-term SMA period
    :param long_window: Long-term SMA period
    :return: 'BUY', 'SELL', 'HOLD', or 'NO DATA'
    """
    if df.empty or "Close" not in df.columns:
        return "NO DATA"

    df = df.copy()
    df["SMA_short"] = df["Close"].rolling(window=short_window).mean()
    df["SMA_long"] = df["Close"].rolling(window=long_window).mean()

    df = df.dropna()

    if len(df) < 2:
        return "NO DATA"

    prev_short = df["SMA_short"].iloc[-2]
    prev_long = df["SMA_long"].iloc[-2]
    last_short = df["SMA_short"].iloc[-1]
    last_long = df["SMA_long"].iloc[-1]

    if prev_short < prev_long and last_short > last_long:
        return "BUY"
    elif prev_short > prev_long and last_short < last_long:
        return "SELL"
    else:
        return "HOLD"
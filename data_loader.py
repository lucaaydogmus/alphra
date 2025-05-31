import yfinance as yf
import pandas as pd


def fetch_price_data(ticker: str, period: str = "7d", interval: str = "1h") -> pd.DataFrame:
    """
    Fetch recent stock data for a given ticker.

    :param ticker: Stock symbol, e.g. 'AAPL'
    :param period: Time window, e.g. '1d', '5d', '7d', '1mo'
    :param interval: Time interval between data points, e.g. '1m', '5m', '1h', '1d'
    :return: DataFrame of OHLCV (Open, High, Low, Close, Volume) data
    """
    try:
        data = yf.download(ticker, period=period, interval=interval, progress=False)
        if data.empty:
            raise ValueError(f"No data returned for ticker: {ticker}")
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

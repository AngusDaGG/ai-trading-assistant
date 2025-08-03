
import requests, pandas as pd

BASE = "https://www.okx.com/api/v5/market/candles"

def fetch_kline(symbol="SOL-USDT", bar="1H", limit=200) -> pd.DataFrame:
    r = requests.get(BASE, params={"instId": symbol, "bar": bar, "limit": str(limit)}, timeout=10)
    r.raise_for_status()
    raw = r.json()["data"]
    cols = ["ts","open","high","low","close","vol","volCcy","volQuote","confirm"]
    df = pd.DataFrame(raw, columns=cols).iloc[::-1].reset_index(drop=True)
    df['ts'] = pd.to_datetime(df['ts'].astype(float), unit='ms')
    numeric = ["open","high","low","close","vol"]
    df[numeric] = df[numeric].astype(float)
    return df[['ts','open','high','low','close','vol']]

import requests, pandas as pd

BASE = "https://www.okx.com/api/v5/market/candles"

def fetch_kline(symbol="SOL-USDT", bar="1H", limit=200):
    resp = requests.get(BASE, params={"instId": symbol, "bar": bar, "limit": str(limit)}, timeout=10)
    resp.raise_for_status()
    data = resp.json()["data"]

    cols = ["ts","open","high","low","close","vol","volCcy","volQuote","confirm"]
    df = pd.DataFrame(data, columns=cols).iloc[::-1].reset_index(drop=True)
    df["ts"] = pd.to_datetime(df["ts"].astype(float), unit="ms")
    df[["open","high","low","close","vol"]] = df[["open","high","low","close","vol"]].astype(float)

    # ★ 在這裡把 vol 改名成 volume
    df = df.rename(columns={"vol": "volume"})

    # 回傳時也改成 volume
    return df[["ts","open","high","low","close","volume"]]

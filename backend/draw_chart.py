import io, base64, pandas as pd, mplfinance as mpf, pandas_ta as ta
def render_chart(df: pd.DataFrame, title="K-line"):
    df = df.set_index("ts")
    df["rsi"] = ta.rsi(df["close"], length=14)
    macd = ta.macd(df["close"])
    df = pd.concat([df, macd], axis=1)
    apds = [
        mpf.make_addplot(df["rsi"], panel=1, ylabel="RSI"),
        mpf.make_addplot(df["MACD_12_26_9"], panel=2, ylabel="MACD"),
        mpf.make_addplot(df["MACDs_12_26_9"], panel=2)
    ]
    buf = io.BytesIO()
    mpf.plot(df[["open","high","low","close"]], type="candle", style="yahoo",
             volume=True, addplot=apds, title=title,
             savefig=dict(fname=buf, dpi=120, bbox_inches="tight"))
    buf.seek(0)
    return "data:image/png;base64," + base64.b64encode(buf.read()).decode()

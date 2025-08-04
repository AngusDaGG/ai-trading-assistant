import io, base64
import pandas as pd
import mplfinance as mpf
import pandas_ta as ta   # ★ 需要這行

def render_chart(df: pd.DataFrame, title="K-line"):
    df = df.set_index("ts")

    # 技術指標
    df["rsi"] = ta.rsi(df["close"], length=14)
    macd = ta.macd(df["close"])
    df = pd.concat([df, macd], axis=1)

    apds = [
        mpf.make_addplot(df["rsi"], panel=1, ylabel="RSI"),
        mpf.make_addplot(df["MACD_12_26_9"], panel=2, ylabel="MACD"),
        mpf.make_addplot(df["MACDs_12_26_9"], panel=2),
    ]

    buf = io.BytesIO()
    # 帶 volume 欄一起繪圖
    mpf.plot(
        df[["open", "high", "low", "close", "volume"]],
        type="candle",
        style="yahoo",
        volume=True,
        addplot=apds,
        title=title,
        savefig=dict(fname=buf, dpi=120, bbox_inches="tight"),
    )
    buf.seek(0)
    return "data:image/png;base64," + base64.b64encode(buf.read()).decode()


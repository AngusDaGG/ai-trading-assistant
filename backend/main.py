from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from backend.fetch_okx import fetch_kline
from backend.draw_chart import render_chart

app = FastAPI(title="AI Trading Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/chart")
def chart(symbol: str = Query("SOL-USDT"), bar: str = Query("1H"), limit: int = Query(200, ge=1, le=1000)):
    df = fetch_kline(symbol, bar, limit)
    img = render_chart(df, title=f"{symbol} {bar}")
    return JSONResponse({"image": img})

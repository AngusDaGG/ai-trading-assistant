
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pathlib import Path
import base64, io
from fetch_okx import fetch_kline
from draw_chart import render_chart

app = FastAPI(title="AI Trading Assistant - Phase1")

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

@app.get("/")
def root():
    return {"msg": "API alive"}

@app.get("/chart")
def chart(symbol: str = Query("SOL-USDT"), bar: str = Query("1H"), limit: int = Query(200, ge=1, le=1000)):
    df = fetch_kline(symbol, bar, limit)
    img_b64 = render_chart(df, title=f"{symbol} {bar}")
    return JSONResponse({"symbol": symbol, "bar": bar, "image": img_b64})

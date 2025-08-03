
# AI Trading Assistant – Phase 1 (MVP)

功能：  
1. 前端 React – 輸入幣種、按一下就看到最新 K 線圖  
2. 後端 FastAPI – 自動向 OKX API 抓資料並使用 mplfinance 畫圖  
3. CORS 已開啟，前端與後端可分開部署或本機測試  

---

## 本機快速啟動

```bash
# 1. 後端
cd backend
python -m venv .venv && source .venv/bin/activate  # Windows 用 .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000            # http://localhost:8000/chart

# 2. 前端 (如果你裝了 Node.js + npm)
cd ../frontend
npm install
npm run dev                                       # http://localhost:5173
```

---

## 雲端部署 (Render 範例)

1. 登入 Render → New Web Service → 連接 GitHub Repo  
2. Root：`backend/`  
3. Build Command：`pip install -r requirements.txt`  
4. Start Command：`uvicorn main:app --host 0.0.0.0 --port $PORT`  

（前端可用 Vercel / Netlify 部署，或用 Render Static Site 指到 `frontend/`）

---

Made with ❤️  2025-08-03

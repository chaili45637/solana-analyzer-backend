from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from solana_utils import analyze_wallet_today

app = FastAPI()

# 允许前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze")
async def analyze(address: str = Query(..., description="Solana Wallet Address")):
    try:
        result = analyze_wallet_today(address)
        return result
    except Exception as e:
        return {"error": str(e)}
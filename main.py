from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许 CORS（前端跨域请求）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或指定你的前端地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Solana Analyzer API is running"}

@app.get("/analyze")
async def analyze(address: str):
    # 示例逻辑，替换成你自己的数据处理逻辑
    return {
        "address": address,
        "tx_count": 123,
        "buy_total": 12.5,
        "sell_total": 8.0,
        "fee_total": 0.2,
        "net_profit": 4.3,
        "total_value": 20.0
    }
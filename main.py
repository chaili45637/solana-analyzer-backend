# backend/main.py

from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from solana_utils import analyze_wallet
from fastapi.middleware.cors import CORSMiddleware
import datetime

app = FastAPI()

# 跨域配置，允许前端请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 根据需要设置允许的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeResponse(BaseModel):
    address: str
    tx_count: int
    buy_total: float
    sell_total: float
    fee_total: float
    net_profit: float
    asset_value: float
    related_addresses: list[str]
    risk_message: str
    transactions: list[dict]

@app.get("/analyze", response_model=AnalyzeResponse)
def analyze(
    address: str = Query(..., description="Solana钱包地址"),
    tx_type: Optional[str] = Query(None, description="交易类型过滤"),
    start_date: Optional[str] = Query(None, description="起始日期，格式YYYY-MM-DD"),
    end_date: Optional[str] = Query(None, description="结束日期，格式YYYY-MM-DD"),
):
    filters = {}
    if tx_type:
        filters["type"] = tx_type
    if start_date:
        try:
            filters["start_date"] = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        except:
            return {"error": "start_date格式错误，需YYYY-MM-DD"}
    if end_date:
        try:
            filters["end_date"] = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        except:
            return {"error": "end_date格式错误，需YYYY-MM-DD"}

    result = analyze_wallet(address, filters)
    return result
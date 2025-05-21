from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许跨域请求，方便前端调用API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境建议限制为你前端的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 根路径，返回简单消息用于健康检查
@app.get("/")
async def root():
    return {"message": "Solana Analyzer API is running"}

# 示例分析接口，接收钱包地址参数，返回模拟的分析结果
@app.get("/analyze")
async def analyze(address: str = Query(..., description="Solana wallet address to analyze")):
    # 这里可以替换为你自己的真实业务逻辑
    return {
        "address": address,
        "tx_count": 42,
        "buy_total": 12.5,
        "sell_total": 7.8,
        "fee_total": 0.15,
        "net_profit": 4.55,
        "total_value": 50.0
    }

# 你可以继续添加其他接口，例如下面的示例
@app.get("/api/transactions")
async def get_transactions():
    # 示例返回空交易列表
    return {"transactions": []}

@app.get("/api/asset_value")
async def get_asset_value():
    # 示例返回资产估值为0
    return {"asset_value": 0}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许所有来源跨域访问，部署时可以改成前端实际域名
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境建议填写具体前端地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Solana Analyzer API is running"}

@app.get("/api/transactions")
async def get_transactions():
    # 这里写你获取交易的逻辑，示例返回空数组
    return {"transactions": []}

@app.get("/api/asset_value")
async def get_asset_value():
    # 这里写你资产估值的逻辑，示例返回0
    return {"asset_value": 0}

# 示例新增一个分析接口
@app.get("/api/analyze")
async def analyze():
    # 这里写你分析的具体逻辑
    return {"analysis": "This is a placeholder for analysis result"}
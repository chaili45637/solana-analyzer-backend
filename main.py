# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 跨域设置，允许所有源访问，根据需求可修改
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 根路径，返回简单消息用于健康检查
@app.get("/")
async def root():
    return {"message": "Solana Analyzer API is running"}

# 这里是你之前所有的路由和逻辑，比如交易数据接口、分析接口等
# 下面是示例，替换为你的具体业务代码

@app.get("/api/transactions")
async def get_transactions():
    # 这里写你获取交易的逻辑
    return {"transactions": []}

@app.get("/api/asset_value")
async def get_asset_value():
    # 这里写你资产估值的逻辑
    return {"asset_value": 0}

# 继续添加你的其他API接口
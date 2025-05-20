# backend/solana_utils.py

import datetime

# 示例交易数据，真实环境请调用Solana RPC或API接口获取
sample_transactions = [
    {
        "tx_id": "tx1",
        "date": datetime.date(2025, 5, 1),
        "type": "NFT Buy",
        "amount": 2.5,
        "counterparty": "addr1",
        "fee": 0.0005,
        "success": True,
    },
    {
        "tx_id": "tx2",
        "date": datetime.date(2025, 5, 2),
        "type": "DeFi Stake",
        "amount": 10,
        "counterparty": "defi_contract",
        "fee": 0.001,
        "success": True,
    },
    {
        "tx_id": "tx3",
        "date": datetime.date(2025, 5, 3),
        "type": "Transfer",
        "amount": 1,
        "counterparty": "addr2",
        "fee": 0.0003,
        "success": True,
    },
    {
        "tx_id": "tx4",
        "date": datetime.date(2025, 5, 4),
        "type": "NFT Sell",
        "amount": 3,
        "counterparty": "addr3",
        "fee": 0.0007,
        "success": True,
    },
]

# 已知诈骗地址示例
known_scam_addresses = {"scammer1", "bad_actor_addr"}

def analyze_wallet(address: str, filters: dict):
    """
    分析钱包，根据过滤条件返回详细交易和统计信息
    filters可包含：
        - type: 交易类型过滤 (如 "NFT Buy", "DeFi Stake", "Transfer")
        - start_date: datetime.date类型，开始日期
        - end_date: datetime.date类型，结束日期
    """
    txs = sample_transactions  # 真实项目请替换为实际查询代码

    # 筛选交易
    filtered_txs = []
    for tx in txs:
        if filters.get("type") and tx["type"] != filters["type"]:
            continue
        if filters.get("start_date") and tx["date"] < filters["start_date"]:
            continue
        if filters.get("end_date") and tx["date"] > filters["end_date"]:
            continue
        filtered_txs.append(tx)

    # 统计分析
    buy_total = sum(tx["amount"] for tx in filtered_txs if "Buy" in tx["type"])
    sell_total = sum(tx["amount"] for tx in filtered_txs if "Sell" in tx["type"])
    fee_total = sum(tx["fee"] for tx in filtered_txs)
    net_profit = sell_total - buy_total - fee_total
    tx_count = len(filtered_txs)

    # 资产组合估值（示例固定值，实际需调用行情API）
    asset_value = 100  # TODO: 调用市场行情接口获取实时估值

    # 关联地址网络
    related_addresses = set(tx["counterparty"] for tx in filtered_txs if tx["counterparty"] != address)

    # 安全风险检测
    risky = any(addr in known_scam_addresses for addr in related_addresses)
    risk_message = "Warning: Wallet interacted with suspicious addresses!" if risky else "No known risks detected."

    return {
        "address": address,
        "tx_count": tx_count,
        "buy_total": buy_total,
        "sell_total": sell_total,
        "fee_total": fee_total,
        "net_profit": net_profit,
        "asset_value": asset_value,
        "related_addresses": list(related_addresses),
        "risk_message": risk_message,
        "transactions": filtered_txs,
    }
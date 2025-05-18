import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("QUICKNODE_RPC")

def get_today_unix_range():
    now = datetime.utcnow()
    start = datetime(now.year, now.month, now.day)
    end = start + timedelta(days=1)
    return int(start.timestamp()), int(end.timestamp())

def fetch_transactions(address):
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSignaturesForAddress",
        "params": [address, {"limit": 100}]
    }
    res = requests.post(RPC_URL, json=payload, headers=headers)
    res.raise_for_status()
    return res.json()["result"]

def analyze_wallet_today(address):
    start_ts, end_ts = get_today_unix_range()
    txs = fetch_transactions(address)

    total_in = 0
    total_out = 0
    fee_total = 0
    count = 0

    for tx in txs:
        block_time = tx.get("blockTime")
        if not block_time:
            continue
        if block_time < start_ts or block_time > end_ts:
            continue

        # 查询交易详情
        sig = tx["signature"]
        detail_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTransaction",
            "params": [sig, {"encoding": "jsonParsed"}]
        }
        res = requests.post(RPC_URL, json=detail_payload).json()
        result = res.get("result")
        if not result:
            continue

        meta = result.get("meta", {})
        fee = meta.get("fee", 0)
        fee_total += fee / 1e9  # lamports to SOL

        # 判断资金流向（简单判断：如果是接收者）
        transaction = result.get("transaction", {})
        message = transaction.get("message", {})
        account_keys = message.get("accountKeys", [])

        pre_balances = meta.get("preBalances", [])
        post_balances = meta.get("postBalances", [])

        for i, acct in enumerate(account_keys):
            pubkey = acct.get("pubkey")
            if pubkey == address and i < len(pre_balances):
                delta = (post_balances[i] - pre_balances[i]) / 1e9
                if delta > 0:
                    total_in += delta
                elif delta < 0:
                    total_out += -delta
                break
        count += 1

    net = total_in - total_out - fee_total
    return {
        "address": address,
        "tx_count": count,
        "buy_total": round(total_in, 6),
        "sell_total": round(total_out, 6),
        "fee_total": round(fee_total, 6),
        "net_profit": round(net, 6)
    }
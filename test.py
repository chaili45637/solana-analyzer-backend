from solana_utils import analyze_wallet_today

if __name__ == "__main__":
    address = "AGExAnYkhmxgDKVydxSh25qWzfkvoopZuuWvY5rZnoMB"
    try:
        result = analyze_wallet_today(address)
        print("分析结果:", result)
    except Exception as e:
        print("出错了:", e)
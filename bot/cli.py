import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Simple Trading Bot")

    parser.add_argument("--symbol", type=str, required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, help="BUY or SELL")
    parser.add_argument("--type", type=str, required=True, help="MARKET or LIMIT")
    parser.add_argument("--qty", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price for LIMIT order")

    return parser.parse_args()
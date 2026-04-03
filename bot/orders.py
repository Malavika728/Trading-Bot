import random
import time

def create_order(symbol, side, order_type, quantity, price=None):
    # simulate API delay
    time.sleep(1)

    # fake response like Binance
    mock_response = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "orderId": random.randint(100000, 999999),
        "status": "FILLED" if order_type == "MARKET" else "NEW",
        "executedQty": quantity if order_type == "MARKET" else 0,
        "avgPrice": price if price else round(random.uniform(50000, 70000), 2)
    }

    return mock_response
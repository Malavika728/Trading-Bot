from binance.client import Client

# NOTE: Replace with your own keys
API_KEY = "your_api_key_here"
API_SECRET = "your_secret_key_here"

BASE_URL = "https://testnet.binancefuture.com"

def get_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = BASE_URL
    return client
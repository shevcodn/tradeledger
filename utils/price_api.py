import os
import time
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_KEY")
CACHE_TTL = 3900
SHARED_CACHE_PATH = os.getenv("SHARED_CACHE_PATH", "../shared/price_cache.json")

def _load_cache():
    try:
        with open(SHARED_CACHE_PATH, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def _save_cache(cache):
    try:
        with open(SHARED_CACHE_PATH, 'w') as f:
            json.dump(cache, f, indent=2)
    except OSError:
        pass

def get_price(ticker):
    cache = _load_cache()
    now = time.time()
    if ticker in cache and now - cache[ticker]["time"] < CACHE_TTL:
        return cache[ticker]["price"]
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        price = float(data["Global Quote"]["05. price"])
        cache[ticker] = {"price": price, "time": now}
        _save_cache(cache)
        return price
    except (requests.RequestException, KeyError, ValueError):
        if ticker in cache:
            return cache[ticker]["price"]
        return None

def get_prices(tickers):
    return {ticker: get_price(ticker) for ticker in tickers}
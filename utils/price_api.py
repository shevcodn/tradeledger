import os
import time
import json
from dotenv import load_dotenv

load_dotenv()

CACHE_TTL = 3900
SHARED_CACHE_PATH = os.getenv("SHARED_CACHE_PATH", "../shared/price_cache.json")

_redis = None

def _get_redis():
    global _redis
    if _redis is None:
        url = os.getenv("UPSTASH_REDIS_URL")
        token = os.getenv("UPSTASH_REDIS_TOKEN")
        if url and token:
            from upstash_redis import Redis
            _redis = Redis(url=f"https://{url}", token=token)
    return _redis

def _load_cache():
    try:
        with open(SHARED_CACHE_PATH, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def get_price(ticker):
    r = _get_redis()
    if r:
        try:
            val = r.get(f"price:{ticker}")
            if val is not None:
                return float(val)
        except Exception:
            pass
        return None
    cache = _load_cache()
    now = time.time()
    if ticker in cache and now - cache[ticker]["time"] < CACHE_TTL:
        return cache[ticker]["price"]
    return None

def get_prices(tickers):
    return {ticker: get_price(ticker) for ticker in tickers}
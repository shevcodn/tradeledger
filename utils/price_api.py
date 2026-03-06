import os
import time
import json
from dotenv import load_dotenv

load_dotenv()

CACHE_TTL = 3900
SHARED_CACHE_PATH = os.getenv("SHARED_CACHE_PATH", "../shared/price_cache.json")
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

FALLBACK_PRICES = {
    "AAPL": 272.84, "NVDA": 185.09, "TSLA": 408.38, "MSFT": 401.86,
    "GOOGL": 308.06, "AMZN": 207.95, "NFLX": 985.33, "META": 657.01,
    "AMD": 203.68, "BTC": 86420.0, "ETH": 2190.0, "COIN": 198.45,
}

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

def _fetch_price_yfinance(ticker):
    try:
        import yfinance as yf
        t = yf.Ticker(ticker)
        price = t.fast_info.last_price
        if price and price > 0:
            return round(float(price), 2)
    except Exception:
        pass
    return None

def _fetch_price_alphavantage(ticker):
    if not ALPHA_VANTAGE_KEY:
        return None
    try:
        import requests
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}"
        data = requests.get(url, timeout=5).json()
        price = float(data["Global Quote"]["05. price"])
        return round(price, 2)
    except Exception:
        return None

def _fetch_live_price(ticker):
    price = _fetch_price_yfinance(ticker)
    if price:
        return price
    return _fetch_price_alphavantage(ticker)

def _load_cache():
    try:
        with open(SHARED_CACHE_PATH, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def _save_cache(cache):
    try:
        os.makedirs(os.path.dirname(SHARED_CACHE_PATH), exist_ok=True)
        with open(SHARED_CACHE_PATH, 'w') as f:
            json.dump(cache, f, indent=2)
    except OSError:
        pass

def get_price(ticker):
    r = _get_redis()
    now = time.time()

    if r:
        try:
            val = r.get(f"price:{ticker}")
            if val is not None:
                return float(val)
        except Exception:
            pass
        price = _fetch_live_price(ticker)
        if price:
            try:
                r.set(f"price:{ticker}", str(price), ex=CACHE_TTL)
            except Exception:
                pass
            return price
        return FALLBACK_PRICES.get(ticker)

    cache = _load_cache()
    if ticker in cache and now - cache[ticker]["time"] < CACHE_TTL:
        return cache[ticker]["price"]

    price = _fetch_live_price(ticker)
    if price:
        cache[ticker] = {"price": price, "time": now}
        _save_cache(cache)
        return price
    if ticker in cache:
        return cache[ticker]["price"]
    return FALLBACK_PRICES.get(ticker)

def get_prices(tickers):
    return {ticker: get_price(ticker) for ticker in tickers}

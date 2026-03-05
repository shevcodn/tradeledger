def check_alerts(prices_history, ticker, threshold=5.0):
    alerts = []
    for i in range(1, len(prices_history)):
        prev = prices_history[i - 1]
        curr = prices_history[i]
        change = ((curr - prev) / prev) * 100
        if change <= -threshold:
            alerts.append(f"Alert: {ticker} dropped {change:.2f}% from ${prev} to ${curr}")
    return alerts
def draw_chart(prices, ticker, height=10):
    if not prices:
        return
    min_p = min(prices)
    max_p = max(prices)
    print(f"\n{ticker} Price Chart (Min: {min_p:.2f}, Max: {max_p:.2f})")
    print("-" * (len(prices) * 2 + 5))
    for row in range(height, -1, -1):
        line = ""
        threshold = min_p + (max_p - min_p) * (row / height)
        for price in prices:
            if price >= threshold:
                line += "█ "
            else:
                line += "  "
        print(f"{threshold:6.0f} | {line}")
    print(" " * 9 + "-" * (len(prices) * 2))
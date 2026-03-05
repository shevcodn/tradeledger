def binary_search(transactions, ticker):
    sorted_t = sorted(transactions, key=lambda t: t.ticker)
    lo, hi = 0, len(sorted_t) - 1
    idx = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_t[mid].ticker == ticker:
            idx = mid
            break
        elif sorted_t[mid].ticker < ticker:
            lo = mid + 1
        else:
            hi = mid - 1
    if idx == -1:
        return []
    result = []
    i = idx
    while i >= 0 and sorted_t[i].ticker == ticker:
        result.append(sorted_t[i])
        i -= 1
    i = idx + 1
    while i < len(sorted_t) and sorted_t[i].ticker == ticker:
        result.append(sorted_t[i])
        i += 1
    return result

def search_by_date(transactions, date):
    return [t for t in transactions if t.date == date]
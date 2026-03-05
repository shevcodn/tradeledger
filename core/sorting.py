def sort_by_pnl(transactions, prices):
    def calculate_pnl(transaction):
        current_price = prices.get(transaction.ticker, transaction.price)
        return (current_price - transaction.price) * transaction.quantity
    
    buys = [t for t in transactions if t.type == "buy"]
    return sorted(buys, key=calculate_pnl, reverse=True)

def sort_by_date(transactions):
    return sorted(transactions, key=lambda t: t.date, reverse=True)

def sort_by_ticker(transactions):
    return sorted(transactions, key=lambda t: t.ticker)

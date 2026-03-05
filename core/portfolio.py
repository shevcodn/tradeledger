import heapq

class Portfolio:
    def __init__(self):
        self.holdings = {}
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        ticker = transaction.ticker
        if transaction.type == "buy":
            if ticker not in self.holdings:
                self.holdings[ticker] = {"qty": 0, "avg_price": 0.0}
            old_qty = self.holdings[ticker]["qty"]
            old_avg = self.holdings[ticker]["avg_price"]
            new_qty = old_qty + transaction.quantity
            new_avg = (old_avg * old_qty + transaction.price * transaction.quantity) / new_qty
            self.holdings[ticker] = {"qty": new_qty, "avg_price": new_avg}
        elif transaction.type == "sell":
            if ticker in self.holdings:
                self.holdings[ticker]["qty"] -= transaction.quantity
                if self.holdings[ticker]["qty"] <= 0:
                    del self.holdings[ticker]

    def get_pnl(self, ticker, current_price):
        if ticker in self.holdings:
            qty = self.holdings[ticker]["qty"]
            avg_price = self.holdings[ticker]["avg_price"]
            return (current_price - avg_price) * qty
        return 0.0
    
    def get_all_pnl(self, prices):
        pnl = {}
        for ticker, holding in self.holdings.items():
            current_price = prices.get(ticker, holding["avg_price"])
            pnl[ticker] = self.get_pnl(ticker, current_price)
        return pnl
    
    def get_best_trade(self, prices):
        best_trade = None
        best_pnl = float('-inf')
        for transaction in self.transactions:
            if transaction.type == "buy":
                current_price = prices.get(transaction.ticker, transaction.price)
                pnl = (current_price - transaction.price) * transaction.quantity
                if pnl > best_pnl:
                    best_pnl = pnl
                    best_trade = transaction
        return best_trade, best_pnl
    
    def get_worst_trade(self, prices):
        worst_trade = None
        worst_pnl = float('inf')
        for transaction in self.transactions:
            if transaction.type == "buy":
                current_price = prices.get(transaction.ticker, transaction.price)
                pnl = (current_price - transaction.price) * transaction.quantity
                if pnl < worst_pnl:
                    worst_pnl = pnl
                    worst_trade = transaction
        return worst_trade, worst_pnl
    
    def get_top5(self, prices):
        top5 = []
        for transaction in self.transactions:
            if transaction.type == "buy":
                current_price = prices.get(transaction.ticker, transaction.price)
                pnl = (current_price - transaction.price) * transaction.quantity
                heapq.heappush(top5, (-pnl, transaction))
        return [(t, -pnl) for pnl, t in heapq.nlargest(5, top5)]
    
    def get_summary(self, prices):
        summary = {}
        for ticker, holding in self.holdings.items():
            current_price = prices.get(ticker, holding["avg_price"])
            pnl = self.get_pnl(ticker, current_price)
            summary[ticker] = {
                "quantity": holding["qty"],
                "avg_price": holding["avg_price"],
                "current_price": current_price,
                "pnl": pnl
            }
        return summary
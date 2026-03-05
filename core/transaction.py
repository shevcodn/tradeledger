from datetime import datetime
import json

class Transaction:
    def __init__(self, ticker, type, price, quantity, date=None):
        self.ticker = ticker.upper()
        self.type = type
        self.price = price
        self.quantity = quantity
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "ticker": self.ticker,
            "type": self.type,
            "price": self.price,
            "quantity": self.quantity,
            "date": self.date
        }

    def __repr__(self):
        return f"{self.type.upper()} {self.quantity} {self.ticker} @ ${self.price:.2f} on {self.date}"

class TransactionNode:
    def __init__(self, transaction):
        self.transaction = transaction
        self.next = None

class TransactionHistory:
    def __init__(self):
        self.head = None

    def add(self, transaction):
        new_node = TransactionNode(transaction)
        new_node.next = self.head
        self.head = new_node

    def get_all(self):
        transaction = []
        current = self.head
        while current:
            transaction.append(current.transaction)
            current = current.next
        return transaction
    
    def save_to_json(self, filepath):
        transactions = self.get_all()
        with open(filepath, 'w') as f:
            json.dump([t.to_dict() for t in transactions], f, indent=4)
        
    def load_from_json(self, filepath):
        try:
            with open(filepath, 'r') as f:
                content = f.read().strip()
                if not content:
                    return
                data = json.loads(content)
                for item in reversed(data):
                    transaction = Transaction(**item)
                    self.add(transaction)
        except (FileNotFoundError, json.JSONDecodeError):
            pass


            

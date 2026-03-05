import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

from core.transaction import Transaction, TransactionHistory
from core.portfolio import Portfolio
from core.search import binary_search, search_by_date
from core.sorting import sort_by_date
from utils.display import show_transactions, show_pnl, show_summary
from utils.alerts import check_alerts
from utils.chart import draw_chart
from utils.price_api import get_prices

load_dotenv()

console = Console()
DATA_FILE = os.getenv("DATA_FILE", "data/transactions.json")
ALERT_THRESHOLD = float(os.getenv("ALERT_THRESHOLD", 5.0))

history = TransactionHistory()
portfolio = Portfolio()

def load_data():
    history.load_from_json(DATA_FILE)
    for t in history.get_all():
        portfolio.add_transaction(t)

def save_data():
    history.save_to_json(DATA_FILE)

def add_transaction():
    console.print("\n[bold green]Add Transaction[/bold green]")
    ticker = input("Ticker (e.g. AAPL): ").strip().upper()
    type_ = input("Type (buy/sell): ").strip().lower()
    price = float(input("Price: $"))
    quantity = int(input("Quantity: "))
    date = input("Date (YYYY-MM-DD) or Enter for today: ").strip() or None
    t = Transaction(ticker, type_, price, quantity, date)
    history.add(t)
    portfolio.add_transaction(t)
    save_data()
    console.print(f"[green]Added: {t}[/green]")

def view_portfolio():
    transactions = history.get_all()
    if not transactions:
        console.print("[red]No transactions yet![/red]")
        return
    tickers = list(portfolio.holdings.keys())
    prices = get_prices(tickers)
    prices = {k: v for k, v in prices.items() if v is not None}
    summary = portfolio.get_summary(prices)
    total_invested = sum(h["avg_price"] * h["qty"] for h in portfolio.holdings.values())
    total_value = sum(prices.get(t, portfolio.holdings[t]["avg_price"]) * portfolio.holdings[t]["qty"] for t in portfolio.holdings)
    total_pnl = total_value - total_invested
    show_transactions(transactions)
    show_pnl(summary)
    show_summary(total_invested, total_value, total_pnl, len(transactions))

def search_menu():
    console.print("\n[bold green]Search[/bold green]")
    choice = input("Search by (ticker/date): ").strip().lower()
    if choice == "ticker":
        ticker = input("Ticker: ").strip().upper()
        results = binary_search(history.get_all(), ticker)
    else:
        date = input("Date (YYYY-MM-DD): ").strip()
        results = search_by_date(history.get_all(), date)
    if results:
        show_transactions(results)
    else:
        console.print("[red]No results found![/red]")

def chart_menu():
    ticker = input("Ticker for chart: ").strip().upper()
    transactions = binary_search(history.get_all(), ticker)
    if not transactions:
        console.print("[red]No transactions for this ticker![/red]")
        return
    prices = [t.price for t in sort_by_date(transactions)]
    draw_chart(prices, ticker)

def alerts_menu():
    ticker = input("Ticker for alerts: ").strip().upper()
    transactions = binary_search(history.get_all(), ticker)
    if not transactions:
        console.print("[red]No transactions for this ticker![/red]")
        return
    prices = [t.price for t in sort_by_date(transactions)]
    alerts = check_alerts(prices, ticker, ALERT_THRESHOLD)
    if alerts:
        for alert in alerts:
            console.print(f"[red]{alert}[/red]")
    else:
        console.print("[green]No alerts![/green]")

def top5_menu():
    tickers = list(portfolio.holdings.keys())
    prices = get_prices(tickers)
    prices = {k: v for k, v in prices.items() if v is not None}
    top5 = portfolio.get_top5(prices)
    if not top5:
        console.print("[red]No trades yet![/red]")
        return
    console.print("\n[bold green]Top 5 Trades by P&L[/bold green]")
    for t, pnl in top5:
        color = "green" if pnl >= 0 else "red"
        console.print(f"  {t.ticker} | {t.quantity} shares | [{color}]${pnl:.2f}[/{color}]")

def menu():
    load_data()
    while True:
        console.print(Panel(
            "[1] Add Transaction\n"
            "[2] View Portfolio\n"
            "[3] Search\n"
            "[4] Price Chart\n"
            "[5] Check Alerts\n"
            "[6] Top 5 Trades\n"
            "[0] Exit",
            title="[bold green]TradeLedger[/bold green]",
            border_style="green"
        ))
        choice = input("Choice: ").strip()
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            search_menu()
        elif choice == "4":
            chart_menu()
        elif choice == "5":
            alerts_menu()
        elif choice == "6":
            top5_menu()
        elif choice == "0":
            console.print("[green]Bye![/green]")
            break
        else:
            console.print("[red]Invalid choice![/red]")

if __name__ == "__main__":
    menu()
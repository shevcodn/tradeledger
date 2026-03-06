from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

def show_transactions(transactions):
    table = Table(title="Transaction History", box=box.MINIMAL)
    table.add_column("Date", style="green")
    table.add_column("Ticker", style="bold")
    table.add_column("Type", style="green")
    table.add_column("Qty")
    table.add_column("Price", justify="right")
    for t in transactions:
        color = "green" if t.type == "buy" else "red"
        table.add_row(
            t.date,
            t.ticker,
            f"[{color}]{t.type.upper()}[/{color}]",
            str(t.quantity),
            f"${t.price:.2f}"
        )
    console.print(table)

def show_pnl(summary):
    table = Table(title="Portfolio P&L", box=box.MINIMAL)
    table.add_column("Ticker", style="bold")
    table.add_column("Qty")
    table.add_column("Avg Buy")
    table.add_column("Current")
    table.add_column("P&L", justify="right")
    for ticker, data in summary.items():
        pnl = data["pnl"]
        color = "green" if pnl >= 0 else "red"
        table.add_row(
            ticker,
            str(data["quantity"]),
            f"${data['avg_price']:.2f}",
            f"${data['current_price']:.2f}",
            f"[{color}]${pnl:.2f}[/{color}]"
        )
    console.print(table)

def show_summary(total_invested, total_value, total_pnl, num_trades):
    color = "green" if total_pnl >= 0 else "red"
    panel = Panel(
        f"Invested: ${total_invested:.2f}\n"
        f"Value:    ${total_value:.2f}\n"
        f"[{color}]P&L:      ${total_pnl:.2f}[/{color}]\n"
        f"Trades:   {num_trades}",
        title="Portfolio Summary",
        border_style=color
    )
    console.print(panel)
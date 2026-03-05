<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&duration=3000&pause=1000&color=00FF88&center=true&vCenter=true&width=600&lines=Portfolio+Projects;Python+%C2%B7+Rich+%C2%B7+Alpha+Vantage+%C2%B7+LinkedList;Built+during+1000-task+curriculum" alt="Typing SVG" />

### Denis Shevchenko · [shevcodn.dev](https://shevcodn.dev)

[![Python](https://img.shields.io/badge/Python-3.12-00ff88?style=flat-square&logo=python&logoColor=black)](https://python.org)
[![Status](https://img.shields.io/badge/Status-Active_Development-00ff88?style=flat-square)](https://github.com/shevcodn/projects)
[![Projects](https://img.shields.io/badge/Projects-2_of_7-00ff88?style=flat-square)](https://github.com/shevcodn/projects)

</div>

---

## Projects

| # | Project | Stack | Try it | Status |
|---|---------|-------|--------|--------|
| 01 | [Stock Portfolio Tracker](https://github.com/shevcodn/stock-portfolio-tracker) | Python · Alpha Vantage · LinkedList · HashMap | [▶ Live](https://shevcodn.dev/#project-01) | ✅ Done |
| 02 | [TradeLedger](https://github.com/shevcodn/tradeledger) | Python · Rich · Alpha Vantage · LinkedList · Heap | [▶ Live](https://shevcodn.dev/#project-02) | ✅ Done |
| 03 | MarketPulse | WebSockets · Redis · React | — | 🔜 p800 |
| 04 | DeployKit | Docker · GitHub Actions · Railway | — | 🔜 p900 |
| 05 | AuthVault | JWT · OAuth · Railway deploy | — | 🔜 p960 |
| 06 | WealthTrack | FastAPI · PostgreSQL · Docker | — | 🔜 p980 |
| 07 | PortfolioOS | TBD | — | 🔜 p1000 |

---

## Project-02: TradeLedger

> **Python CLI app** — advanced trade ledger with Rich UI, P&L tracking, price alerts and ASCII charts.

```
Stack:   Python · Rich · Alpha Vantage API · LinkedList · Heap · Binary Search
Storage: JSON persistence between sessions
Alerts:  Sliding window price drop detection
```

### Features

| Option | Description |
|--------|-------------|
| `1` Add Transaction | Log buy/sell with date, price, quantity |
| `2` View Portfolio | Rich table: avg price · current price · P&L |
| `3` Search | Binary search by ticker or date |
| `4` Price Chart | ASCII chart of transaction prices |
| `5` Check Alerts | Sliding window price drop alerts |
| `6` Top 5 Trades | Best trades ranked by P&L via Heap |

### Data Structures

- **LinkedList** — transaction history, newest → oldest
- **HashMap** — `O(1)` holdings lookup by ticker
- **Heap** — `O(n log k)` top-5 trades by P&L
- **Binary Search** — `O(log n)` search by ticker

### Quick Start (local)

```bash
git clone https://github.com/shevcodn/tradeledger
cd tradeledger
cp .env.example .env        # add your Alpha Vantage key
pip install -r requirements.txt
python main.py
```

> **Free API key:** [alphavantage.co](https://www.alphavantage.co/support/#api-key) — 30 seconds to get

### Try it live

**[▶ shevcodn.dev/#project-02](https://shevcodn.dev/#project-02)** — interactive terminal, no install needed

---

<div align="center">

*Built during p1→p1000 Python engineering curriculum · Toronto 2026*

[![Website](https://img.shields.io/badge/shevcodn.dev-00ff88?style=flat-square&logo=vercel&logoColor=black)](https://shevcodn.dev)

</div>
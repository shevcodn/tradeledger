<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&duration=3000&pause=1000&color=00FF88&center=true&vCenter=true&width=600&lines=TradeLedger+v2.0;Python+%C2%B7+Rich+%C2%B7+Alpha+Vantage;LinkedList+%C2%B7+Heap+%C2%B7+Binary+Search" alt="Typing SVG" />

### Denis Shevchenko · [shevcodn.dev](https://shevcodn.dev)

[![Python](https://img.shields.io/badge/Python-3.12-00ff88?style=flat-square&logo=python&logoColor=black)](https://python.org)
[![Rich](https://img.shields.io/badge/Rich-UI-00ff88?style=flat-square)](https://github.com/Textualize/rich)
[![Try Live](https://img.shields.io/badge/▶_Try_Live-shevcodn.dev-00ff88?style=flat-square&logo=vercel&logoColor=black)](https://shevcodn.dev/#project-02)

</div>

---

## Projects

| # | Project | Stack | Try it | Status |
|---|---------|-------|--------|--------|
| 01 | [Stock Portfolio Tracker](https://github.com/shevcodn/projects) | Python · Alpha Vantage API · LinkedList · HashMap | [▶ Live](https://shevcodn.dev/#project-01) | ✅ Done |
| 02 | [TradeLedger](https://github.com/shevcodn/tradeledger) | Python · Rich · yfinance · Alpha Vantage · LinkedList · Heap | [▶ Live](https://shevcodn.dev/#project-02) | ✅ Done |
| 03 | MarketPulse | WebSockets · Redis · React | — | 🔜 p800 |
| 04 | DeployKit | Docker · GitHub Actions · Railway | — | 🔜 p900 |
| 05 | AuthVault | JWT · OAuth · Railway deploy | — | 🔜 p960 |
| 06 | WealthTrack | FastAPI · PostgreSQL · Docker | — | 🔜 p980 |
| 07 | PortfolioOS | TBD | — | 🔜 p1000 |

---

## Project-02: TradeLedger

> **Python CLI app** — advanced trade journal with Rich UI. Track any ticker, log buy/sell, monitor P&L, set price alerts, rank top trades by profit.

```
Stack:   Python · Rich · yfinance · Alpha Vantage fallback · LinkedList · Heap · Binary Search
Balance: $25,000 virtual
Tickers: Any ticker (user inputs)
Cache:   Shared with Project-01 (TTL 65 min, one API key)
```

### Features

| Command | Description |
|---------|-------------|
| `buy TICKER QTY` | Buy at real-time price |
| `sell TICKER QTY` | Sell with P&L calculation |
| `portfolio` | Rich table: avg price · current price · P&L % |
| `search TICKER` | Binary search in transaction history |
| `top N` | Top N trades by profit via Heap |
| `alert TICKER PRICE` | Set price drop alert |
| `history` | Full transaction log via LinkedList |

### Data Structures

- **LinkedList** — transaction history, newest → oldest
- **HashMap** — `O(1)` holdings lookup by ticker
- **Heap** — `O(n log k)` top-N trades by P&L
- **Binary Search** — `O(log n)` search by ticker or date

### Quick Start

```bash
git clone https://github.com/shevcodn/tradeledger
cd tradeledger
cp .env.example .env
pip install -r requirements.txt
python main.py
```

> **Prices:** yfinance (Yahoo Finance) — primary. Alpha Vantage — fallback (optional API key).

### Try it live

**[▶ shevcodn.dev/#project-02](https://shevcodn.dev/#project-02)** — interactive terminal, no install needed

---

<div align="center">

*Project 02 of 7 · Built during p1→p1000 Python curriculum · Toronto 2026*

[![Website](https://img.shields.io/badge/Website-shevcodn.dev-00ff88?style=flat-square&logo=vercel&logoColor=black)](https://shevcodn.dev)
[![GitLab](https://img.shields.io/badge/GitLab-shevcodn-00ff88?style=flat-square&logo=gitlab&logoColor=black)](https://gitlab.com/shevcodn)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-shevcodn-00ff88?style=flat-square&logo=linkedin&logoColor=black)](https://linkedin.com/in/shevcodn)
[![LeetCode](https://img.shields.io/badge/LeetCode-shevcodn-00ff88?style=flat-square&logo=leetcode&logoColor=black)](https://leetcode.com/shevcodn)

</div>


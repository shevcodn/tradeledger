<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&duration=3000&pause=1000&color=00FF88&center=true&vCenter=true&width=600&lines=TradeLedger+v2.0;Python+%C2%B7+Rich+%C2%B7+Alpha+Vantage;LinkedList+%C2%B7+Heap+%C2%B7+Binary+Search" alt="Typing SVG" />

### Denis Shevchenko · [shevcodn.dev](https://shevcodn.dev)

[![Python](https://img.shields.io/badge/Python-3.12-00ff88?style=flat-square&logo=python&logoColor=black)](https://python.org)
[![Rich](https://img.shields.io/badge/Rich-UI-00ff88?style=flat-square)](https://github.com/Textualize/rich)
[![Try Live](https://img.shields.io/badge/▶_Try_Live-shevcodn.dev-00ff88?style=flat-square&logo=vercel&logoColor=black)](https://shevcodn.dev/#project-02)

</div>

---

# TradeLedger

> Advanced CLI trade journal built with **Rich UI**. Track any ticker, log buy/sell trades, monitor P&L, set price alerts, and rank top trades — all from the terminal.

**[▶ Try it live → shevcodn.dev/#project-02](https://shevcodn.dev/#project-02)**

---

## Projects

| # | Project | Stack | Try it | Status |
|---|---------|-------|--------|--------|
| 01 | [Stock Portfolio Tracker](https://github.com/shevcodn/projects) | Python · Alpha Vantage API · LinkedList · HashMap | [▶ Live demo](https://shevcodn.dev/#project-01) | ✅ Done |
| 02 | [TradeLedger](https://github.com/shevcodn/tradeledger) | Python · Rich · Alpha Vantage · LinkedList · Heap | [▶ Live demo](https://shevcodn.dev/#project-02) | ✅ Done |
| 03 | MarketPulse | WebSockets · Redis · React | — | 🔜 p800 |
| 04 | DeployKit | Docker · GitHub Actions · Railway | — | 🔜 p900 |
| 05 | AuthVault | JWT · OAuth · Railway deploy | — | 🔜 p960 |
| 06 | WealthTrack | FastAPI · PostgreSQL · Docker | — | 🔜 p980 |
| 07 | PortfolioOS | TBD | — | 🔜 p1000 |

---

## Features

| Option | Description |
|--------|-------------|
| `1` Add Transaction | Log buy/sell with date, price, quantity |
| `2` View Portfolio | Rich table: avg price · current price · P&L % |
| `3` Search | Binary search by ticker or date |
| `4` ASCII Chart | Price chart of transaction history |
| `5` Check Alerts | Sliding window price drop detection |
| `6` Top 5 Trades | Best trades ranked by P&L via Heap |

---

## Data Structures Used

| Structure | Usage | Complexity |
|-----------|-------|------------|
| **LinkedList** | Transaction history (newest → oldest) | O(1) insert |
| **HashMap** | Holdings lookup by ticker | O(1) lookup |
| **Heap** | Top-5 trades by P&L | O(n log k) |
| **Binary Search** | Search by ticker / date | O(log n) |

---

## Stack

```
Python 3.12
Rich          — tables, colors, panels, progress bars
Alpha Vantage — real-time stock prices (shared cache)
JSON          — persistence between sessions
```

---

## Quick Start

```bash
git clone https://github.com/shevcodn/tradeledger
cd tradeledger
cp .env.example .env        # add your Alpha Vantage key
pip install -r requirements.txt
python main.py
```

> Free API key: [alphavantage.co](https://www.alphavantage.co/support/#api-key)

### Shared Price Cache

This project shares a price cache with [Stock Portfolio Tracker](https://github.com/shevcodn/projects):

```
projects/
├── stock-tracker/
├── tradeledger/
└── shared/
    └── price_cache.json    ← TTL 65 min, one API key
```

---

## Project Structure

```
tradeledger/
├── main.py
├── core/
│   ├── transaction.py      # LinkedList
│   ├── portfolio.py        # HashMap
│   ├── sorting.py          # Heap (top trades)
│   └── search.py           # Binary Search
├── utils/
│   ├── display.py          # Rich tables
│   ├── chart.py            # ASCII chart
│   ├── alerts.py           # Sliding window alerts
│   └── price_api.py        # Alpha Vantage + shared cache
└── data/
    └── transactions.json
```

---

<div align="center">

*Project 02 of 7 · Built during p1→p1000 Python curriculum · Toronto 2026*

[![Website](https://img.shields.io/badge/shevcodn.dev-00ff88?style=flat-square&logo=vercel&logoColor=black)](https://shevcodn.dev)
[![All Projects](https://img.shields.io/badge/All_Projects-00ff88?style=flat-square&logo=github&logoColor=black)](https://github.com/shevcodn/projects)

</div>

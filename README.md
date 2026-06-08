# Binance Futures Trading Bot

A Python-based CLI tool for placing Market and Limit orders on the Binance Futures Testnet.

## Project Status
- **Core Logic:** Complete (Client wrapper, order preparation, validation, and logging).
- **Environment:** Setup documentation prepared.
- **API Connectivity:** Code is ready for deployment.
    * *Note: As of Monday, june 8, 2026, the Binance Futures Testnet portal (testnet.binancefuture.com) is returning a "Server Not Found" error. The application is fully structured and prepared to execute trades as soon as the testnet service is restored.*

## Setup & Execution
1. Install dependencies: `pip install -r requirements.txt`
2. Update `cli.py` with valid API Key/Secret Key in the `BinanceClient` initialization.
3. Usage: `python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001`
# Binance Futures Testnet Trading Bot

Simple CLI Python trading bot for Binance Futures Testnet.

## Features

Market Orders
Limit Orders
BUY/SELL support
CLI validation
Logging
Error handling

## Setup

Install Python 3

Install dependencies:

pip install -r requirements.txt

Add API keys inside cli.py

## Run examples

MARKET ORDER:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

LIMIT ORDER:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

## Assumptions

User has Binance Futures Testnet account
Valid API keys required
Internet connection required

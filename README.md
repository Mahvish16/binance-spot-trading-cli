## Binance Spot Testnet Order Placer (Python CLI)

A simple command-line tool built with Python to place **Spot testnet orders** (LIMIT / MARKET, BUY / SELL) using the Binance API.

This tool uses the **[Binance Spot Testnet](https://testnet.binance.vision/)** and is safe for experimentation — no real money involved.

### Features

* Place `MARKET` and `LIMIT` orders
* Supports `BUY` and `SELL`
* Uses environment variables for API key/secret
* Built using class-based design for modularity
* CLI interface with `argparse`

### Requirements

* Python 3.7+
* Binance Python SDK: `python-binance`
* `.env` file with your testnet API keys

### Setup Instructions

1. **Clone the repository (or copy the script)**

2. **Install dependencies**

```bash
pip install python-binance python-dotenv
```

3. **Create `.env` file** in the same directory:

```
API_KEY=your_testnet_api_key_here
API_SECRET=your_testnet_api_secret_here
```

> Get your testnet keys from: [https://testnet.binance.vision/](https://testnet.binance.vision)

### Usage

#### Basic Syntax

```bash
python order_placer.py --symbol SYMBOL --side SIDE --type TYPE --quantity QUANTITY [--price PRICE]
```

#### Examples

**Place a Market Buy Order:**

```bash
python order_placer.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

**Place a Limit Sell Order:**

```bash
python order_placer.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

###  CLI Argument Help

| Argument     | Required | Description                      |
| ------------ | -------- | -------------------------------- |
| `--symbol`   |  Yes    | Trading pair, e.g. `BTCUSDT`     |
| `--side`     |  Yes    | `BUY` or `SELL`                  |
| `--type`     |  Yes    | `MARKET` or `LIMIT`              |
| `--quantity` |  Yes    | Amount of asset to trade         |
| `--price`    |  No     | Required for `LIMIT` orders only |



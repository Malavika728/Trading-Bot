# Trading Bot (Binance Futures Testnet)

## Overview

This project is a simple Python-based trading bot developed as part of an assignment.
It provides a command-line interface (CLI) to place MARKET and LIMIT orders for Binance Futures (USDT-M).

The application is designed with a modular structure, input validation, logging, and error handling to reflect real-world development practices.

---

## Features

* Place MARKET and LIMIT orders
* Supports both BUY and SELL sides
* CLI-based input using argparse
* Input validation with clear error messages
* Logging of requests, responses, and errors
* Modular and readable code structure

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py        # Binance client setup (placeholder for real API)
│   ├── orders.py        # Order placement logic
│   ├── validators.py    # Input validation
│   ├── logger.py        # Logging configuration
│   └── cli.py           # CLI argument parsing
│
├── logs/
│   └── app.log          # Log file
│
├── main.py              # Entry point
├── requirements.txt
└── README.md
```

---

## Setup Instructions

1. Clone or download the project

2. Create a virtual environment:

```
python -m venv venv
```

3. Activate the virtual environment:

**Windows:**

```
venv\Scripts\activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

### ▶️ MARKET Order

```
python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

### ▶️ LIMIT Order

```
python main.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.001 --price 30000
```

---

## Sample Output

```
--- Order Details ---
Symbol     : BTCUSDT
Side       : BUY
Type       : MARKET
Quantity   : 0.001

--- Response ---
Order ID      : 123456
Status        : FILLED
Executed Qty  : 0.001
Avg Price     : 64000

✔ Order placed successfully
```

---

## Logging

Logs are stored in:

```
logs/app.log
```

The log file contains:

* Order requests
* API responses (or simulated responses)
* Error messages

---

## Note on API Integration

Due to network restrictions, Binance Futures Testnet was not accessible during development.

To ensure the application remains functional and demonstrates the required architecture, a simulated order execution layer has been implemented. This layer mimics real Binance API responses.

The code is structured in a way that allows easy replacement of the mock logic with actual Binance API calls.

---

## Future Improvements

* Integration with live Binance Testnet API
* Additional order types (Stop-Limit, OCO, etc.)
* Enhanced CLI experience with prompts
* Basic UI for interaction

---

## Conclusion

This project demonstrates the implementation of a structured Python application with CLI interaction, validation, logging, and modular design, suitable for extension into a real trading system.

import os
from dotenv import load_dotenv
import argparse
from binance import Client
import logging

logging.basicConfig(
    filename='binance_order.log',
    level=logging.INFO,  # Use DEBUG for more detail
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class BinanceOrderPlacer:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")
        self.client = Client(api_key, api_secret)
        self.client.API_URL = 'https://testnet.binance.vision/api'

    def is_valid_symbol(self, symbol):
        logging.info("Fetching all symbols for validation")
        try:
            tickers = self.client.get_all_tickers()
            valid_symbols = [ticker['symbol'] for ticker in tickers]
            return symbol.upper() in valid_symbols
        except Exception as e:
            print("Error fetching symbols:", e)
            return False


    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            side = side.upper()
            order_type = order_type.upper()
            logging.info(f"Placing {order_type} {side} order: Symbol={symbol}, Quantity={quantity}, Price={price}")

            if order_type == "LIMIT" and side == "BUY":
                order = self.client.order_limit_buy(
                    symbol=symbol,
                    quantity=quantity,
                    price=price
                )
            elif order_type == "LIMIT" and side == "SELL":
                order = self.client.order_limit_sell(
                    symbol=symbol,
                    quantity=quantity,
                    price=price
                )
            elif order_type == "MARKET" and side == "BUY":
                order = self.client.order_market_buy(
                    symbol=symbol,
                    quantity=quantity
                )
            elif order_type == "MARKET" and side == "SELL":
                order = self.client.order_market_sell(
                    symbol=symbol,
                    quantity=quantity
                )
            else:
                raise ValueError("Invalid side or order type provided.")
            logging.info(f"Order response: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing order: {e}")
            return f"Error: {e}"


def parse_arguments():
    parser = argparse.ArgumentParser(description='Place a Binance Test order')
    parser.add_argument('--symbol', required=True, help='Trading pair symbol, e.g., BTCUSDT')
    parser.add_argument('--side', required=True, help='Order direction: BUY or SELL')
    parser.add_argument('--type', required=True, help='Order type: MARKET or LIMIT')
    parser.add_argument('--quantity', required=True, help='Amount of asset to trade')
    parser.add_argument('--price', required=False, help='Set a price for LIMIT orders (optional for MARKET orders)')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    print(f"Placing order: symbol={args.symbol}, side={args.side}, type={args.type}, quantity={args.quantity}")

    placer = BinanceOrderPlacer()

    if not placer.is_valid_symbol(args.symbol):
        print(f"Invalid symbol: {args.symbol}. Please check the trading pair (e.g., BTCUSDT).")
        exit()
    
    result = placer.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )
    print("Order result:", result)

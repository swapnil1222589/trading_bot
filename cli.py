import argparse
from bot.client import BinanceClient
from bot.orders import execute_order
from bot.validators import validate_side, validate_order_type, validate_quantity

API_KEY="ADD_YOUR_API_KEY"
API_SECRET="ADD_YOUR_SECRET_KEY"

parser=argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

parser.add_argument("--symbol",required=True)
parser.add_argument("--side",required=True)
parser.add_argument("--type",required=True)
parser.add_argument("--quantity",required=True)
parser.add_argument("--price")

args=parser.parse_args()

try:
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    client=BinanceClient(API_KEY, API_SECRET)

    print("\nORDER SUMMARY")
    print("Symbol:",args.symbol)
    print("Side:",args.side)
    print("Type:",args.type)
    print("Qty:",args.quantity)

    if args.type=="LIMIT":
        if not args.price:
            raise ValueError("LIMIT order needs price")
        print("Price:",args.price)

    execute_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

except Exception as e:
    print("Error:",str(e))

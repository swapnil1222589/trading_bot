from binance.client import Client

class BinanceClient:

    def __init__(self, api_key, api_secret):

        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )

    def place_market_order(self,symbol,side,quantity):

        return self.client.futures_create_order(

            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    def place_limit_order(self,symbol,side,quantity,price):

        return self.client.futures_create_order(

            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

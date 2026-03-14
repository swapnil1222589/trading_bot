from bot.logging_config import setup_logger

logger = setup_logger()

def execute_order(client,symbol,side,order_type,qty,price=None):

    try:

        logger.info("Order Request")

        if order_type=="MARKET":

            order=client.place_market_order(
                symbol,
                side,
                qty
            )

        else:

            order=client.place_limit_order(
                symbol,
                side,
                qty,
                price
            )

        logger.info(order)

        print("\nORDER SUCCESS")

        print("Order ID:",order.get('orderId'))

        print("Status:",order.get('status'))

        print("Executed Qty:",order.get('executedQty'))

        print("Avg Price:",order.get('avgPrice','N/A'))

        return order

    except Exception as e:

        logger.error(str(e))

        print("\nORDER FAILED")

        print(str(e))

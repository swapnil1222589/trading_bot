def validate_side(side):

    if side not in ["BUY","SELL"]:

        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type):

    if order_type not in ["MARKET","LIMIT"]:

        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(qty):

    if float(qty) <= 0:

        raise ValueError("Quantity must be positive")

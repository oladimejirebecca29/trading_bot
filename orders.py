def prepare_order(symbol, side, order_type, qty, price=None):
    params = {"symbol": symbol, "side": side, "type": order_type, "quantity": qty}
    if order_type == 'LIMIT':
        params.update({"price": price, "timeInForce": "GTC"})
    return params
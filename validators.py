def validate_order(args):
    if args.type == 'LIMIT' and not args.price:
        raise ValueError("Price is required for LIMIT orders.")
    if args.qty <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return True
import argparse
from bot.client import BinanceClient
from bot.orders import prepare_order
from bot.validators import validate_order
from bot.logging_config import logger

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", choices=['BUY', 'SELL'], required=True)
    parser.add_argument("--type", choices=['MARKET', 'LIMIT'], required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)
    args = parser.parse_args()

    try:
        validate_order(args)
        # UPDATED: No need to pass keys here anymore!
        client = BinanceClient() 
        params = prepare_order(args.symbol, args.side, args.type, args.qty, args.price)
        
        logger.info(f"Request: {params}")
        response = client.send_request(params)
        logger.info(f"Response: {response}")
    except Exception as e:
        logger.error(f"Failed: {e}")

if __name__ == "__main__":
    main()
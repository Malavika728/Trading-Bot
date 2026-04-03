from bot.cli import get_args
from bot.validators import validate_inputs
from bot.orders import create_order
from bot.logger import setup_logger

import logging

def main():
    setup_logger()
    args = get_args()

    try:
        # Validate inputs
        validate_inputs(args.symbol, args.side, args.type, args.qty, args.price)

        print("\n--- Order Details ---")
        print(f"Symbol     : {args.symbol}")
        print(f"Side       : {args.side}")
        print(f"Type       : {args.type}")
        print(f"Quantity   : {args.qty}")
        if args.price:
            print(f"Price      : {args.price}")

        logging.info(f"Placing order: {vars(args)}")

        # Place order
        response = create_order(
            args.symbol,
            args.side.upper(),
            args.type.upper(),
            args.qty,
            args.price
        )

        print("\n--- Response ---")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Avg Price     : {response.get('avgPrice', 'N/A')}")

        print("\n✔ Order placed successfully")

        logging.info(f"Order success: {response}")

    except Exception as e:
        print("\n✖ Error:", str(e))
        logging.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
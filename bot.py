from alpaca.trading.client import TradingClient

import argparse


class AlpacaTradingBot:
    def __init__(self, api_key, api_secret, paper=True):
        # Initialize the new Alpaca TradingClient
        self.client = TradingClient(api_key, api_secret, paper=paper)

    def check_account(self):
        # Fetch account details using the new API
        account = self.client.get_account()
        print("Account status:", account.status)
        print("Equity:", account.equity)
        print("Buying Power:", account.buying_power)

    def place_order(self, symbol, qty, side, order_type, time_in_force):
        try:
            # Create an order request using the new API
            order_request = OrderRequest(
                symbol=symbol,
                qty=qty,
                side=side,
                type=order_type,
                time_in_force=time_in_force,
            )
            order = self.client.submit_order(order_request)
            print(f"Order placed: {order}")
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description="Alpaca Trading Bot")
    parser.add_argument(
        "--key", required=True, help="Path to the file containing your Alpaca API key"
    )
    parser.add_argument(
        "--secret",
        required=True,
        help="Path to the file containing your Alpaca API secret",
    )
    parser.add_argument(
        "--env",
        required=True,
        choices=["real", "paper"],
        help="Indicates whether we should use a real account or paper account",
    )

    args = parser.parse_args()

    # Read API key and secret from files
    try:
        with open(args.key, "r") as f:
            api_key = f.read().strip()
        with open(args.secret, "r") as f:
            api_secret = f.read().strip()
    except Exception as e:
        print(f"Error reading API credentials: {e}")
        exit(1)

    use_paper = args.env == "paper"
    bot = AlpacaTradingBot(api_key=api_key, api_secret=api_secret, paper=use_paper)

    print("Checking account status...")
    bot.check_account()


if __name__ == "__main__":
    main()

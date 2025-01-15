import alpaca_trade_api as tradeapi
import argparse

class AlpacaTradingBot:
    def __init__(self, api_key, api_secret, base_url):
        self.api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

    def check_account(self):
        account = self.api.get_account()
        print("Account status:", account.status)
        print("Equity:", account.equity)
        print("Buying Power:", account.buying_power)

    def place_order(self, symbol, qty, side, order_type, time_in_force):
        try:
            order = self.api.submit_order(
                symbol=symbol,
                qty=qty,
                side=side,
                type=order_type,
                time_in_force=time_in_force
            )
            print(f"Order placed: {order}")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Alpaca Trading Bot")
    parser.add_argument('--key', required=True, help="Path to the file containing your Alpaca API key")
    parser.add_argument('--secret', required=True, help="Path to the file containing your Alpaca API secret")
    parser.add_argument('--api_url', required=True, help="The URL to the Alpaca API to use (used to select live vs paper account)")

    args = parser.parse_args()

    # Read API key and secret from files
    try:
        with open(args.key, 'r') as f:
            api_key = f.read().strip()
        with open(args.secret, 'r') as f:
            api_secret = f.read().strip()
    except Exception as e:
        print(f"Error reading API credentials: {e}")
        exit(1)

    bot = AlpacaTradingBot(api_key=api_key, api_secret=api_secret, base_url=args.api_url)

    print("Checking account status...")
    bot.check_account()

if __name__ == "__main__":
    main()

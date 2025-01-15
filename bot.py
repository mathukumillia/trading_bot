from alpaca.trading.client import TradingClient


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

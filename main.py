import argparse
from bot import AlpacaTradingBot


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

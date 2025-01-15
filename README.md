# Trading Bot

Contains code for my first attempt at a trading bot.

# Usage

Run the bot using the run.sh script as follows:

```
./run.sh <keys_directory> <real|paper>
```

The `real|paper` argument determines whether the bot should run against the
real Alpaca API (with live funds) or the paper Alpaca API.

The `keys_directory` argument is the path to a directory that contains the
API keys necessary to authenticate with the Alpaca API. The script expects
the directory to look like this:

```
+ keys_directory
---+ paper
-----+ key
-----+ secret
---+ real
-----+ key
-----+ secret
```

The `key` and `secret` files in both the `real` and `paper` directories contain
the API key and API secret for the live and paper accounts respectively.

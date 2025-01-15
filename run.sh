#!/bin/bash

# Check if virtual environment exists, if not, create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt &> /dev/null
else
    echo "Error: requirements.txt not found!"
    deactivate
    exit 1
fi

# Check if correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <directory> <real|paper>"
  exit 1
fi

# Assign arguments to variables
dir="$1"
env="$2"
url="https://paper-api.alpaca.markets/v2"

# Validate the environment and use it to set the API url.
if [ "$env" == "real" ]; then
  echo "Using real account"
  url="https://api.alpaca.markets"
elif [ "$env" == "paper" ]; then
  echo "Using paper account"
  url="https://paper-api.alpaca.markets"
else
  echo "Invalid second argument. It must be 'real' or 'paper'."
  exit 1
fi

# Define the paths to the key and secret files
key_file="$dir/$env/key"
secret_file="$dir/$env/secret"

# Check if the key and secret files exist
if [ ! -f "$key_file" ]; then
  echo "Error: Key file not found at $key_file"
  exit 1
fi

if [ ! -f "$secret_file" ]; then
  echo "Error: Secret file not found at $secret_file"
  exit 1
fi

# Run the bot
if [ -f "bot.py" ]; then
    echo "Running trading bot..."
    python3 bot.py --key $key_file --secret $secret_file --api_url $url
else
    echo "Error: bot.py not found!"
    deactivate
    exit 1
fi

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

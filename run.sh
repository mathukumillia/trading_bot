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
    python3 main.py --key $key_file --secret $secret_file --env $env
else
    echo "Error: bot.py not found!"
    deactivate
    exit 1
fi

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

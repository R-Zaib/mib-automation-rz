# CoinGecko API Endpoint Status Checker

This script checks the HTTP status codes for specified endpoints in the CoinGecko API.

## Requirements

- Python
- requests library (`pip install requests`)

## Script Explanation

The script defines a function, `check_status_code`, to make a GET request to the CoinGecko API for a given endpoint and print the resulting HTTP status code. The list of endpoints is then iterated over, and the function is called for each endpoint to check and display the status codes.

## Usage

# To access endpoint
To access all the possible endpoints, please visit:
https://docs.coingecko.com/reference/endpoint-overview

    
# List of endpoints to check
endpoints = [
    "/ping",
    "/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=1&page=1",
    "/coins/nonexistentcoin",  # Intentionally non-existent coin
    "/coins/markets?vs_currency=invalidcurrency",
]

You can add the endpoint you want to check in endpoint.


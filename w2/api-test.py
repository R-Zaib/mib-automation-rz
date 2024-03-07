import requests

# Function to make a request and print the HTTP status code
def check_status_code(endpoint):
    try:
        response = requests.get(f"https://api.coingecko.com/api/v3/{endpoint}")
        status_code = response.status_code
    except requests.RequestException as e:
        status_code = "Error"

    print(f"| `/{endpoint}` | {status_code} |")
    
# List of endpoints to check
endpoints = [
    "/ping",
    "/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=1&page=1",
    "/coins/nonexistentcoin",  # Intentionally non-existent coin
    "/coins/markets?vs_currency=invalidcurrency",
    
]

# Check status codes for each endpoint
for endpoint in endpoints:
    check_status_code(endpoint)



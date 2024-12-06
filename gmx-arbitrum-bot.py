import requests
import time

# API Endpoint for GMX on Arbitrum
BUY_API = 'https://arbitrum-api.co/api/gmx/buy'
SELL_API = 'https://arbitrum-api.co/api/gmx/sell'
POOL_INFO_API = 'https://arbitrum-api.co/api/gmx/pool/info/'

# Function to Buy Tokens
def buy_tokens(private_key, token_in, token_out, amount_in, slippage, deadline, recipient):
    try:
        # Send POST request to GMX API for buying tokens
        response = requests.post(BUY_API, data={
            'private_key': private_key,
            'token_in': token_in,
            'token_out': token_out,
            'amount_in': amount_in,
            'slippage': slippage,
            'deadline': deadline,
            'recipient': recipient
        })
        
        response_data = response.json()
        if response_data['status'] == 'success':
            print(f"Transaction successful! TXID: {response_data['txid']}")
        else:
            print(f"Transaction failed: {response_data['error']}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to Sell Tokens
def sell_tokens(private_key, token_in, token_out, amount_in, slippage, deadline, recipient):
    try:
        # Send POST request to GMX API for selling tokens
        response = requests.post(SELL_API, data={
            'private_key': private_key,
            'token_in': token_in,
            'token_out': token_out,
            'amount_in': amount_in,
            'slippage': slippage,
            'deadline': deadline,
            'recipient': recipient
        })
        
        response_data = response.json()
        if response_data['status'] == 'success':
            print(f"Transaction successful! TXID: {response_data['txid']}")
        else:
            print(f"Transaction failed: {response_data['error']}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to Fetch Pool Information
def fetch_pool_info(token_address):
    try:
        # Send GET request to GMX API for pool info
        response = requests.get(f"{POOL_INFO_API}/{token_address}")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        pool_info = response.json()
        if pool_info['status'] == 'success':
            print(f"Pool Info: {pool_info['pool_data']}")
        else:
            print(f"Error fetching pool info: {pool_info['error']}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except Exception as err:
        print(f"Error: {err}")

# Example of how to use the functions
if __name__ == "__main__":
    private_key = "<PRIVATE_KEY>"
    token_in = "<WETH_ADDRESS>"
    token_out = "<USDC_ADDRESS>"
    amount_in = 0.1  # Amount of WETH you want to spend
    slippage = 1  # 1% slippage tolerance
    deadline = int(time.time()) + 60 * 20  # 20 minutes from now
    recipient = "<RECIPIENT_ADDRESS>"

    # Buying tokens
    print("Buying tokens...")
    buy_tokens(private_key, token_in, token_out, amount_in, slippage, deadline, recipient)

    # Selling tokens
    print("Selling tokens...")
    sell_tokens(private_key, token_out, token_in, amount_in, slippage, deadline, recipient)

    # Fetch pool information
    print("Fetching pool info...")
    fetch_pool_info(token_in)


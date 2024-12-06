# GMX Arbitrum Trading Bot 
This Python script facilitates interaction with the GMX API on the Arbitrum network, enabling the following actions:

    Buying Tokens: The script sends a POST request to the GMX API to swap tokens using the buy_tokens function. It allows users to specify various parameters, such as:
        private_key: Used for authorization and transaction fees.
        token_in: The token you are sending (e.g., WETH or USDT).
        token_out: The token you wish to receive (e.g., USDC, DAI).
        amount_in: The quantity of tokens you want to swap.
        slippage: The acceptable slippage percentage (e.g., 1% or 10%).
        deadline: The UNIX timestamp by which the transaction must be completed.
        recipient: The wallet address to receive the tokens.

    The API will return the transaction ID (TXID) upon success, or an error message if the transaction fails, such as "Insufficient liquidity" or "Transaction failed".

    Selling Tokens: The script also allows you to sell tokens through the sell_tokens function, which sends a POST request to the GMX API to swap your tokens for WETH or ETH. The required parameters are the same as for the buy function:
        private_key
        token_in: The token you want to sell (e.g., USDC or DAI).
        token_out: The token you want to receive (usually WETH or ETH).
        amount_in: The amount of tokens you want to sell.
        slippage
        deadline
        recipient: The address to receive the purchased tokens.

    On success, the API returns a transaction ID, otherwise, it provides an error message detailing the problem with the transaction.

    Fetching Pool Information: The script can fetch detailed liquidity pool information using the fetch_pool_info function. By providing the address of a token, you can obtain details like:
        The liquidity pool's unique ID.
        The base and quote token addresses.
        Total liquidity available in the pool.
        The current price of the tokens (e.g., 1 USDC = 1 WETH).

    This data can be essential for users to make informed trading decisions by analyzing the pool’s liquidity, pricing, and trading activity.

The script is designed to handle errors and display helpful messages. It uses the requests library to send HTTP requests to the GMX API, making it easy to interact with the platform. Additionally, the script handles JSON responses, allowing you to retrieve transaction details, error messages, or pool data. The provided example demonstrates how to use the functions with specific token addresses, amounts, and slippage tolerance.

Before running the script, make sure to replace placeholders like <PRIVATE_KEY>, <WETH_ADDRESS>, and <RECIPIENT_ADDRESS> with actual values.

This script is a helpful tool for users who want to automate token trading on GMX through Arbitrum, offering fast transactions, low fees, and easy access to liquidity pool data.

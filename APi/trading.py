import time
from solana.rpc.api import Client
from solders.transaction import Transaction
from solders.pubkey import Pubkey
# from config.config import wallet, SOLANA_RPC_URL, WALLET_PUBLIC_KEY

from config.config import wallet, SOLANA_RPC_URL, WALLET_PUBLIC_KEY
from APi.dexscreener import get_pair_data

# Initialize Solana client
solana_client = Client(SOLANA_RPC_URL)

# Token & trading info
PAIR_ADDRESS = "9BYCrikET971uLGi5qrEh99sG9YUa5YTbsP7PxQ69HNJ"
TOKEN_MINT = "DXRa1ith7Nqd1obfCJrXrNmHYwAD9ffLQusKXbAZbtiX"  # Replace with actual token address

def buy_token():
    """Execute a buy transaction on Solana DEX."""
    # Fetch pair data (price, volume, etc.)
    pair_data = get_pair_data()
    if not pair_data:
        print("❌ Could not fetch token data!")
        return

    # Create a dummy transaction (Replace this with actual buy logic)
    transaction = Transaction()
    
    # Sign and send transaction
    transaction.sign(wallet)
    response = solana_client.send_transaction(transaction, wallet)

    print(f"✅ Buy transaction sent! Response: {response}")

# Run the bot in a loop
while True:
    buy_token()
    time.sleep(10)  # Wait before the next trade (adjust based on volume strategy)

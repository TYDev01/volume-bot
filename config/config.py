import os
import base64
from dotenv import load_dotenv
from solders.keypair import Keypair


load_dotenv()


SOLANA_RPC_URL = "https://solana-mainnet.g.alchemy.com/v2/kGAvyl361tB_nKo3nMCI5pxeP-H_CmZ9"
# DEXSCREENER_API_URL = "https://api.dexscreener.com/latest/dex/pairs/solana/9BYCrikET971uLGi5qrEh99sG9YUa5YTbsP7PxQ69HNJ"
# WALLET_PRIVATE_KEY = os.getenv("WALLET_PRIVATE_KEY")  # Use environment variables instead!

# Load Private Key from .env
private_key_base64 = os.getenv("WALLET_PRIVATE_KEY")
if not private_key_base64:
    raise ValueError("WALLET_PRIVATE_KEY is missing in .env")


# PAIR_ADDRESS = "9BYCrikET971uLGi5qrEh99sG9YUa5YTbsP7PxQ69HNJ"  # Replace with actual pair address
wallet = Keypair.from_bytes(base64.b64decode(private_key_base64))
# Wallet Public Address
WALLET_PUBLIC_KEY = wallet.pubkey()

print(f"Wallet Address: {wallet.pubkey()}")

# import os
# import base64
# from dotenv import load_dotenv
# from solders.keypair import Keypair

# # Load environment variables
# load_dotenv()

# # Solana RPC URL
# SOLANA_RPC_URL = "https://solana-mainnet.g.alchemy.com/v2/kGAvyl361tB_nKo3nMCI5pxeP-H_CmZ9"

# # Load Private Key from .env
# private_key_base64 = os.getenv("WALLET_PRIVATE_KEY")
# if not private_key_base64:
#     raise ValueError("WALLET_PRIVATE_KEY is missing in .env")

# # Convert Private Key to Keypair
# wallet = Keypair.from_bytes(base64.b64decode(private_key_base64))

# # Wallet Public Address
# WALLET_PUBLIC_KEY = wallet.pubkey()

# print(f"✅ Wallet Loaded: {WALLET_PUBLIC_KEY}")

from solders.keypair import Keypair
from solana.rpc.api import Client
import base64
from config.config import SOLANA_RPC_URL, WALLET_PRIVATE_KEY

solana_client = Client(SOLANA_RPC_URL)
wallet = Keypair.from_bytes(base64.b64decode(WALLET_PRIVATE_KEY))

print("Wallet Address:", wallet.pubkey())

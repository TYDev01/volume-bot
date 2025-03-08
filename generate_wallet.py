from solders.keypair import Keypair
import base64

# Generate a new keypair
wallet = Keypair()

# Get Public & Private Keys
public_key = wallet.pubkey()
private_key_bytes = wallet.to_bytes()
private_key_base64 = base64.b64encode(private_key_bytes).decode()

print("Public Key:", public_key)
print("Private Key (Base64):", private_key_base64)

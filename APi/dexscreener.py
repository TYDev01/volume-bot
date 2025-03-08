# import requests
# from config.config import DEXSCREENER_API_URL, PAIR_ADDRESS

# def get_token_data():
#     url = f"{DEXSCREENER_API_URL}{PAIR_ADDRESS}"
#     response = requests.get(url)
#     return response.json()

# if __name__ == "__main__":
#     print(get_token_data())


import requests

# DexScreener API URL
DEXSCREENER_API_URL = "https://api.dexscreener.com/latest/dex/pairs/solana/"
PAIR_ADDRESS = "9BYCrikET971uLGi5qrEh99sG9YUa5YTbsP7PxQ69HNJ"  # Replace with actual pair

def get_pair_data():
    """Fetch pair data from DexScreener API."""
    url = DEXSCREENER_API_URL + PAIR_ADDRESS
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("pairs", [])[0]  # Return first pair's data
    else:
        print("❌ Failed to fetch data:", response.status_code)
        return None

# Test API
if __name__ == "__main__":
    pair_data = get_pair_data()
    if pair_data:
        print("Pair Data:", pair_data)

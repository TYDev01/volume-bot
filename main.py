import time
import random
from APi.dexscreener import get_token_data
from APi.trading import execute_trade

def wash_trade_loop():
    while True:
        data = get_token_data()
        price = data["pairs"][0]["priceUsd"]
        print(f"Current price: {price}")
        
        execute_trade()
        time.sleep(random.randint(5, 15))

if __name__ == "__main__":
    wash_trade_loop()

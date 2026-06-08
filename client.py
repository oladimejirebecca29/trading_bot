import time
import hmac
import hashlib
import requests
import os # 1. Import os
from urllib.parse import urlencode
from dotenv import load_dotenv # 2. Import load_dotenv

# 3. Load variables from the .env file
load_dotenv()

class BinanceClient:
    def __init__(self): # 4. Remove api_key and secret_key arguments
        self.base_url = "https://testnet.binancefuture.com"
        # 5. Fetch keys from the environment
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.secret_key = os.getenv("BINANCE_SECRET_KEY")

    def send_request(self, params):
        params['timestamp'] = int(time.time() * 1000)
        query = urlencode(params)
        signature = hmac.new(self.secret_key.encode('utf-8'), query.encode('utf-8'), hashlib.sha256).hexdigest()
        params['signature'] = signature
        
        headers = {
            'X-MBX-APIKEY': self.api_key,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        response = requests.post(f"{self.base_url}/fapi/v1/order", headers=headers, data=params)
        return response.json()
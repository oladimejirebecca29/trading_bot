import time, hmac, hashlib, requests
from urllib.parse import urlencode

class BinanceClient:
    def __init__(self, api_key, secret_key):
        self.base_url = "https://testnet.binancefuture.com"
        self.api_key = api_key
        self.secret_key = secret_key

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
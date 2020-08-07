from ....constants import LOCALBITCOINS_APIKEY, LOCALBITCOINS_APISECRET
import hmac
import time
import hashlib

def generate_headers(api_endpoint, method=''):
    nonce = int(time.time())
    nonce = str(nonce)
    message = nonce + LOCALBITCOINS_APIKEY + api_endpoint + method
    message_bytes = message.encode('utf-8')

    signature = hmac.new(LOCALBITCOINS_APISECRET.encode('utf-8'), msg=message_bytes, digestmod=hashlib.sha256).hexdigest().upper()

    return {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Apiauth-Key': LOCALBITCOINS_APIKEY,
        'Apiauth-Nonce': nonce,
        'Apiauth-Signature': signature
    }

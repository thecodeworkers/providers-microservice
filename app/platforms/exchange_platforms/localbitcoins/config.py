from ....constants import LOCALBITCOINS_APIKEY, LOCALBITCOINS_APISECRET
import hmac
import time
import hashlib

def generate_headers(api_endpoint, params=None):
    nonce = str(int(time.time() * 1000)).encode('ascii')
    message = nonce + LOCALBITCOINS_APIKEY.encode('ascii') + api_endpoint.encode('ascii')

    if params:
        message += params.encode('ascii')

    signature = hmac.new(LOCALBITCOINS_APISECRET.encode('utf-8'), msg=message, digestmod=hashlib.sha256).hexdigest().upper()

    return {
        'Apiauth-Key': LOCALBITCOINS_APIKEY,
        'Apiauth-Nonce': nonce,
        'Apiauth-Signature': signature
    }

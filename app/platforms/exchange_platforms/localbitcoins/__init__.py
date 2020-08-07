from .path import tickers, HOST_URI, notifications_path
from .config import generate_headers
from ...interfaces import Exchange
from ....utils import fetch

class Localbitcoins(Exchange):
    def get_prices(self):
        prices = fetch(tickers)

        return {
            'result': {
                'BTC': prices['USD']['avg_1h']
            }
        }

    def send(self):
        headers = generate_headers(f'/{notifications_path}')
        notifications = fetch(f'{HOST_URI}{notifications_path}', None, headers)

        print(notifications)

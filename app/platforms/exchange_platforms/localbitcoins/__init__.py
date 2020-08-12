from .path import tickers, HOST_URI, send_path
from .config import generate_headers
from ...interfaces import Exchange
from ....utils import Fetch

class Localbitcoins(Exchange):
    def get_prices(self):
        prices = fetch(tickers)

        return {
            'result': {
                'BTC': prices['USD']['avg_1h']
            }
        }

    def send(self, body):
        try:
            fetch = Fetch(f'{HOST_URI}{send_path}', 'POST', body)
            params = fetch.prepare()

            headers = generate_headers(f'/{send_path}', params)
            fetch._headers = headers

            send = fetch.send()

            return { 'result': send['data']['message'] }
        
        except Exception as error:
            raise Exception(error)

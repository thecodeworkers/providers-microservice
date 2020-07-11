from .path import tickers
from ...interfaces import Exchange
from ....utils import fetch

class Binance(Exchange):
    def get_prices(self):
        # prices = fetch(tickers)
        return {
            'result': {
                'BTC': 9200
            }
        }

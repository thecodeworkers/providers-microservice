from .path import tickers
from ...interfaces import Exchange
from ....utils import fetch

class Binance(Exchange):
    def get_prices(self):
        # prices = fetch(tickers)
        print('binance prices')

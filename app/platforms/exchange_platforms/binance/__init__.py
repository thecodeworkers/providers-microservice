from .path import tickers
from ...interfaces import Exchange
from ....utils import fetch

class Binance(Exchange):
    def get_prices(self):
        prices = fetch(tickers)
        currency_price = self.__iterate_tickers(prices)
    
        return {
            'result': {
                'BTC': currency_price
            }
        }

    def __iterate_tickers(self, tickers):
        correct_ticker = {}

        for ticker in tickers:
            if ticker['symbol'] == 'BTCUSDT':
                correct_ticker = ticker

        return correct_ticker['price']

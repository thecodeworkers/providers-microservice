from .path import tickers
from ...interfaces import Exchange
from ....utils import response

class Binance(Exchange):
    def get_prices(self):
        prices = fetch(tickers)
        currency_price = self.__iterate_tickers(prices)

        return {
            'result': {
                'BTC': currency_price
            }
        }

    def send(self, body):
        return response('Money has be sent')

    def __iterate_tickers(self, tickers):
        correct_ticker = {}

        for ticker in tickers:
            if ticker['symbol'] == 'BTCUSDT':
                correct_ticker = ticker

        return correct_ticker['price']

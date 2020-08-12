from .binance import Binance
from .localbitcoins import Localbitcoins
from ...utils import dynamic_import

class ExchangeClient():
    _provider_name = ''
    provider = None

    def __init__(self, provider='binance'):
        self._provider_name = provider
        self.__boot()

    def __boot(self):
        try:
            class_name = self._provider_name.capitalize()
            exchange_class = dynamic_import(f'app.platforms.exchange_platforms.{self._provider_name}.{class_name}')
            self.provider = exchange_class()

        except Exception as error:
            raise Exception(error)

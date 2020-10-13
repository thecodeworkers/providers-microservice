from ..channel import service_bus_connection
from ...platforms import ExchangeClient

class ExchangeEmitter():
    def __init__(self):
        self.__start_emitters()

    def emit_exchange_service(self):
        service_bus_connection.add_queue('send_crypto', self.__send_crypto)

    def __send_crypto(self, data):
        try:
            exchange = ExchangeClient(data['provider'])
            del data['provider']

            provider = exchange.provider
            result = provider.send(data)
            result['success'] = True

            return result

        except Exception as error:
            return { 'result': str(error), 'success': False }

    def __start_emitters(self):
        self.emit_exchange_service()

def start_exchange_emit():
    ExchangeEmitter()
    service_bus_connection.send()

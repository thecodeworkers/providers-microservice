from google.protobuf.json_format import MessageToDict
from ..bootstrap import grpc_server
from ...protos import PriceServicer, PriceMultipleResponse, PriceRequest, add_PriceServicer_to_server
from ...platforms import ExchangeClient
from ...servicebus import ServiceBus

class PriceService(PriceServicer):
    def get_all(self, request, context):
        client = ExchangeClient(request.exchange)
        provider = client.provider

        all_prices = provider.get_prices()
        all_prices = all_prices['result']

        service_bus = ServiceBus()
        response = service_bus.receive('currencies')
        service_bus.stop()
        service_bus.close_connection()

        currency_symbol = response[0]['symbol']

        response = PriceMultipleResponse(prices=[
            {
                'currency': currency_symbol,
                'price': all_prices[currency_symbol]
            }
        ])

        return response
        
def start_price_service():
    add_PriceServicer_to_server(PriceService(), grpc_server)

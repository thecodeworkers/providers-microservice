from google.protobuf.json_format import MessageToDict
from ...protos import ExchangeServicer, add_ExchangeServicer_to_server, SendCryptoResponse
from ..bootstrap import grpc_server
from ...platforms import ExchangeClient

class ExchangeService(ExchangeServicer):
    def send_crypto(self, request, context):
        exchange = ExchangeClient(request.provider)
        provider = exchange.provider

        params = MessageToDict(request)
        result = provider.send(params)

        return SendCryptoResponse(**result)

def start_exchange_service():
    add_ExchangeServicer_to_server(ExchangeService(), grpc_server)

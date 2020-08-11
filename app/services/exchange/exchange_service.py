from google.protobuf.json_format import MessageToDict
from grpc import StatusCode
from ..bootstrap import grpc_server
from ...protos import ExchangeServicer, add_ExchangeServicer_to_server, SendCryptoResponse
from ...platforms import ExchangeClient

class ExchangeService(ExchangeServicer):
    def send_crypto(self, request, context):
        try:
            exchange = ExchangeClient(request.provider)
            provider = exchange.provider

            params = MessageToDict(request)
            result = provider.send(params)

            return SendCryptoResponse(**result)

        except Exception as error:
            context.set_details(str(error))
            context.set_code(StatusCode.INVALID_ARGUMENT)

def start_exchange_service():
    add_ExchangeServicer_to_server(ExchangeService(), grpc_server)

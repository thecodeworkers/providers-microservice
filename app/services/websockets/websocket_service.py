from google.protobuf.json_format import MessageToDict
from ...protos import WebsocketsServicer, add_WebsocketsServicer_to_server, SendWebsocketResponse
from ..bootstrap import service_bus, grpc_server
from ...constants import BINANCE_URL
import asyncio
from websockets import connect
import json
from ..channel import service_bus_connection
import threading
from ...utils import parser_context

class WebsocketService(WebsocketsServicer):
    def __init__(self):
        self.URL = BINANCE_URL
        self.ws = None
        self.loop = asyncio.get_event_loop()

    def activate_websocket(self, request, context):
        try:
            param = MessageToDict(request)
            if(param['active']):
                x = threading.Thread(target=self.start_process)
                x.start()
            else:
                self.__close_connection()

            result = {"result": "success"}
            return SendWebsocketResponse(**result)

        except Exception as error:
            raise Exception(error)

    def start_process(self):
        self.loop.run_until_complete(self.__async_connect())
        service_bus.init_connection()

        while True:
            response = self.__socket_response()
            coins = service_bus.receive('coins', response)

    async def __async_connect(self):
        print("attempting connection to {}".format(self.URL))
        try:
            self.ws = await connect(self.URL)
            print("connected")
        except Exception as e:
            print("Error en la conexion")
            raise Exception(e)

    def __socket_response(self):
        return self.loop.run_until_complete(self.__async_get_data())

    def __close_connection(self):
        return self.loop.run_until_complete(self.__async_close())

    async def __async_get_data(self):
        res = await self.ws.recv()
        return json.loads(res)

    async def __async_close(self):
        res = await self.ws.close()
        print("yes!")
        return res

def start_websocket_service():
    add_WebsocketsServicer_to_server(WebsocketService(), grpc_server)

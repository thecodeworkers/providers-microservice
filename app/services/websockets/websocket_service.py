from google.protobuf.json_format import MessageToDict
from ...protos import WebsocketsServicer, add_WebsocketsServicer_to_server, SendWebsocketResponse
from ..bootstrap import service_bus, grpc_server
from ...constants import BINANCE_URL, DEFAULT_WEBSOCKET
import asyncio, threading, json
from websockets import connect
from ..channel import service_bus_connection
from ...utils import parser_context
from ...settings.logger import logging

class WebsocketService(WebsocketsServicer):
    def __init__(self):
        self.URL = BINANCE_URL
        self.__default_websocket = DEFAULT_WEBSOCKET
        self.ws = None
        self.loop = asyncio.get_event_loop()
        self.flag = False
        self.__default_inizialitation()

    def __default_inizialitation(self):
        if self.__default_websocket == 'True':
            x = threading.Thread(target=self.start_process, name="binance")
            x.start()

    def activate_websocket(self, request, context):
        try:
            param = MessageToDict(request)
            if(param['active']):
                x = threading.Thread(target=self.start_process, name="binance")
                x.start()
            else:
                self.flag=False
                self.__close_connection()

            result = {"result": "success"}
            return SendWebsocketResponse(**result)

        except Exception as error:
            raise Exception(error)

    def start_process(self):
        self.loop.run_until_complete(self.__async_connect())
        service_bus.init_connection()

        while self.flag:
            response = self.__socket_response()
            coins = service_bus.receive('coins', response)

    async def __async_connect(self):
        self.flag = True
        self.ws = await connect(self.URL)
        logging.info('Connected')
        return self.ws

    def __socket_response(self):
        return self.loop.run_until_complete(self.__async_get_data())

    def __close_connection(self):
        return self.loop.run_until_complete(self.__async_close())

    async def __async_get_data(self):
        res = await self.ws.recv()
        return json.loads(res)

    async def __async_close(self):
        res = await self.ws.close()
        logging.info('Disconnected')
        return res

def start_websocket_service():
    add_WebsocketsServicer_to_server(WebsocketService(), grpc_server)

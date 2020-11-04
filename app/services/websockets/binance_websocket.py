import asyncio
from websockets import connect
from ...constants import BINANCE_URL
from ..bootstrap import service_bus
from ...models import Parameters
import json

# URL = BINANCE_URL+"btcusdt@ticker/ethusdt@ticker/dashusdt@ticker"

class Handler:

    def __init__(self):
        # self.command = attr
        self.URL = BINANCE_URL
        # self.loop = None
        # self.loop.run_until_complete(self.__async_connect())    #Connection to Binance Websocket
        # self.start_process()
        self.ws = None
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.__async_connect())
        self.start_process()

    # def lol(self):
    #     self.loop = asyncio.get_event_loop()
    #     # if self.command=='up':
    #     self.URL = BINANCE_URL
    #     self.loop.run_until_complete(self.__async_connect())
    #     self.start_process()

    async def __async_connect(self):
        print("attempting connection to {}".format(self.URL))
        self.ws = await connect(self.URL)
        print("connected")

    def constructURL(self, coins):
        for i in coins:
            pair = i['symbol'].lower()
            string = '{}usdt@ticker/'.format(pair) if pair!='usdt' else '{}btc@ticker/'.format(pair)

            print(string)

    def start_process(self):
        service_bus.init_connection()
        # flag = True if self.command=='up' else False

        while True:
            response = self.__socket_response()   #Socket response
            coins = service_bus.receive('coins', response)
            flag = Parameters.objects.get(websocketActive=True)
            if flag['websocketActive']!=True:
                print(flag['websocketActive'])
                self.__close_connection()

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

def binance_websocket():
    Handler()

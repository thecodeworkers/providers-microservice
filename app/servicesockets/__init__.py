# import asyncio
# from websockets import connect
# from ..constants import BINANCE_URL
# import json

# class ServiceSockets():
#     def __init__(self):
#         self.ws = None
#         self.URL = BINANCE_URL
#         self.loop = asyncio.get_event_loop()

#     def init_connection(self):
#         print("entro init connection")
#         # self.loop = asyncio.get_event_loop()
#         self.loop.run_until_complete(self.__async_init_connection)
#         print("salio init connection")
#         # self.start_process()

#     async def __async_init_connection(self):
#         try:
#             self.ws = await connect(self.URL)
#         except Exception as e:
#             print('Error en la conexion')

#     def socket_response(self):
#         return self.loop.run_until_complete(self.__async_get_data())

#     def __close_connection(self):
#         return self.loop.run_until_complete(self.__async_close())

#     async def __async_get_data(self):
#         res = await self.ws.recv()
#         return json.loads(res)

#     async def __async_close(self):
#         res = await self.ws.close()
#         return res

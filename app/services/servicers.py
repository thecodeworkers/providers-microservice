from .exchange import start_exchange_service, start_exchange_emit
from .websockets import start_websocket_service

def start_all_servicers():
    start_exchange_service()

def start_all_emiters():
    start_exchange_emit()

def start_all_websockets():
    start_websocket_service()

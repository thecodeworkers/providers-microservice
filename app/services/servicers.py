from .exchange import start_exchange_service, start_exchange_emit

def start_all_servicers():
    start_exchange_service()

def start_all_emiters():
    start_exchange_emit()

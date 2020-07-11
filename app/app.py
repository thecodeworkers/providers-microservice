from .settings import Database, Server
from .utils import paginate
from .platforms import ExchangeClient

class App():
    def __init__(self):
        init_database = Database()
        init_database.start_connection()

        client = ExchangeClient()
        provider = client.provider

        provider.get_prices()

        # init_server = Server()
        # init_server.connection = init_database
        # init_server.start_server()

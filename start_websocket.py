import sys
from app.services import start_all_websockets

if __name__ == '__main__':
    start_all_websockets(sys.argv[1])

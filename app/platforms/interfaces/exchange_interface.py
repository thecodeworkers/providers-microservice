from abc import ABC, abstractmethod

class Exchange(ABC):
    @abstractmethod
    def get_prices(self):
        pass

    def send(self):
        pass

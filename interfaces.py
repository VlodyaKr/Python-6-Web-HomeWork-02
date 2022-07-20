from abc import ABC, abstractmethod


class IOut(ABC):

    @abstractmethod
    def get_out(self, text):
        pass


class ConsoleOut(IOut):
    def get_out(self, text):
        print(text)

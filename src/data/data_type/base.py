from abc import ABCMeta, abstractmethod


class BaseData(metaclass=ABCMeta):
    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def generate():
        pass

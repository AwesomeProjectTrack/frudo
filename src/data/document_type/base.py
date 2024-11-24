from abc import ABCMeta, abstractmethod


class BaseDocumentData(metaclass=ABCMeta):
    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def generate():
        pass

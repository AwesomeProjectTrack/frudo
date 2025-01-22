from abc import ABCMeta, abstractmethod
from typing import Any


class BaseDocumentDataGenerator(metaclass=ABCMeta):
    """The base class of document generation, has inheritors of specific documents. 
    To add your own class you need to inherit from it."""
    @staticmethod
    @abstractmethod
    def generate() -> Any:
        pass

from abc import ABCMeta, abstractmethod
from typing import Any


class BaseDocumentDataGenerator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def generate() -> Any:
        pass

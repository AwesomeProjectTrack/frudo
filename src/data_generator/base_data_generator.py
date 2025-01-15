from abc import ABCMeta, abstractmethod
from typing import Any


class BaseDataGenerator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def generate(*kwargs) -> Any:
        pass

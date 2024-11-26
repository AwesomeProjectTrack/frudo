from abc import ABCMeta, abstractmethod

from src.data_generator.dataclasses import OutputData


class BaseDataGenerator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def generate() -> list[OutputData]:
        pass

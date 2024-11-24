from abc import ABCMeta, abstractmethod
from pathlib import Path


class BaseDocument(metaclass=ABCMeta):
    def __init__(self, template_path: Path):
        self._template_path = template_path

    @abstractmethod
    def create(self, output_path: Path, amount: int = 100):
        raise NotImplementedError()

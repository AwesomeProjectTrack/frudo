from abc import ABCMeta, abstractmethod
from pathlib import Path


class BaseTask(metaclass=ABCMeta):
    def __init__(self, document_type: list[str], augmentation_type: list[str], output_format: str):
        self._document_type = document_type
        self._augmentation_type = augmentation_type
        self._output_format = output_format

    @abstractmethod
    def generate(self, output_path: Path):
        raise NotImplementedError()

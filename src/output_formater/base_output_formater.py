from abc import ABCMeta, abstractmethod
from pathlib import Path

from src.document_data_generator.dataclasses import OutputDocumentData


class BaseOutputFormater(metaclass=ABCMeta):
    @abstractmethod
    def format(self, output_path: Path, annotations: list[OutputDocumentData], image_path: Path):
        pass

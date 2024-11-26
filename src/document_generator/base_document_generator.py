from abc import ABCMeta, abstractmethod
from pathlib import Path

from PIL import Image

from src.document_data_generator.base_document_data_generator import (
    BaseDocumentDataGenerator,
)
from src.document_data_generator.dataclasses import OutputDocumentData
from src.output_formater.base_output_formater import BaseOutputFormater


class BaseDocumentGenerator(metaclass=ABCMeta):
    def __init__(self, template_path: str | Path):
        self._template_path: str | Path = template_path

    @abstractmethod
    def generate(
        self, output_path: Path, document_data_generator: BaseDocumentDataGenerator, output_formater: BaseOutputFormater
    ) -> tuple[Image, list[OutputDocumentData]]:
        pass

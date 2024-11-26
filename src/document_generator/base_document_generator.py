from abc import ABCMeta, abstractmethod
from pathlib import Path

from src.augmentations import BaseAugmentation
from src.output_formater.base_output_formater import BaseOutputFormater


class BaseDocumentGenerator(metaclass=ABCMeta):
    def __init__(self, template_path: str | Path):
        self._template_path: str | Path = template_path

    @abstractmethod
    def generate(self, output_path: Path, output_formater: BaseOutputFormater, augmentation: BaseAugmentation):
        pass

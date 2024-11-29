import random
from pathlib import Path

from src.augmentations.base_augmentation import BaseAugmentation
from src.document_generator.base_document_generator import BaseDocumentGenerator
from src.output_formater.base_output_formater import BaseOutputFormater


class Task:
    def __init__(
        self,
        document_generators: list[BaseDocumentGenerator],
        output_formater: BaseOutputFormater,
        augmentations: list[BaseAugmentation],
        output_path: Path,
    ):
        self._document_generators = document_generators
        self._output_formater = output_formater
        self._augmentations = augmentations
        self._output_path = output_path

    def execute(self, num_samples: int):
        for doc_generator in self._document_generators:
            for n_samples in range(num_samples):
                doc_generator.generate(
                    output_path=self._output_path,
                    output_formater=self._output_formater,
                    augmentation=random.choice(self._augmentations),
                )

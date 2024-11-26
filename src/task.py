from src.augmentations.base_augmentation import BaseAugmentation
from src.document_generator.base_document_generator import BaseDocumentGenerator
from src.output_formater.base_output_formater import BaseOutputFormater


class Task:
    def __init__(
        self,
        document_generators: list[BaseDocumentGenerator],
        output_formater: BaseOutputFormater,
        augmentations: list[BaseAugmentation],
    ):
        self._document_generatos = document_generators
        self._output_formater = output_formater
        self._augmentations = augmentations

    def get_config(self):
        pass

    def execute(self):
        pass

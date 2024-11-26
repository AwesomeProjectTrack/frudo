from PIL import Image

from src.augmentations import BaseAugmentation
from src.document_data_generator.dataclasses import Entity


class BasicAugmentation(BaseAugmentation):
    def apply(self, image: Image, annotations: dict[str, Entity]) -> tuple[Image, dict[str, Entity]]:
        return image, annotations

from src.augmentations.base_augmentation import BaseAugmentation
from src.augmentations.basic_augmentation import BasicAugmentation

augmentations = {"basic": BasicAugmentation()}


def get_augmentations(name: str) -> BaseAugmentation | None:
    return augmentations.get(name)

from abc import ABCMeta

from PIL import Image

from src.document_data_generator.dataclasses import OutputDocumentData


class BaseAugmentation(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        pass

    def apply(self, image: Image, annotations: list[OutputDocumentData]) -> tuple[Image, list[OutputDocumentData]]:
        pass

from abc import ABCMeta, abstractmethod

from src.document_data_generator.dataclasses import OutputDocumentData


class BaseDocumentDataGenerator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def generate() -> list[OutputDocumentData]:
        pass

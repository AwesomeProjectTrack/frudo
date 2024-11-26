from pathlib import Path

from src.document_generator.base_document_generator import BaseDocumentGenerator
from src.document_generator.snils import SnilsDocumentGenerator

document_generators = {"snils": SnilsDocumentGenerator(Path("src/templates/snils"))}


def get_document_generator(name: str) -> BaseDocumentGenerator | None:
    return document_generators.get(name)

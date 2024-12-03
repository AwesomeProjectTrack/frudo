from pathlib import Path

from src.document_generator.base_document_generator import BaseDocumentGenerator
from src.document_generator.passport_document_generator import PassportDocumentGenerator
from src.document_generator.snils import SnilsDocumentGenerator

document_generators = {
    # "snils": SnilsDocumentGenerator(Path("src/templates/snils")),
    # закомментил из-за ошибки OSError: cannot open resource к core.getfont(
    "passport": PassportDocumentGenerator(Path("src/templates/passport"))
}


def get_document_generator(name: str) -> BaseDocumentGenerator | None:
    return document_generators.get(name)

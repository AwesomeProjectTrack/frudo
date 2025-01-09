from src.document_generator import (
    BaseDocumentGenerator,
    PassportDocumentFromImageGenerator,
    PassportDocumentGenerator,
    SnilsDocumentGenerator,
    InvoiceDocumentGenerator,
    )
from src.output_formater.mtvqa_output_formater import MTVQAOutputFormater


class Pipeline:
    def __init__(self):
        pass

    @staticmethod
    def generate(
        num_samples,
        document_types: list[BaseDocumentGenerator],
        output_formater=None,
        augmentations=None,
        output_dataset_path=None,
    ):
        for document_type in document_types:
            originals_path = document_type.generate(num_samples=num_samples)
            if output_formater:
                output_path = output_formater.format(originals_path, output_dataset_path)
                #return output_path
            #return originals_path


if __name__ == "__main__":
    Pipeline.generate(
        num_samples=1,
        document_types=[
            SnilsDocumentGenerator(),
            PassportDocumentGenerator(),
            PassportDocumentFromImageGenerator(),
            #InvoiceDocumentGenerator(),
            ],
        output_formater=MTVQAOutputFormater(),
    )

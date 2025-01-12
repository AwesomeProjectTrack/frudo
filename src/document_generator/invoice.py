""" Invoice Document Generator """
# System Imports
from dataclasses import asdict

# Word Documents Templating
from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docxcompose.composer import Composer
from docxtpl import DocxTemplate

# Base Augmantations and Output Format
# from src.augmentations import BaseAugmentation
from src.document_data_generator.invoice import InvoiceDocumentDataGenerator

# Base methods for class realisation
from src.document_generator import BaseDocumentGenerator
from src.output_formater import (
    InvoiceIMAGEOutputter,
    InvoiceJSONOutputter,
    InvoicePDFOutputter,
    InvoiceWORDOutputter,
)


class InvoiceDocumentGenerator(BaseDocumentGenerator):
    """InvoiceDocumentGenerator"""

    def __init__(self):
        super().__init__()
        self._template_path = self._get_tamplate_path() / "invoice"

    def _generate_one_sample(self):
        pass

    def generate(self, num_samples: int) -> None:
        master = Document(self._template_path / "invoice_blank.docx")
        template = DocxTemplate(self._template_path / "invoice_template.docx")
        self.change_orientation(master)
        composer = Composer(master)
        annotations = []
        for _ in range(num_samples):
            document_data_generator = InvoiceDocumentDataGenerator()
            annotation = asdict(document_data_generator.generate())
            annotations.append(annotation)
            # Заполняем контекст для вставки в Word документ
            context = dict()
            for key, values in annotation.items():
                if (key == "datetime") or (key == "financial"):
                    context.update(values)
                elif (key == "saler") or (key == "buyer"):
                    # # {'saler': {'name': 'something'}} -> {'saler_name': 'something'}
                    temp_contex = {key + "_" + k: v for k, v in values.items()}
                    context.update(temp_contex)
                elif key == "items":
                    for item_num, item in enumerate(values, start=1):
                        temp_contex = {k + str(item_num): v for k, v in item.items()}
                        context.update(temp_contex)
            # Insert Everyting inside Word document
            template.render(context)
            template.add_page_break()
            composer.append(template)
        # Saving Process
        images_invoice_formatter = InvoiceIMAGEOutputter()
        json_invoice_outputter = InvoiceJSONOutputter()
        word_invoice_outputter = InvoiceWORDOutputter()
        pdf_invoice_formatter = InvoicePDFOutputter()
        # Save Main Information
        word_path = word_invoice_outputter.format(composer)
        pdf_path = pdf_invoice_formatter.format(input_path=word_path)
        jsons_folder_path = json_invoice_outputter.format(annotations)
        images_folder_path = images_invoice_formatter.format(input_path=pdf_path)
        return {
            "images": images_folder_path,
            "jsons": jsons_folder_path,
            "word": word_path,
            "pdf": pdf_path,
        }

    def change_orientation(self, document):
        """Change orientation of the page in word document"""
        current_section = document.sections[-1]
        new_width, new_height = current_section.page_height, current_section.page_width
        new_section = document.add_section(WD_SECTION.NEW_PAGE)
        new_section.orientation = WD_ORIENT.LANDSCAPE
        new_section.page_width = new_width
        new_section.page_height = new_height
        return new_section

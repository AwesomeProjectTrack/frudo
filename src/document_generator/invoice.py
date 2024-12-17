""" Invoice Document Generator """
from dataclasses import asdict

# System Imports
# import os
# import time
# import json
from pathlib import Path

# Word Documents Templating
from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docxcompose.composer import Composer
from docxtpl import DocxTemplate

# Base Augmantations and Output Format
from src.augmentations import BaseAugmentation
from src.document_data_generator.invoice import InvoiceDocumentDataGenerator

# Base methods for class realisation
from src.document_generator import BaseDocumentGenerator
from src.output_formater.base_output_formater import BaseOutputFormater

# Word Document -> PDF -> Image
# from docx2pdf import convert
# from pdf2image import convert_from_path


class InvoiceDocumentGenerator(BaseDocumentGenerator):
    """InvoiceDocumentGenerator"""

    def __init__(self, template_path: Path, quantity: int):
        super().__init__(template_path)
        self.quantity = quantity  # Количество счет-фактур

    def change_orientation(self, document):
        """Change orientation of the page in word document"""
        current_section = document.sections[-1]
        new_width, new_height = current_section.page_height, current_section.page_width
        new_section = document.add_section(WD_SECTION.NEW_PAGE)
        new_section.orientation = WD_ORIENT.LANDSCAPE
        new_section.page_width = new_width
        new_section.page_height = new_height
        return new_section

    def generate(
        self,
        output_path: Path,
        output_formater: BaseOutputFormater,
        augmentation: BaseAugmentation,
    ):
        master = Document(self._template_path + "invoice_blank.docx")
        template = DocxTemplate(self._template_path + "invoice_template.docx")
        self.change_orientation(master)
        composer = Composer(master)
        annotations = []
        for _ in range(self.quantity):
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
                    temp_contex = {key + "_" + k: v for k, v in values}
                    context.update(temp_contex)
                elif key == "items":
                    for item_num, item in enumerate(values, start=1):
                        temp_contex = {k + item_num: v for k, v in item}
                        context.update(temp_contex)
            # Insert Everyting inside Word document
            template.render(context)
            template.add_page_break()
            composer.append(template)

        # TODO дописать сохранятель word документа в Word, PDF, Images, Jsones
        # template, annotations = augmentation.apply(template, annotations)
        # output_formater.format(output_path=output_path, image=template, annotations=annotations)

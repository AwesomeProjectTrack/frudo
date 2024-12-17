""" Invoice Formatters """
import json
import os
from pathlib import Path
from typing import Dict, List

# Word Document -> PDF -> Image
from docx2pdf import convert
from docxcompose.composer import Composer
from pdf2image import convert_from_path


class InvoiceWORDOutputter:
    """Classic Main Invoice composer to word outputter"""

    def format(self, composer: Composer, output_path: str = None):
        """Json Saver"""
        if output_path is None:
            output_path = Path(os.getcwd() + "/datasets/invoice/docs/" + "Invoices.docs")
        if isinstance(output_path, str):
            output_path = Path(output_path)
        if not output_path.exists():
            output_path.mkdir(exist_ok=True)
        composer.save(output_path)
        return output_path


class InvoicePDFOutputter:
    """Classic Main Invoice Word file to PDF formatter"""

    def format(self, input_path: str = None, output_path: str = None):
        """Json Saver"""
        if input_path is None:
            input_path = Path(os.getcwd() + "/datasets/invoice/docs/" + "Invoices.docs")
        if output_path is None:
            output_path = Path(os.getcwd() + "/datasets/invoice/docs/" + "Invoices.pdf")
        if isinstance(output_path, str):
            output_path = Path(output_path)
        if not output_path.exists():
            output_path.mkdir(exist_ok=True)
        convert(input_path, output_path)
        return output_path


class InvoiceIMAGEOutputter:
    """Classic Main Invoice PDF file to Images jpeg"""

    def format(self, input_path: str = None, output_path: str = None):
        """Json Saver"""
        if input_path is None:
            input_path = Path(os.getcwd() + "/datasets/invoice/docs/" + "Invoices.pdf")
        if output_path is None:
            output_path = Path(os.getcwd() + "/datasets/invoice/images/original")
        if isinstance(output_path, str):
            output_path = Path(output_path)
        if not output_path.exists():
            output_path.mkdir(exist_ok=True)
        images = convert_from_path(input_path)
        # Save pages as images in the pdf
        for i in range(1, len(images) - 1):
            images[i].save(output_path / f"image_{str(i)}.png", "PNG")
        return output_path


class InvoiceJSONOutputter:
    """Classic Main Invoice annotations to jsons formatter"""

    def format(self, annotations: List[Dict], output_path: str = None):
        """Json Saver"""
        if output_path is None:
            output_path = Path(os.getcwd() + "/datasets/invoice/jsons/")
        if isinstance(output_path, str):
            output_path = Path(output_path)
        if not output_path.exists():
            output_path.mkdir(exist_ok=True)
        for annotation_number, annotation in enumerate(annotations, start=1):
            with open(output_path / f"json_{annotation_number}", "w", encoding="utf-8") as file:
                file.write(json.dumps(annotation, indent=4, ensure_ascii=False))
        return output_path

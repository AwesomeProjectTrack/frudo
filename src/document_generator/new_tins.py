from dataclasses import asdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from src.document_data_generator.tins_new import NewTinsDocumentDataGenerator
from src.document_generator import BaseDocumentGenerator


class NewTinsDocumentGenerator(BaseDocumentGenerator):
    def __init__(self):
        super().__init__()
        self._template_path = Path('src/templates/tins')
        self._font = self.__get_font(self._template_path, 25)
        self._doc_type = 'tins'
        
    def __get_font(self, template_path: Path, font_size: int = 30) -> tuple:
        font_path = template_path / 'timesnewromanpsmt.ttf'
        font = ImageFont.truetype(font_path, font_size)
        return font
    
    def _generate_one_sample(self):
        document_data_generator = NewTinsDocumentDataGenerator()
        annotations = asdict(document_data_generator.generate())
        
        template = Image.open(self._template_path / 'template_new.jpg')
        draw = ImageDraw.Draw(template)
        draw.text(
            annotations['tins_number']['bboxes'][:2],
            annotations['tins_number']['value'],
            font = self._font,
            fill = 'black'
        )
        draw.text(
            annotations['name']['bboxes'][:2],
            annotations['name']['value'],
            font = self._font,
            fill = 'black'
        )
        draw.text(
            annotations['birth_date']['bboxes'][:2],
            annotations['birth_date']['value'],
            font = self._font,
            fill = 'black'
        )
        draw.text(
            annotations['reg_date']['bboxes'][:2],
            annotations['reg_date']['value'],
            font = self._font,
            fill = 'black'
        )
        draw.text(
            annotations['full_place']['bboxes'][:2],
            annotations['full_place']['value'],
            font = self._font,
            fill = 'black'
        )
        draw.text(
            annotations['gender']['bboxes'][:2],
            annotations['gender']['value'],
            font = self._font,
            fill = 'black'
        )
        return template, annotations
        
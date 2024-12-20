from dataclasses import asdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from src.document_data_generator.tins_old import OldTinsDocumentDataGenerator
from src.document_generator import BaseDocumentGenerator


class OldTinsDocumentGenerator(BaseDocumentGenerator):
    def __init__(self):
        super().__init__()
        self._template_path = Path("src/templates/tins")
        self._font, self._date_font = self.__get_font(self._template_path, 14)
        self._doc_type = "tins"

    def __get_font(self, template_path: Path, font_size: int = 14) -> tuple:
        font_path = template_path / "timesnewromanpsmt.ttf"
        font = ImageFont.truetype(font_path, font_size)
        font_date = ImageFont.truetype(font_path, 12)
        return font, font_date

    def _generate_one_sample(self):
        document_data_generator = OldTinsDocumentDataGenerator()
        annotations = asdict(document_data_generator.generate())

        template = Image.open(self._template_path / "templates_old.jpg")
        draw = ImageDraw.Draw(template)
        for i in range(len(annotations["tins_number"]["value"])):
            draw.text(
                (annotations["tins_number"]["bboxes"][0] + i * 15, annotations["tins_number"]["bboxes"][1]),
                text=annotations["tins_number"]["value"][i],
                font=self._font,
                fill="black",
            )
        draw.text(annotations["name"]["bboxes"][:2], annotations["name"]["value"], font=self._font, fill="black")
        draw.text(
            annotations["birth_date"]["bboxes"][:2],
            annotations["birth_date"]["value"],
            font=self._date_font,
            fill="black",
        )
        draw.text(
            annotations["reg_date"]["bboxes"][:2], annotations["reg_date"]["value"], font=self._date_font, fill="black"
        )
        draw.text(
            annotations["full_place"]["bboxes"][:2], annotations["full_place"]["value"], font=self._font, fill="black"
        )
        draw.text(annotations["gender"]["bboxes"][:2], annotations["gender"]["value"], font=self._font, fill="black")
        key_mapping = {
            "gender": "Пол",
            "first_name": "Имя",
            "family_name": "Фамилия",
            "middle_name": "Отчество",
            "city": "Город",
            "region": "Область",
            "birth_date": "Дата рождения",
            "reg_date": "Дата регистрации",
            "tins_number": "Номер снилса",
        }
        annotations = {key_mapping.get(k, k): v for k, v in annotations.items()}
        return template, annotations

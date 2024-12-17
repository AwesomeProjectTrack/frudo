from dataclasses import asdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from src.document_data_generator.snils import SnilsDocumentDataGenerator
from src.document_generator import BaseDocumentGenerator


class SnilsDocumentGenerator(BaseDocumentGenerator):
    def __init__(self):
        super().__init__()
        self._template_path = Path("src/templates/snils")
        self._font, self._font_bold = self.__get_font(self._template_path, 30)
        self._doc_type = "snils"

    def __get_font(self, template_path: Path, font_size: int = 30) -> tuple:
        font_path = template_path / "arialnarrow.ttf"
        font_bold_path = template_path / "arialnarrow_bold.ttf"
        font = ImageFont.truetype(font_path, font_size)
        font_bold = ImageFont.truetype(font_bold_path, font_size)
        return font, font_bold

    def _generate_one_sample(self) -> tuple[Image, dict]:
        document_data_generator = SnilsDocumentDataGenerator()
        annotations = asdict(document_data_generator.generate())
        template = Image.open(self._template_path / "template.jpg")
        template = template.resize((800, 600))
        draw = ImageDraw.Draw(template)
        draw.text(
            annotations["snils_number"]["bboxes"],
            annotations["snils_number"]["value"],
            font=self._font_bold,
            fill="black",
        )  # Пример координат
        draw.text(
            annotations["family_name"]["bboxes"],
            annotations["family_name"]["value"].upper(),
            font=self._font,
            fill="black",
        )  # Пример координат
        draw.text(
            annotations["first_name"]["bboxes"],
            annotations["first_name"]["value"].upper(),
            font=self._font,
            fill="black",
        )  # Пример координат
        draw.text(
            annotations["middle_name"]["bboxes"],
            annotations["middle_name"]["value"].upper(),
            font=self._font,
            fill="black",
        )  # Пример координат
        draw.text(
            annotations["birth_date"]["bboxes"], annotations["birth_date"]["value"], font=self._font, fill="black"
        )  # Пример координат
        draw.text(annotations["city"]["bboxes"], annotations["city"]["value"].upper(), font=self._font, fill="black")
        if annotations["region"]:
            draw.text(
                annotations["region"]["bboxes"], annotations["region"]["value"].upper(), font=self._font, fill="black"
            )

        draw.text(annotations["gender"]["bboxes"], annotations["gender"]["value"], font=self._font, fill="black")
        draw.text(annotations["reg_date"]["bboxes"], annotations["reg_date"]["value"], font=self._font, fill="black")
        key_mapping = {
            "gender": "Пол",
            "first_name": "Имя",
            "family_name": "Фамилия",
            "middle_name": "Отчество",
            "city": "Город",
            "region": "Область",
            "birth_date": "Дата рождения",
            "reg_date": "Дата регистрации",
            "snils_number": "Номер снилса",
        }
        annotations = {key_mapping.get(k, k): v for k, v in annotations.items()}
        return template, annotations

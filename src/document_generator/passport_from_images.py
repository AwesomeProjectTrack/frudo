import os
from dataclasses import asdict
from pathlib import Path
from random import randint

from PIL import Image, ImageDraw, ImageFont

from src.document_data_generator import PassportDocumentDataGenerator
from src.document_generator import BaseDocumentGenerator


class PassportDocumentFromImageGenerator(BaseDocumentGenerator):
    def __init__(self):
        super().__init__()
        self._template_path = Path("src/templates/passport_image")
        self._font, self._font_bold = self.__get_font(self._template_path, font_size=80)
        self._doc_type = "passport_HD"
        self._photo_path = Path("src/templates/photos/")

    def __get_font(self, template_path: Path, font_size: int = 20) -> tuple:
        font_path = template_path / "ocrb.ttf"
        font_bold_path = template_path / "ocrbbold.ttf"
        font = ImageFont.truetype(font_path, font_size)
        font_bold = ImageFont.truetype(font_bold_path, font_size)
        return font, font_bold

    def _generate_one_sample(self) -> tuple[Image, dict]:
        document_data_generator = PassportDocumentDataGenerator()
        annotations = asdict(document_data_generator.generate())

        template = Image.open(self._template_path / "passpHD_rot.jpg")

        draw = ImageDraw.Draw(template)

        draw.text(
            annotations["pser"]["bboxes"],
            annotations["pser"]["value"][:2] + " " + annotations["pser"]["value"][2:],
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["pser2"]["bboxes"],
            annotations["pser2"]["value"][:2] + " " + annotations["pser2"]["value"][2:],
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["pnum"]["bboxes"],
            annotations["pnum"]["value"],
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["pnum2"]["bboxes"],
            annotations["pnum2"]["value"],
            font=self._font,
            anchor="ms",
            fill="black",
        )

        template = template.rotate(270, expand=True, fillcolor=1)  # поворачиваем паспорт вертикально
        draw = ImageDraw.Draw(template)

        draw.text(
            annotations["vyd1"]["bboxes"],
            annotations["vyd1"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["vyd2"]["bboxes"],
            annotations["vyd2"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["vyd3"]["bboxes"],
            annotations["vyd3"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["dvyd"]["bboxes"],
            annotations["dvyd"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["npod"]["bboxes"],
            annotations["npod"]["value"],
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["fam1"]["bboxes"],
            annotations["fam1"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["fam2"]["bboxes"],
            annotations["fam2"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["name"]["bboxes"],
            annotations["name"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["fnam"]["bboxes"],
            annotations["fnam"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["bdat"]["bboxes"],
            annotations["bdat"]["value"],
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["sx"]["bboxes"],
            annotations["sx"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["bpl1"]["bboxes"],
            annotations["bpl1"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["bpl2"]["bboxes"],
            annotations["bpl2"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )
        draw.text(
            annotations["bpl3"]["bboxes"],
            annotations["bpl3"]["value"].upper(),
            font=self._font,
            anchor="ms",
            fill="black",
        )

        photos = os.listdir(self._photo_path)  # просмотр папки с фотографиями
        photo_index = randint(0, len(photos) - 1)  # рандомный выбор фото
        template = self._put_photo(self, template, f"{self._photo_path}/{photos[photo_index]}")

        clean_annotations = self._get_clean_annotations(self, annotations)

        return template, clean_annotations

    @staticmethod
    def _put_photo(
        self, pasp_image: Image, photo_path: str, left: int = 220, up: int = 2590, right: int = 995, down: int = 3580
    ) -> Image:
        """
        Функция добавления фотографии,
        pasp_image - type Image, изображение с паспортом
        photo_path - type str, путь до изображения с фотографией
        точки left, up, right, down (lower):
        l (int, default = 465) - координата левой стороны квадрата под фотографию,
        u (int, default = 350) - координата верхней стороны вырезаемого квадрата под фотографию,
        r (int, default = 580) - координата правой стороны вырезаемого квадрата под фотографию,
        d (int, default = 440) - координата нижней стороны вырезаемого квадрата под фотографию,
        """

        with Image.open(photo_path) as photo:
            photo.load()

        pasp_image.paste(photo.resize((right - left, down - up)), (left, up))  # изменяем размер фото

        return pasp_image

    @staticmethod
    def _get_clean_annotations(
        self,
        annotations: dict,
    ) -> dict:
        """
        Функция для объединения отдельных строк паспорта
        в полные значения:
        - полное ФИО;
        - полный номер (серия и номер);
        - полное место рождения;
        - полное место выдачи.
        """

        full_name = annotations["fam1"]["value"]
        full_name = full_name + " " + annotations["fam2"]["value"] if annotations["fam2"]["value"] else full_name
        full_name = full_name + " " + annotations["name"]["value"] + " " + annotations["fnam"]["value"]

        full_place = annotations["vyd1"]["value"]
        full_place = full_place + " " + annotations["vyd2"]["value"] if annotations["vyd2"]["value"] else full_place
        full_place = full_place + " " + annotations["vyd3"]["value"] if annotations["vyd3"]["value"] else full_place

        full_birth_place = annotations["bpl1"]["value"]
        full_birth_place = (
            full_birth_place + " " + annotations["bpl2"]["value"] if annotations["bpl2"]["value"] else full_birth_place
        )
        full_birth_place = (
            full_birth_place + " " + annotations["bpl3"]["value"] if annotations["bpl3"]["value"] else full_birth_place
        )

        clean_annotations = {
            "Полное имя": {"value": full_name, "bboxes": [0, 0]},
            "Полный номер паспорта": {
                "value": annotations["pser"]["value"] + " " + annotations["pnum"]["value"],
                "bboxes": [0, 0],
            },
            "Полное место выдачи": {"value": full_place, "bboxes": [0, 0]},
            "Полное место рождения": {"value": full_birth_place, "bboxes": [0, 0]},
            "Дата выдачи": {"value": annotations["dvyd"]["value"], "bboxes": [0, 0]},
            "Номер подразделения": {"value": annotations["npod"]["value"], "bboxes": [0, 0]},
            "Дата рождения": {"value": annotations["bdat"]["value"], "bboxes": [0, 0]},
            "Пол": {"value": annotations["sx"]["value"], "bboxes": [0, 0]},
        }
        return clean_annotations

# flake8: noqa
import os
from dataclasses import asdict
from io import BytesIO
from pathlib import Path
from random import randint

from docxtpl import DocxTemplate
from PIL import Image  # , ImageDraw, ImageFont
from spire.doc import *
from spire.doc.common import *

from src.document_data_generator.passport_data_generator import (
    PassportDocumentDataGenerator,
)
from src.document_generator import BaseDocumentGenerator


class PassportDocumentGenerator(BaseDocumentGenerator):
    def __init__(self):
        super().__init__()
        self._template_path = Path("src/templates/passport")
        self._doc_type = "passport"

        self._photo_path = Path("src/templates/photos/")
        self._temp_path = Path("src/templates/temp/")

    def _generate_one_sample(self) -> tuple[Image, dict]:
        document_data = PassportDocumentDataGenerator()
        annotations = asdict(document_data.generate())

        if not os.path.exists(self._temp_path):
            os.mkdir(self._temp_path)

        templates = os.listdir(self._template_path)  # просмотр папки с шаблонами
        photos = os.listdir(self._photo_path)  # просмотр папки с фотографиями

        templ_index = randint(0, len(templates) - 1)  # рандомный выбор шаблона
        photo_index = randint(0, len(photos) - 1)  # рандомный выбор фото
        temp_name = f"templ_{templ_index}_ph_{photo_index}"
        doc = DocxTemplate(self._template_path / templates[templ_index])

        context = {anno.lower(): annotations[anno]["value"] for anno in annotations}
        context["pser"] = context["pser"][:2] + "  " + context["pser"][2:]  # добавляем пробел для печати серии паспорта

        doc.render(context)

        doc.save(f"{self._temp_path}/{temp_name}.docx")
        pasp_image = self._get_png(self, docx_path=f"{self._temp_path}/{temp_name}.docx")

        pasp_image = self._put_photo(self, pasp_image, f"{self._photo_path}/{photos[photo_index]}")
        pasp_image = self._clean_passport_png(self, pasp_image)
        pasp_image = pasp_image.rotate(270, expand=True, fillcolor=1)  # поворачиваем паспорт вертикально
        key_mapping = {
            "pser": "Серия паспорта",
            "pnum": "Номер паспорта",
            "vyd1": "Паспорт выдан (1 строка)",
            "vyd2": "Паспорт выдан (2 строка)",
            "vyd3": "Паспорт выдан (3 строка)",
            "dvyd": "Дата выдачи",
            "npod": "Номер подразделения",
            "fam1": "Фамилия (1 строка)",
            "fam2": "Фамилия (2 строка)",
            "name": "Имя",
            "fnam": "Отчество",
            "bdat": "Дата рождения",
            "sx": "Пол",
            "bpl1": "Место рождения (1 строка)",
            "bpl2": "Место рождения (2 строка)",
            "bpl3": "Место рождения (3 строка)",
        }
        annotations = {key_mapping.get(k, k): v for k, v in annotations.items()}
        # os.remove(f"{self._temp_path}/{temp_name}.docx")

        pasp_image = pasp_image.convert("RGB")
        return pasp_image, annotations

    @staticmethod
    def _get_png(self, docx_path: str) -> Image:
        # def _get_png(self, doc: DocxTemplate) -> Image:
        """функция печати docx в Image"""

        document = Document()
        document.LoadFromFile(docx_path)

        document.JPEGQuality = 100
        # document.SaveToFile("src/templates/results/im.pdf", FileFormat.PDF)

        imageStream = document.SaveImageToStreams(0, ImageType.Bitmap)
        # Save the bitmap to PIL Image
        pasp_image = Image.open(BytesIO(imageStream.ToArray()))

        document.Close()
        os.remove(docx_path)
        return pasp_image

    @staticmethod
    def _put_photo(
        self, pasp_image: Image, photo_path: str, l: int = 465, u: int = 350, r: int = 580, d: int = 440
    ) -> Image:  # Функция добавления фотографии, точки left, up, right, down (lower)
        # def _put_photo(self, pasp_path, photo_path, ):
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

        photo = photo.rotate(90)

        pasp_image.paste(photo.resize((r - l, d - u)), (l, u))  # уменьшаем фото
        # pasp_image.save(pasp_path)

        return pasp_image

    @staticmethod
    def _clean_passport_png(self, pasp_image: Image, l=135, u=90, r=660, d=470) -> Image:
        """
        функция обрезания паспорта
        png_path - путь к файлу изображения,
        координаты по умолчанию задаются для подготовленного шаблона,
        но могут быть заданы при вызове:
        l (default = 135) - координата левой стороны вырезаемого квадрата,
        u (default = 90) - координата верхней стороны вырезаемого квадрата,
        r (default = 660) - координата правой стороны вырезаемого квадрата,
        d (default = 470) - координата нижней стороны вырезаемого квадрата,
        """

        pasp_image = pasp_image.crop((l, u, r, d))

        return pasp_image

# flake8: noqa: F405
import os
from dataclasses import asdict
from io import BytesIO
from pathlib import Path
from random import randint

from docxtpl import DocxTemplate
from PIL import Image
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

        pasp_image = pasp_image.convert("RGB")
        clean_annotations = self._get_clean_annotations(self, annotations)

        return pasp_image, clean_annotations

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
        self, pasp_image: Image, photo_path: str, left: int = 465, upper: int = 350, right: int = 580, down: int = 440
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

        photo = photo.rotate(90)

        pasp_image.paste(photo.resize((right - left, down - upper)), (left, upper))  # уменьшаем фото

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

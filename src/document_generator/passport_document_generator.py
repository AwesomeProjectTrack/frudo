# import numpy as np
import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from random import randint

from docxtpl import DocxTemplate
from PIL import Image  # , ImageDraw, ImageFont
from spire.doc import *
from spire.doc.common import *

from src.augmentations import BaseAugmentation
from src.document_data_generator.passport_data_generator import (
    PassportDocumentDataGenerator,
)
from src.document_generator import BaseDocumentGenerator
from src.output_formater.base_output_formater import BaseOutputFormater

# import os


class PassportDocumentGenerator(BaseDocumentGenerator):
    def __init__(self, template_path: Path):
        super().__init__(template_path)

    def generate(
        self,
        output_path: Path,
        output_formater: BaseOutputFormater,
        augmentation: BaseAugmentation,
        sample_index: int,  # порядковый номер для картинки в датасете
    ):
        """
        keys = np.array([ #не успел разобраться, наверное из класса перечень переменных можно вытянуть красивее
            pser,
            pnum,
            vyd1,
            vyd2,
            vyd3,
            dvyd,
            npod,
            fam1,
            fam2,
            name,
            fname,
            bdat,
            sx,
            bpl1,
            bpl2,
            bpl3,
        ])
        """
        document_data = PassportDocumentDataGenerator()
        annotations = asdict(document_data.generate())

        date = datetime.now()
        date = date.strftime("%d_%m_%Y")
        new_folder = "/ds_passports_" + date
        # path_out = output_path / new_folder #пока что вручную ниже указал папку, потом можно будет единообразно
        path_out = "src/templates/results" + new_folder
        path_photo = "src/templates/photos/"
        path_templates = "src/templates/passport/"

        if not os.path.exists(path_out):
            os.mkdir(path_out)

        templates = os.listdir(path_templates)
        photos = os.listdir(path_photo)

        templ_index = randint(0, len(templates) - 1)  # рандомный выбор шаблона
        # photo_index = randint(0, len(photos)-1) #для рандомного выбора фото
        photo_index = sample_index  # пока вручную поставлен выбор подряд

        doc = DocxTemplate(path_templates + templates[templ_index])

        # sample = datas.loc[sample_index]
        # annotations["first_name"]["value"]
        context = {anno: annotations[anno]["value"] for anno in annotations}
        doc.render(context)
        doc.save(f"{path_out}/{sample_index}.docx")

        self._print_png(f"{path_out}/{sample_index}")
        os.remove(f"{path_out}/{sample_index}.docx")

        self._clean_top_png(f"{path_out}/{sample_index}.png")
        self._clean_bottom_png(f"{path_out}/{sample_index}.png")
        self._put_photo(f"{path_out}/{sample_index}.png", path_photo + "/" + photos[photo_index])

        # sample_json = {descr: feature for descr, feature in zip(descriptions, sample)}
        # sample_json['Класс документа'] = "Паспорт"
        # sample_json['Страна'] = "Российская Федерация"
        # sample_json['Печать'] = "CV макет Test"
        json_to_file = json.dumps(annotations, indent=4, ensure_ascii=False)

        # Writing to sample.json
        with open(f"{path_out}/{sample_index}.json", "w") as outfile:
            outfile.write(json_to_file)

        # template, annotations = augmentation.apply(template, annotations)
        # output_formater.format(output_path=output_path, image=template, annotations=annotations)

    def _print_png(self, path: str):
        """функция печати docx в PNG"""

        document = Document()

        # Load a Word file
        document.LoadFromFile(path + ".docx")

        # Loop through the pages in the document
        # for i in range(document.GetPageCount()): #перебор не будем делать, печатаем только первую страницу
        # Convert a specific page to bitmap image
        imageStream = document.SaveImageToStreams(
            # i,
            0,
            ImageType.Bitmap,
        )
        # Save the bitmap to a PNG file
        with open(path + ".png", "wb") as imageFile:
            imageFile.write(imageStream.ToArray())

        document.Close()

    def _clean_top_png(self, path: str, h=60):
        """функция обрезания верха фотографии высотой h пикселей"""
        with Image.open(path) as img:
            img.load()

        img_clean = img.crop((0, h, img.width, img.height))
        img_clean.save(path)

    def _clean_bottom_png(self, path: str, h=430):
        """функция обрезания низа фотографии (ниже h пикселей)"""
        with Image.open(path) as img:
            img.load()

        img_clean = img.crop((0, 0, img.width, h))
        img_clean.save(path)

    def _put_photo(self, pasp_path, photo_path, l=465, u=290, r=580, d=380):
        """Функция добавления фотографии, точки left, up, right, down (lower)"""
        with Image.open(pasp_path) as pasp:
            pasp.load()
        with Image.open(photo_path) as photo:
            photo.load()

        photo = photo.rotate(90)

        pasp.paste(photo.resize((r - l, d - u)), (l, u))  # уменьшаем фото
        pasp.save(pasp_path)

import os
from random import randint

from dataclasses import asdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from src.document_data_generator import PassportDocumentDataGenerator
from src.document_generator import BaseDocumentGenerator


class PassportDocumentFromImageGenerator(BaseDocumentGenerator):
    def __init__(self):
        super().__init__()
        self._template_path = Path("src/templates/passport_image")
        self._font, self._font_bold = self.__get_font(self._template_path, font_size = 80)
        self._doc_type = "passport_HD"
        self._photo_path = Path("src/templates/photos/")

    def __get_font(self, template_path: Path, font_size: int = 20) -> tuple:
        font_path = template_path / "ocrb.ttf"
        font_bold_path = template_path / "ocrbbold.ttf"
        #print(font_path, font_bold_path)
        #/workspace/src/templates/passport_image/arialnarrow_bold.ttf
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
        
        """TO DO: надо бы автоматизировать от первоначального списка..
        for anno in annotations:
            print("annotations[anno]:")
            print(annotations[anno])

            draw.text(
                annotations[anno]["bboxes"],
                annotations[anno]["value"],
                font=self._font_bold,
                fill="black",
            )  
        """
        photos = os.listdir(self._photo_path)  # просмотр папки с фотографиями
        photo_index = randint(0, len(photos) - 1)  # рандомный выбор фото
        template = self._put_photo(self, template, f"{self._photo_path}/{photos[photo_index]}")

        clean_annotations = self._get_clean_annotations(self, annotations)

        return template, clean_annotations


    @staticmethod
    def _put_photo(
        self, 
        pasp_image: Image, 
        photo_path: str, 
        l: int = 220, u: int = 2590, r: int = 995, d: int = 3580
    ) -> Image:  
        # Функция добавления фотографии, точки left, up, right, down (lower)
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

        #photo = photo.rotate(90)

        pasp_image.paste(photo.resize((r - l, d - u)), (l, u))  # изменяем размер фото
        # pasp_image.save(pasp_path)

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

        # key_mapping = {
        #     "pser" : "Серия паспорта", 
        #     "pser2" : "Серия паспорта (на второй странице)", 
        #     "pnum" : "Номер паспорта", 
        #     "pnum2" : "Номер паспорта (на второй странице)", 
        #     "vyd1": "Паспорт выдан (1 строка)",
        #     "vyd2": "Паспорт выдан (2 строка)",
        #     "vyd3": "Паспорт выдан (3 строка)",
        #     "dvyd": "Дата выдачи",
        #     "npod": "Номер подразделения",
        #     "fam1": "Фамилия (1 строка)",
        #     "fam2": "Фамилия (2 строка)",
        #     "name": "Имя",
        #     "fnam": "Отчество",
        #     "bdat": "Дата рождения",
        #     "sx": "Пол",
        #     "bpl1": "Место рождения (1 строка)",
        #     "bpl2": "Место рождения (2 строка)",
        #     "bpl3": "Место рождения (3 строка)",
        # }
        # clean_annotations = {key_mapping.get(k, k): v for k, v in annotations.items()}

        full_name = annotations['fam1']['value']
        full_name = full_name + " " + annotations['fam2']['value'] if annotations['fam2']['value'] else full_name
        full_name = full_name + " " + annotations['name']['value'] + " " + annotations['fnam']['value']

        full_place = annotations['vyd1']['value']
        full_place = full_place + " " + annotations['vyd2']['value'] if annotations['vyd2']['value'] else full_place
        full_place = full_place + " " + annotations['vyd3']['value'] if annotations['vyd3']['value'] else full_place

        full_birth_place = annotations['bpl1']['value'] 
        full_birth_place = full_birth_place + " " + annotations['bpl2']['value'] if annotations['bpl2']['value'] else full_birth_place
        full_birth_place = full_birth_place + " " + annotations['bpl3']['value'] if annotations['bpl3']['value'] else full_birth_place
        
        clean_annotations = {
        'Полное имя' : {'value': full_name, 'bboxes':[0, 0]},
        'Полный номер паспорта' : {'value': annotations['pser']['value'] + " " + annotations['pnum']['value'], 'bboxes':[0, 0]},
        'Полное место выдачи' : {'value': full_place, 'bboxes':[0, 0]},
        'Полное место рождения' : {'value': full_birth_place, 'bboxes':[0, 0]},
        'Дата выдачи' : {'value':  annotations['dvyd']['value'], 'bboxes':[0, 0]},
        'Номер подразделения' : {'value':  annotations['npod']['value'], 'bboxes':[0, 0]},
        'Дата рождения' : {'value':  annotations['bdat']['value'], 'bboxes':[0, 0]},
        'Пол' : {'value':  annotations['sx']['value'], 'bboxes':[0, 0]},
        }
        return clean_annotations

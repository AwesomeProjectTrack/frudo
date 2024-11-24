import json
import uuid
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from src.data.document_type.snils_data import SnildDocumentData
from src.document.base import BaseDocument


@dataclass
class SnilsPosition:
    snils_number_position: tuple[float, float]
    family_name_position: tuple[float, float]
    name_position: tuple[float, float]
    second_name_position: tuple[float, float]
    birth_date_position: tuple[float, float]
    birth_place_position_one: tuple[float, float]
    gender_position: tuple[float, float]
    birth_place_position_two: tuple[float, float] | None
    birth_place_position_three: tuple[float, float] | None
    registration_date_position: tuple[float, float]


@dataclass
class SnilsAnnotations(SnilsPosition):
    snils_number: str
    family_name: str
    name: str
    second_name: str
    birth_date: str
    birth_place_one: str
    gender: str
    birth_place_two: str | None
    birth_place_three: str | None
    registration_date: str


class Snils(BaseDocument):
    def __init__(self, template_path: Path):
        super().__init__(template_path)
        self._font, self._font_bold = self.__get_font(template_path, 30)
        self._anno = self.__get_annotations(template_path / "data.json")

    def __get_font(self, template_path, font_size: int = 30) -> tuple:
        font_path = template_path / "arialnarrow.ttf"
        font_bold_path = template_path / "arialnarrow_bold.ttf"
        font = ImageFont.truetype(font_path, font_size)
        font_bold = ImageFont.truetype(font_bold_path, font_size)
        return font, font_bold

    def __get_annotations(self, anno_path):
        return json.loads(anno_path)

    def __get_anno_bboxes(self):
        anno = self._anno["annotations"][0]["result"]
        number_pos = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "номер"
        ]
        family_name_pos = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "фамилия"
        ]
        name_pos = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "имя"
        ]
        second_name_pos = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "отчество"
        ]
        date_birth_pos = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "дата"
        ]
        mesto_one_pos = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "место 1"
        ]
        mesto_two_pos = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "место 2"
        ]
        mesto_three_pos = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "место 3"
        ]
        sex_pos = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "пол"
        ]
        date_reg_pos = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "дата рег"
        ]

        return SnilsPosition(
            snils_number_position=number_pos[0],
            family_name_position=family_name_pos[0],
            name_position=name_pos[0],
            second_name_position=second_name_pos[0],
            birth_date_position=date_birth_pos[0],
            birth_place_position_one=mesto_one_pos[0],
            birth_place_position_two=mesto_two_pos[0],
            birth_place_position_three=mesto_three_pos[0],
            registration_date_position=date_reg_pos[0],
            gender_position=sex_pos[0],
        )

    def _get_annotations(self):
        bboxes_positions = self.__get_anno_bboxes()
        data = SnildDocumentData.generate()
        return SnilsAnnotations(
            **bboxes_positions,
            snils_number=data["snils"],
            family_name=data["last_name"],
            name=data["first_name"],
            second_name=data["second_name"],
            birth_date=data["birth_date"],
            birth_place_one=data["mesto_one"],
            gender=data["sex"],
            birth_place_two=data["mesto_two"],
            birth_place_three=data["mesto_three"],
            registration_date=data["date_reg"],
        )

    def _create(self, template_path: Path, annotations: SnilsAnnotations, output_path: Path):
        template = Image.open(template_path)
        template = template.resize((800, 600))
        draw = ImageDraw.Draw(template)
        draw.text(
            annotations.snils_number_position,
            annotations.snils_number,
            font=self._font_bold,
            fill="black",
        )  # Пример координат
        draw.text(
            annotations.family_name_position, annotations.family_name.upper(), font=self._font, fill="black"
        )  # Пример координат
        draw.text(
            annotations.name_position, annotations.name.upper(), font=self._font, fill="black"
        )  # Пример координат
        draw.text(
            annotations.second_name_position, annotations.second_name.upper(), font=self._font, fill="black"
        )  # Пример координат
        draw.text(
            annotations.birth_date_position, annotations.birth_date, font=self._font, fill="black"
        )  # Пример координат
        draw.text(
            annotations.birth_place_position_one, annotations.birth_place_one.upper(), font=self._font, fill="black"
        )
        if annotations.birth_place_position_two:
            draw.text(
                annotations.birth_place_position_two, annotations.birth_place_two.upper(), font=self._font, fill="black"
            )
        if annotations.birth_place_position_three:
            draw.text(
                annotations.birth_place_position_three,
                annotations.birth_place_three.upper(),
                font=self._font,
                fill="black",
            )
        draw.text(annotations.gender_position, annotations.gender, font=self._font, fill="black")
        draw.text(annotations.registration_date_position, annotations.registration_date, font=self._font, fill="black")
        template.save(output_path / f"snils_{uuid.uuid4()}.png")

    def create(self, output_path: Path, amount: int = 100):
        annotations = self._get_annotations()
        for _ in range(amount):
            self._create(
                template_path=self._template_path / "template.jpg",
                annotations=annotations,
                output_path=output_path,
            )

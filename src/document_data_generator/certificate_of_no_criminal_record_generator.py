import json
from dataclasses import asdict

from src.data_generator import (
    DateGenerator,
    FullNameGenerator,
    Gender,
    GeoPlace,
)
from typing import Any
from src.document_data_generator.base_document_data_generator import (
    BaseDocumentDataGenerator,
)
from src.document_data_generator.dataclasses import Entity


class CertificateOfNoCriminalRecordGenerator(BaseDocumentDataGenerator):
    @staticmethod
    def generate() -> Any :
        """Для Снилс нужны ФИО, место регистрации, дата рождения, дата регистрации"""
        gender = Gender.generate()
        name = FullNameGenerator.generate(gender)
        name = f"{name.first_name} {name.first_name} {name.middle_name}"
        place = GeoPlace.generate()
        birth_date = DateGenerator.generate()

        with open("src/templates/certificate_of_no_criminal_record/data.json", "r") as file:
            anno = json.load(file)
        anno = anno["annotations"][0]["result"]

        name = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "fio"
        ]

        date_birth_pos = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "birth_date"
        ]
        birth_place = [
            [ann["value"]["x"] / 100 * ann["original_width"], ann["value"]["y"] / 100 * ann["original_height"]]
            for ann in anno
            if ann["value"].get("text") and ann["value"]["text"][0] == "birth_place"
        ]




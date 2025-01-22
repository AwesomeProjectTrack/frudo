import json

from src.data_generator import (
    DateGenerator,
    FullNameGenerator,
    Gender,
    GeoPlace,
    SnilsNumber,
)
from src.document_data_generator.base_document_data_generator import (
    BaseDocumentDataGenerator,
)
from src.document_data_generator.dataclasses import Entity, SnilsData


class SnilsDocumentDataGenerator(BaseDocumentDataGenerator):
    
    """Class Generator Russian Individual Insurance Account Number (SNILS)."""
    
    @staticmethod
    def generate() -> SnilsData:
        
        """Generator method, returns an object of SnilsData class, 
        which contains fields with the following information: 
        last name, middle name,
        first name, region of birth, 
        city of birth, date of birth,
        date of registration, gender, 
        snils number"""
        
        gender = Gender.generate()
        name = FullNameGenerator.generate(gender)
        place = GeoPlace.generate()
        birth_date = DateGenerator.generate()
        birth_date = birth_date.strftime("%d %B %Y года")
        registration_date = DateGenerator.generate()
        registration_date = registration_date.strftime("%d %B %Y года")

        snils_number = SnilsNumber.generate()

        with open("src/templates/snils/data.json", "r", encoding="utf-8") as file:
            anno = json.load(file)
        anno = anno["annotations"][0]["result"]

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

        return SnilsData(
            family_name=Entity(value=name.last_name, bboxes=family_name_pos[0]),
            middle_name=Entity(value=name.middle_name, bboxes=second_name_pos[0]),
            first_name=Entity(value=name.first_name, bboxes=name_pos[0]),
            region=Entity(place.region, bboxes=mesto_two_pos[0]),
            city=Entity(place.city, bboxes=mesto_one_pos[0]),
            birth_date=Entity(birth_date, bboxes=date_birth_pos[0]),
            reg_date=Entity(registration_date, bboxes=date_reg_pos[0]),
            gender=Entity(gender, bboxes=sex_pos[0]),
            snils_number=Entity(snils_number, bboxes=number_pos[0]),
        )

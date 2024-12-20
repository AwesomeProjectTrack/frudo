import json
from pathlib import Path

from src.data_generator import (
    BboxTins,
    DateGenerator,
    FullNameGenerator,
    Gender,
    GeoPlace,
    StartCoords,
    TinsNumber,
)
from src.document_data_generator.base_document_data_generator import (
    BaseDocumentDataGenerator,
)
from src.document_data_generator.dataclasses import Entity, OldTinsData


class OldTinsDocumentDataGenerator(BaseDocumentDataGenerator):
    @staticmethod
    def generate() -> OldTinsData:
        gender = Gender.generate()
        short_gender = gender[:3] + "."
        name = FullNameGenerator.generate(gender)
        full_name = name.last_name + " " + name.first_name + " " + name.middle_name
        place = GeoPlace.generate()
        full_place = place.region + " " + place.city
        birth_date = DateGenerator.generate()
        birth_date = birth_date.strftime("%d %B %Y г.")
        registration_date = DateGenerator.generate()
        registration_date = registration_date.strftime("%d %B %Y г.")

        tins_number = TinsNumber.generate()

        annotations_path = Path("src/templates/tins/data.json")

        with open(annotations_path) as file:
            anno = json.load(file)

        start_coords_old = StartCoords.generate(
            width=anno["old"]["width"], height=anno["old"]["heigth"], is_new_tins=False
        )

        anno["old"]["name"]["value"] = full_name
        anno["old"]["name"]["x"] = start_coords_old["name"][0]
        anno["old"]["name"]["y"] = start_coords_old["name"][1]
        anno["old"]["name"]["bbox"] = BboxTins().generate(
            text=full_name, old_coords=[anno["old"]["name"]["x"], anno["old"]["name"]["y"]], is_new_tin=False
        )

        anno["old"]["birth_date"]["value"] = birth_date
        anno["old"]["birth_date"]["x"] = start_coords_old["birth_date"][0]
        anno["old"]["birth_date"]["y"] = start_coords_old["birth_date"][1]
        anno["old"]["birth_date"]["bbox"] = BboxTins().generate(
            text=birth_date,
            old_coords=[anno["old"]["birth_date"]["x"], anno["old"]["birth_date"]["y"]],
            is_new_tin=False,
        )

        anno["old"]["sex"]["value"] = short_gender
        anno["old"]["sex"]["x"] = start_coords_old["sex"][0]
        anno["old"]["sex"]["y"] = start_coords_old["sex"][1]
        anno["old"]["sex"]["bbox"] = BboxTins().generate(
            text=gender, old_coords=[anno["old"]["sex"]["x"], anno["old"]["sex"]["y"]], is_new_tin=False
        )

        anno["old"]["place_of_birth"]["value"] = full_place
        anno["old"]["place_of_birth"]["x"] = start_coords_old["place_of_birth"][0]
        anno["old"]["place_of_birth"]["y"] = start_coords_old["place_of_birth"][1]
        anno["old"]["place_of_birth"]["bbox"] = BboxTins().generate(
            text=full_place,
            old_coords=[anno["old"]["place_of_birth"]["x"], anno["old"]["place_of_birth"]["y"]],
            is_new_tin=False,
        )

        anno["old"]["issued"]["value"] = registration_date
        anno["old"]["issued"]["x"] = start_coords_old["issued"][0]
        anno["old"]["issued"]["y"] = start_coords_old["issued"][1]
        anno["old"]["issued"]["bbox"] = BboxTins().generate(
            text=registration_date,
            old_coords=[anno["old"]["issued"]["x"], anno["old"]["issued"]["y"]],
            is_new_tin=False,
        )

        anno["old"]["tin"]["value"] = tins_number
        anno["old"]["tin"]["x"] = start_coords_old["tin"][0]
        anno["old"]["tin"]["y"] = start_coords_old["tin"][1]
        anno["old"]["tin"]["bbox"] = BboxTins().generate(
            text=tins_number, old_coords=[anno["old"]["tin"]["x"], anno["old"]["tin"]["y"]], is_new_tin=False
        )

        return OldTinsData(
            tins_number=Entity(value=tins_number, bboxes=anno["old"]["tin"]["bbox"]),
            family_name=Entity(value=name.last_name, bboxes=anno["old"]["name"]["bbox"]),
            middle_name=Entity(value=name.middle_name, bboxes=anno["old"]["name"]["bbox"]),
            first_name=Entity(value=name.first_name, bboxes=anno["old"]["name"]["bbox"]),
            name=Entity(value=full_name, bboxes=anno["old"]["name"]["bbox"]),
            birth_date=Entity(value=birth_date, bboxes=anno["old"]["birth_date"]["bbox"]),
            reg_date=Entity(value=registration_date, bboxes=anno["old"]["issued"]["bbox"]),
            city=Entity(value=place, bboxes=anno["old"]["place_of_birth"]["bbox"]),
            region=Entity(place.region, bboxes=anno["old"]["place_of_birth"]["bbox"]),
            full_place=Entity(value=full_place, bboxes=anno["old"]["place_of_birth"]["bbox"]),
            gender=Entity(value=short_gender, bboxes=anno["old"]["sex"]["bbox"]),
        )

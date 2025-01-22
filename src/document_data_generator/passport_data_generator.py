import json
from datetime import datetime

from src.data_generator import (
    DateGenerator,
    DateVydPasspGenerator,
    FullNameFromFileGenerator,
    GeoPlaceFromFile,
    PassportNumber,
    PodrazdelenieNumber,
)
from src.document_data_generator.base_document_data_generator import (
    BaseDocumentDataGenerator,
)
from src.document_data_generator.dataclasses import Entity, PassportData


class PassportDocumentDataGenerator(BaseDocumentDataGenerator):
    
    """Class passport generator."""
    
    @staticmethod
    def generate() -> PassportData:
        
        """
        The following attributes are set for the passport:
        keys_descr = {
            “pser” : ‘Passport series’.
            “pser2” : ‘Passport series’, on the second page.
            “pnum” : ‘Passport number’.
            “pnum2” : ‘Passport number’, on the second page.
            “vyd1” : “Passport issued (line 1).”
            “vyd2” : ”Passport issued (line 2).”
            “vyd3” : “Passport issued (line 3).”
            “dvyd” : ‘Date of issue’,
            “npod” : ‘Unit number’,
            “fam1” : “Surname (line 1)”,
            “fam2” : ‘Surname (line 2)’,
            “name” : ‘First name’,
            “fnam” : ‘patronymic’,
            “bdat” : ‘Date of birth’,
            “sx” : ‘Gender’,
            “bpl1” : “Place of birth (1 line)”,
            “bpl2” : ‘Place of birth (line 2)’,
            “bpl3” : “Place of birth (3rd line)”
        }

        Parameters
        ----------

        Returns
        -------

        """
        # gender = Gender.generate()
        name = FullNameFromFileGenerator.generate()
        vyd_place = GeoPlaceFromFile.generate()
        b_place = GeoPlaceFromFile.generate()
        pass_number = PassportNumber.generate()

        birth_date = DateGenerator.generate(end_date=datetime(2010, 1, 1))
        birth_date_str = birth_date.strftime("%d.%m.%Y")
        vyd_date = DateVydPasspGenerator.generate(birth_date=birth_date)
        vyd_date_str = vyd_date.strftime("%d.%m.%Y")
        nomer_podr = PodrazdelenieNumber.generate()
        sx = "муж." if name.gender == "М" else "жен."

        with open("src/templates/passport_image/passpHD.json", "r", encoding="utf-8") as file:
            anno = json.load(file)

        anno = anno["annotations"]

        pser_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "pser"]

        pser2_pos = [
            [ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "pser2"
        ]

        pnum_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "pnum"]

        pnum2_pos = [
            [ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "pnum2"
        ]

        vyd1_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "vyd1"]

        vyd2_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "vyd2"]

        vyd3_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "vyd3"]

        dvyd_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "dvyd"]

        npod_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "npod"]

        fam1_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "fam1"]

        fam2_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "fam1"]

        name_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "name"]

        fnam_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "fnam"]

        bdat_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "bdat"]

        sx_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "sx"]

        bpl1_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "bpl1"]

        bpl2_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "bpl2"]

        bpl3_pos = [[ann["x1"] + (ann["x2"] - ann["x1"]) / 2, ann["y2"] - 20] for ann in anno if ann["name"] == "bpl3"]

        return PassportData(
            pser=Entity(value=pass_number.pser, bboxes=pser_pos[0]),
            pser2=Entity(value=pass_number.pser, bboxes=pser2_pos[0]),
            pnum=Entity(value=pass_number.pnum, bboxes=pnum_pos[0]),
            pnum2=Entity(value=pass_number.pnum, bboxes=pnum2_pos[0]),
            vyd1=Entity(value="Управление МВД России", bboxes=vyd1_pos[0]),
            vyd2=Entity(value="по г. " + vyd_place.city, bboxes=vyd2_pos[0]),
            vyd3=Entity(value=vyd_place.region, bboxes=vyd3_pos[0]),
            dvyd=Entity(value=vyd_date_str, bboxes=dvyd_pos[0]),
            npod=Entity(value=nomer_podr, bboxes=npod_pos[0]),
            fam1=Entity(value=name.last_name, bboxes=fam1_pos[0]),
            fam2=Entity(value="", bboxes=fam2_pos[0]),
            name=Entity(value=name.first_name, bboxes=name_pos[0]),
            fnam=Entity(value=name.middle_name, bboxes=fnam_pos[0]),
            bdat=Entity(value=birth_date_str, bboxes=bdat_pos[0]),
            sx=Entity(value=sx, bboxes=sx_pos[0]),
            bpl1=Entity(value="г. " + b_place.city, bboxes=bpl1_pos[0]),
            bpl2=Entity(value=b_place.region, bboxes=bpl2_pos[0]),
            bpl3=Entity(value="", bboxes=bpl3_pos[0]),
        )

# import json
# import numpy as np

from win32ctypes.pywin32.pywintypes import datetime

from src.data_generator import (  # FullNameGenerator,; Gender,; GeoPlace,; SnilsNumber,
    DateGenerator,
    DateVydPasspGenerator,
    FullNameFromFileGenerator,
    GeoPlaceFromFile,
    PassportNumber,
    PodrNumber,
)
from src.document_data_generator.base_document_data_generator import (
    BaseDocumentDataGenerator,
)
from src.document_data_generator.dataclasses import Entity, PassportData


class PassportDocumentDataGenerator(BaseDocumentDataGenerator):
    @staticmethod
    def generate() -> PassportData:
        """Для паспорта нужны:
        keys_descr = np.array([
            ['PSER', 'Серия паспорта'],
            ['PNUM', 'Номер паспорта'],
            ['VYD1', 'Паспорт выдан (1 строка)'],
            ['VYD2', 'Паспорт выдан (2 строка)'],
            ['VYD3', 'Паспорт выдан (3 строка)'],
            ['DVYD', 'Дата выдачи'],
            ['NPOD', 'Номер подразделения'],
            ['FAM1', 'Фамилия (1 строка)'],
            ['FAM2', 'Фамилия (2 строка)'],
            ['NAME', 'Имя'],
            ['FNAM', 'Отчество'],
            ['BDAT', 'Дата рождения'],
            ['SX', 'Пол'],
            ['BPL1', 'Место рождения (1 строка)'],
            ['BPL2', 'Место рождения (2 строка)'],
            ['BPL3', 'Место рождения (3 строка)']
        ])
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
        nomer_podr = PodrNumber.generate()
        sx = "муж." if name.gender == "М" else "жен."

        return PassportData(
            pser=Entity(value=pass_number.pser, bboxes=[0, 0]),
            pnum=Entity(value=pass_number.pnum, bboxes=[0, 0]),
            vyd1=Entity(value="Управление МВД России", bboxes=[0, 0]),
            vyd2=Entity(value="по г. " + vyd_place.city + ", ", bboxes=[0, 0]),
            vyd3=Entity(value=vyd_place.region, bboxes=[0, 0]),
            dvyd=Entity(value=vyd_date_str, bboxes=[0, 0]),
            npod=Entity(value=nomer_podr, bboxes=[0, 0]),
            fam1=Entity(value=name.last_name, bboxes=[0, 0]),
            fam2=Entity(value="", bboxes=[0, 0]),
            name=Entity(value=name.first_name, bboxes=[0, 0]),
            fnam=Entity(value=name.middle_name, bboxes=[0, 0]),
            bdat=Entity(value=birth_date_str, bboxes=[0, 0]),
            sx=Entity(value=sx, bboxes=[0, 0]),
            bpl1=Entity(value="г. " + b_place.city + ",", bboxes=[0, 0]),
            bpl2=Entity(value=b_place.region, bboxes=[0, 0]),
            bpl3=Entity(value="", bboxes=[0, 0]),
        )

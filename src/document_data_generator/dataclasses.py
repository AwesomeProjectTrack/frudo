""" Dataclasses for Document Data after generation"""
from dataclasses import dataclass

from src.data_generator import (
    InvoiceCompanyData,
    InvoiceDateTimeData,
    InvoiceFinancialData,
    InvoiceItemData,
)


@dataclass
class Entity:
    """Structure of each Entity"""

    value: str
    bboxes: list[int | float]


@dataclass
class SnilsData:
    """Snils Data Structure"""

    snils_number: Entity
    family_name: Entity
    middle_name: Entity
    first_name: Entity
    birth_date: Entity
    reg_date: Entity
    city: Entity
    region: Entity
    gender: Entity


@dataclass
class PassportData:
    """ """
    pser: Entity
    pnum: Entity
    pser2: Entity  # для картинки нужны разные поля (bbox)
    pnum2: Entity  # для разных страниц
    vyd1: Entity
    vyd2: Entity
    vyd3: Entity
    dvyd: Entity
    npod: Entity
    fam1: Entity
    fam2: Entity
    name: Entity
    fnam: Entity
    bdat: Entity
    sx: Entity
    bpl1: Entity
    bpl2: Entity
    bpl3: Entity

    keys_descr = {
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

    def set_bboxes(self, key: Entity, bbx: list):
        """
        

        Parameters
        ----------
        key: Entity :
            
        bbx: list :
            

        Returns
        -------

        """
        self.key["bboxes"] = bbx


class InvoiceData:
    """Invoice Data Structure"""

    saler: InvoiceCompanyData
    buyer: InvoiceCompanyData
    items: list[InvoiceItemData]
    datatime: InvoiceDateTimeData
    financial: InvoiceFinancialData


@dataclass
class NewTinsData:
    """Tins Data Structure for new version of tins"""

    tins_number: Entity
    family_name: Entity
    middle_name: Entity
    first_name: Entity
    name: Entity
    birth_date: Entity
    reg_date: Entity
    city: Entity
    region: Entity
    gender: Entity
    full_place: Entity


@dataclass
class OldTinsData:
    """Tins Data Structure for old version of tins"""

    tins_number: Entity
    family_name: Entity
    middle_name: Entity
    first_name: Entity
    name: Entity
    birth_date: Entity
    reg_date: Entity
    city: Entity
    region: Entity
    gender: Entity
    full_place: Entity

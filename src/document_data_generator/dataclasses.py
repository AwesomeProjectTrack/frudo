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
    pser: Entity
    pnum: Entity
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


"""
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
    ['SX',   'Пол'],
    ['BPL1', 'Место рождения (1 строка)'],
    ['BPL2', 'Место рождения (2 строка)'],
    ['BPL3', 'Место рождения (3 строка)']
"""


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

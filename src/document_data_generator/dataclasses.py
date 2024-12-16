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
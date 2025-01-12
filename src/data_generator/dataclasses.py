from dataclasses import dataclass


@dataclass
class Entity:
    """Structure of each Entity"""

    value: str
    bboxes: list[int | float]


@dataclass
class FullNameDataclass:
    last_name: str
    middle_name: str
    first_name: str
    gender: str  # добавил пол в класс для единообразия


@dataclass
class GeoPlaceDataclass:
    city: str
    region: str


@dataclass
class FullPassportNumber:
    pser: str
    pnum: str


@dataclass
class InvoiceDateTimeData:
    """InvoiceDateTimeData"""

    N: Entity
    day: Entity
    month: Entity
    year: Entity


@dataclass
class InvoiceCompanyData:
    """InvoiceCompanyData"""

    name: Entity
    address: Entity
    iin_kpp: Entity


@dataclass
class InvoiceItemData:
    """InvoiceItemData"""

    item_name: Entity
    iq: Entity  # Количество товара
    io: Entity  # Цена за единицу
    inetcost: Entity  # Суммарная стоимость без налога
    inc: Entity  # Сумма налога
    igen_cost: Entity  # Итоговая стоимость (себестоимость + налог)


@dataclass
class InvoiceFinancialData:
    """InvoiceItemData"""

    ncs: Entity  # Общая сумма налога
    netsum: Entity  # Общая себестоимость товаров
    gen_cost: Entity  # Общая стоимость (себестоимость + налог)

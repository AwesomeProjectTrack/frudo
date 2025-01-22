from dataclasses import dataclass


@dataclass
class FullNameDataclass:
    """ """
    last_name: str
    middle_name: str
    first_name: str
    gender: str  # добавил пол в класс для единообразия


@dataclass
class GeoPlaceDataclass:
    """ """
    city: str
    region: str


@dataclass
class FullPassportNumber:
    """ """
    pser: str
    pnum: str


@dataclass
class InvoiceDateTimeData:
    """InvoiceDateTimeData"""

    N: int
    day: int
    month: int
    year: int


@dataclass
class InvoiceCompanyData:
    """InvoiceCompanyData"""

    name: int
    address: int
    iin_kpp: int


@dataclass
class InvoiceItemData:
    """InvoiceItemData"""

    item_name: str
    iq: float  # Количество товара
    io: float  # Цена за единицу
    inetcost: float  # Суммарная стоимость без налога
    inc: float  # Сумма налога
    igen_cost: float  # Итоговая стоимость (себестоимость + налог)


@dataclass
class InvoiceFinancialData:
    """InvoiceItemData"""

    ncs: float  # Общая сумма налога
    netsum: float  # Общая себестоимость товаров
    gen_cost: float  # Общая стоимость (себестоимость + налог)

""" Data Generators for Invoices """
from random import randint

from faker import Faker

from src.data_generator.base_data_generator import BaseDataGenerator
from src.data_generator.dataclasses import (
    InvoiceCompanyData,
    InvoiceDateTimeData,
    InvoiceItemData,
)

fake = Faker("ru_RU")


class InvoiceDataTimeGenerator(BaseDataGenerator):
    """Generate DateTime data for Invoices"""

    @staticmethod
    def generate() -> InvoiceDateTimeData:
        """generate method"""
        months = {
            1: "января",
            2: "февраля",
            3: "марта",
            4: "апреля",
            5: "мая",
            6: "июня",
            7: "июля",
            8: "августа",
            9: "сентября",
            10: "октября",
            11: "ноября",
            12: "декабря",
        }
        return InvoiceDateTimeData(
            N=randint(0, 100), day=randint(1, 30), month=months[randint(1, 12)], year=randint(2010, 2025)
        )


class InvoiceCompanyGenerator(BaseDataGenerator):
    """Generate DateTime data for Invoices"""

    @staticmethod
    def generate() -> InvoiceCompanyData:
        """generate method"""
        address = str(randint(100000, 199999)) + "," + fake.city() + "," + fake.street_address()
        iin_kpp = fake.individuals_inn() + "/" + fake.kpp()
        return InvoiceCompanyData(name=fake.company(), address=address, iin_kpp=iin_kpp)


class InvoiceItemGenerator(BaseDataGenerator):
    """Generate DateTime data for Invoices"""

    @staticmethod
    def generate() -> InvoiceItemData:
        iq = randint(1, 5)  # quantity
        io = randint(1000, 9999)  # Цена за единицу
        inetcost = round(iq * io)  # Стоимость товаров
        inc = round(inetcost * 0.18)  # Сумма налога
        igen_cost = inetcost + inc  # Итоговая стоиость
        return InvoiceItemData(
            item_name=fake.text(max_nb_chars=25), iq=iq, io=io, inetcost=inetcost, inc=inc, igen_cost=igen_cost
        )

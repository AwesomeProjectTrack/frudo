""" Data Generators for Invoices """
from random import randint

from faker import Faker

from src.data_generator.base_data_generator import BaseDataGenerator
from src.data_generator.dataclasses import (
    Entity,
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
            N=Entity(value=str(randint(0, 100)), bboxes=[0, 0, 0, 0]),
            day=Entity(value=str(randint(1, 30)), bboxes=[0, 0, 0, 0]),
            month=Entity(value=months[randint(1, 12)], bboxes=[0, 0, 0, 0]),
            year=Entity(value=str(randint(2010, 2025)), bboxes=[0, 0, 0, 0]),
        )


class InvoiceCompanyGenerator(BaseDataGenerator):
    """Generate DateTime data for Invoices"""

    @staticmethod
    def generate() -> InvoiceCompanyData:
        """generate method"""
        address = str(randint(100000, 199999)) + "," + fake.city() + "," + fake.street_address()
        iin_kpp = fake.individuals_inn() + "/" + fake.kpp()
        return InvoiceCompanyData(
            name=Entity(value=fake.company(), bboxes=[0, 0, 0, 0]),
            address=Entity(value=address, bboxes=[0, 0, 0, 0]),
            iin_kpp=Entity(value=iin_kpp, bboxes=[0, 0, 0, 0]),
        )


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
            item_name=Entity(value=fake.text(max_nb_chars=25), bboxes=[0, 0, 0, 0]),
            iq=Entity(value=str(iq), bboxes=[0, 0, 0, 0]),
            io=Entity(value=str(io), bboxes=[0, 0, 0, 0]),
            inetcost=Entity(value=str(inetcost), bboxes=[0, 0, 0, 0]),
            inc=Entity(value=str(inc), bboxes=[0, 0, 0, 0]),
            igen_cost=Entity(value=str(igen_cost), bboxes=[0, 0, 0, 0]),
        )

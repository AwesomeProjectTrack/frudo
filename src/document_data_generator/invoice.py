""" Generator for Invoices """
from random import randint

from src.data_generator import (
    InvoiceCompanyGenerator,
    InvoiceDataTimeGenerator,
    InvoiceItemGenerator,
)
from src.document_data_generator.base_document_data_generator import (
    BaseDocumentDataGenerator,
)
from src.document_data_generator.dataclasses import InvoiceData, InvoiceFinancialData


class InvoiceDocumentDataGenerator(BaseDocumentDataGenerator):
    """SnilsDocumentDataGenerator"""

    @staticmethod
    def generate() -> InvoiceData:
        
        """The method that generates an invoice returns an object of the 
        InvoiceData class that contains the fields: 
        seller, buyer, item, date and time as a single field and 
        an object of the InvoiceFinancialData class."""
        
        saler = InvoiceCompanyGenerator().generate()
        buyer = InvoiceCompanyGenerator().generate()
        datetime = InvoiceDataTimeGenerator.generate()
        items_quantity = randint(1, 3)
        items = [InvoiceItemGenerator().generate() for _ in range(items_quantity)]
        ncs = 0
        netsum = 0
        gen_cost = 0
        for item in items:
            ncs += item.inc
            netsum += item.inetcost
            gen_cost += item.igen_cost
        return InvoiceData(
            saler=saler,
            buyer=buyer,
            items=items,
            datatime=datetime,
            financial=InvoiceFinancialData(ncs=ncs, netsum=netsum, gen_cost=gen_cost),
        )

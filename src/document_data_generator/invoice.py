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
from src.document_data_generator.dataclasses import (
    Entity,
    InvoiceData,
    InvoiceFinancialData,
)


class InvoiceDocumentDataGenerator(BaseDocumentDataGenerator):
    """SnilsDocumentDataGenerator"""

    @staticmethod
    def generate() -> InvoiceData:
        seller = InvoiceCompanyGenerator().generate()
        buyer = InvoiceCompanyGenerator().generate()
        datetime = InvoiceDataTimeGenerator.generate()
        items_quantity = randint(1, 3)
        items = [InvoiceItemGenerator().generate() for _ in range(items_quantity)]
        ncs = 0
        netsum = 0
        gen_cost = 0
        for item in items:
            ncs += float(item.inc.value)
            netsum += float(item.inetcost.value)
            gen_cost += float(item.igen_cost.value)
        return InvoiceData(
            seller=seller,
            buyer=buyer,
            items=items,
            datetime=datetime,
            financial=InvoiceFinancialData(
                ncs=Entity(value=str(ncs), bboxes=[0, 0, 0, 0]),
                netsum=Entity(value=str(netsum), bboxes=[0, 0, 0, 0]),
                gen_cost=Entity(value=str(gen_cost), bboxes=[0, 0, 0, 0]),
            ),
        )

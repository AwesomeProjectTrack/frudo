from dataclasses import asdict

from src.document_data_generator.invoice import InvoiceDocumentDataGenerator

invoice = InvoiceDocumentDataGenerator().generate()
asdict(invoice)

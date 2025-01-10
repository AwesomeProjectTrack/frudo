from docxtpl import DocxTemplate
from faker import Faker
from src.data_generator.geo_place import GeoPlace
import random
from PIL import Image
import datetime
from io import BytesIO
from spire.doc import *
from reportlab.pdfbase import pdfmetrics
from spire.doc.common import *


# Создаем объект Faker для генерации случайных данных

fake = Faker("ru_RU")

def generate_contract_number():
    # Получаем текущую дату в формате ГГГГММДД
    today = datetime.date.today().strftime("%Y%m%d")
    
    # Генерируем случайный код (например, из 6 цифр)
    random_code = random.randint(100000, 999999)
    
    # Собираем номер договора
    contract_number = f"CON-{today}-{random_code}"
    
    return contract_number

# Генерация синтетических документов
def generate_documents(template_path, num_docs, output_dir):
    for i in range(num_docs):
        # Генерация случайных данных
        context = {
            "org_name": fake.large_company(),
            "org_reason": random.choice(['устава компании', 'договоренности', 'решения учредителей', 'договора', 'протокола собрания']),
            "ip_name": " ".join(fake.passport_owner()),
            "orgnip": fake.individuals_ogrn(),
            "money": round(random.uniform(0, 600000), 2),
            "date": fake.date(),
            "debt_money": round(random.uniform(0, 600000), 2),
            "org_address": fake.address(),
            "org_ogrn": fake.businesses_ogrn(),
            "org_tins": fake.businesses_inn(),
            "org_kpp": fake.kpp(),
            "org_current_account": fake.checking_account(),
            "org_bank_name": fake.bank(),
            "org_correspondent_account_number": fake.correspondent_account(),
            "org_bik": fake.bic(),
            "ip_passport": fake.passport_number(),
            "ip_passport_place":  f"Управление МВД России по г. {fake.city_name()}, {fake.region()}",
            "ip_address": fake.address(),
            "ip_tins": fake.individuals_inn(),
            "ip_ogrnip": fake.individuals_ogrn(),
            "ip_current_account": fake.checking_account(),
            "ip_bank_name": fake.bank(),
            "ip_correspondent_account_number": fake.correspondent_account(),
            "ip_bik": fake.bic(),
            "contract_number": generate_contract_number()
        }
        # Загружаем шаблон DOCX
        doc = DocxTemplate(template_path)
        # Заменяем метки на данные
        doc.render(context)
        # Сохраняем новый документ
        output_path = f"{output_dir}/generated_doc_{i+1}.docx"
        doc.save(output_path)
        print(f"Документ {i+1} сохранен: {output_path}")


# Параметры
template_path = "test.docx"  # Путь к вашему шаблону
num_docs = 1  # Количество документов
output_dir = "generated_docs"  # Папка для сохранения
from pathlib import Path
# Генерация документов
generate_documents(template_path, num_docs, output_dir)


import aspose.words as aw

# load document
doc = aw.Document("generated_docs/generated_doc_1.docx")

# set output image format
options = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)

# loop through pages and convert them to PNG images
for pageNumber in range(doc.page_count):
    options.page_set = aw.saving.PageSet(pageNumber)
    doc.save(str(pageNumber+1)+"_page.png", options)



# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from pdf2image import convert_from_path
# from reportlab.pdfgen import canvas
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.lib.pagesizes import letter
# import os

# import pypandoc
# def docx_to_pdf(docx_file, pdf_file):
# #     from docx import Document
    
# #     # Подключаем шрифт, который поддерживает кириллицу
# #     pdfmetrics.registerFont(TTFont('Arial', 'Arial/arial.ttf'))  # Укажите путь к шрифту, если он не установлен системно

# #     # Открываем .docx файл
# #     doc = Document(docx_file)
# #     lines = [paragraph.text for paragraph in doc.paragraphs]
    
# #     # Создаем PDF файл
# #     c = canvas.Canvas(pdf_file, pagesize=letter)
# #     width, height = letter
# #     margin = 50
# #     y = height - margin

# #     c.setFont("Arial", 10)  # Используем зарегистрированный шрифт Arial
    
# #     for line in lines:
# #         if y < margin:  # Добавляем новую страницу, если места не хватает
# #             c.showPage()
# #             c.setFont("Arial", 10)
# #             y = height - margin
# #         c.drawString(margin, y, line)
# #         y -= 15  # Интервал между строками

# #     c.save()

#     # Конвертируем docx в PDF с помощью pypandoc
#     output = pypandoc.convert_file(docx_file, 'pdf', outputfile=pdf_file, extra_args=['-V', "mainfont='Arial/arial.ttf'"])
#     return output

# def pdf_to_images(pdf_file, output_folder):
#     """
#     Convert a .pdf file to images using pdf2image.
#     """
#     images = convert_from_path(pdf_file)
#     image_files = []
#     for i, image in enumerate(images):
#         image_file = os.path.join(output_folder, f"page_{i + 1}.png")
#         image.save(image_file, "PNG")


# for filename in Path(output_dir).iterdir():
#     pdf_output = filename.stem + '.pdf'
#     docx_to_pdf(str(filename), pdf_output)
#     image_folder = filename.stem
#     if not os.path.exists(image_folder):
#         os.makedirs(image_folder)
#     image_files = pdf_to_images(pdf_output, image_folder)
#     print(f"Converted {pdf_output} to images:")


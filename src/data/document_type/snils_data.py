import random

from src.data.data_type.snils import SnilsNumber
from src.data.document_type.base import BaseDocumentData


class SnildDocumentData(BaseDocumentData):
    def generate():
        first_names = ["Иван", "Петр", "Алексей", "Мария", "Елена"]
        last_names = ["Иванов", "Петров", "Сидоров", "Кузнецова", "Попова"]
        middle_names = ["Иванович", "Петрович", "Алексеевич", "Сергеевна", "Викторовна"]
        mesto_one = "Щукино"
        mesto_two = "Ашинский"
        mesto_three = "Челябинская область"
        sex = "женский"
        birth_date = f"{random.randint(1, 28):02}.{random.randint(1, 12):02}.{random.randint(1950, 2020)}"
        date_reg = f"{random.randint(1, 28):02}.{random.randint(1, 12):02}.{random.randint(1996, 2020)}"
        return {
            "last_name": random.choice(last_names),
            "first_name": random.choice(first_names),
            "second_name": random.choice(middle_names),
            "birth_date": birth_date,
            "snils": SnilsNumber.generate(),
            "date_reg": date_reg,
            "sex": sex,
            "mesto_one": mesto_one,
            "mesto_two": mesto_two,
            "mesto_three": mesto_three,
        }

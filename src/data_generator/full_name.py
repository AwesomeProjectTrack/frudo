from typing import Any

from faker import Faker

from src.data_generator.base_data_generator import BaseDataGenerator
from src.data_generator.dataclasses import FullNameDataclass

fake = Faker("ru_RU")


class FullNameGenerator(BaseDataGenerator):
    @staticmethod
    def generate(gender: str = "мужской") -> Any:
        match gender:
            case "женский":
                first_name = fake.first_name_female()
                last_name = fake.last_name_female()
                middle_name = fake.middle_name_female()
            case "мужской":
                first_name = fake.first_name_male()
                last_name = fake.last_name_male()
                middle_name = fake.middle_name_male()
            case _:
                raise ValueError("Невозможно сгенерировать данные")

        return FullNameDataclass(last_name=last_name, middle_name=middle_name, first_name=first_name)

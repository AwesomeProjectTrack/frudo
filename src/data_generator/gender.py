import random

from src.data_generator.base_data_generator import BaseDataGenerator


class Gender(BaseDataGenerator):
    """ """
    @staticmethod
    def generate() -> str:
        """ """
        gender = random.choice(["женский", "мужской"])
        return gender

import random

from src.data_generator.base_data_generator import BaseDataGenerator


class SnilsNumber(BaseDataGenerator):
    """ """
    @staticmethod
    def generate() -> str:
        """ """
        snils = [random.randint(0, 9) for _ in range(9)]
        control_sum = sum((9 - i) * num for i, num in enumerate(snils)) % 101
        if control_sum == 100:
            control_sum = 0
        snils_number = f"{snils[0]:03}-{snils[1]:03}-{snils[2]:03} {control_sum:02}"
        return snils_number

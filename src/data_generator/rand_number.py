import random

from src.data_generator.base_data_generator import BaseDataGenerator


class RandomNumber(BaseDataGenerator):
    @staticmethod
    def generate(n=4) -> str:
        first_n = str(random.randint(1, 9))  # первая цифра не ноль
        number = [str(random.randint(0, 9)) for _ in range(n - 1)]  # случайные остальные цифры
        str_number = f"{first_n}{" ".join(number)}"  # кодовыправители тут сами вставляют пробел между кавычками :(

        return str_number

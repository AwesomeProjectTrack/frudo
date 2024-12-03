from src.data_generator.base_data_generator import BaseDataGenerator
from src.data_generator.rand_number import RandomNumber


class PodrNumber(BaseDataGenerator):
    @staticmethod
    def generate() -> str:
        n1 = RandomNumber.generate(n=3)
        n2 = RandomNumber.generate(n=3)

        return n1 + "-" + n2

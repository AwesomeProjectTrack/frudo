from typing import Any

from src.data_generator.base_data_generator import BaseDataGenerator
from src.data_generator.dataclasses import FullPassportNumber
from src.data_generator.rand_number import RandomNumber


class PassportNumber(BaseDataGenerator):
    """ """
    @staticmethod
    def generate() -> Any:
        """ """
        pser = RandomNumber.generate(n=4)
        pnum = RandomNumber.generate(n=6)
        return FullPassportNumber(pser=pser, pnum=pnum)

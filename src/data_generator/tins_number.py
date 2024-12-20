import random

from src.data_generator.base_data_generator import BaseDataGenerator


class TinsNumber(BaseDataGenerator):
    @staticmethod
    def generate() -> str:
        nums = [random.randint(1, 9) if x == 0 else random.randint(0, 9) for x in range(0, 10)]

        weights = [[7, 2, 4, 10, 3, 5, 9, 4, 6, 8], [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]]
        nums.append(sum([n * w for w, n in zip(weights[0], nums)]) % 11 % 10)
        nums.append(sum([n * w for w, n in zip(weights[1], nums)]) % 11 % 10)

        return "".join(map(str, nums))

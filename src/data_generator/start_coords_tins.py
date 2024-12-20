from PIL import ImageFont

from src.data_generator.base_data_generator import BaseDataGenerator


class StartCoords(BaseDataGenerator):
    @staticmethod
    def generate(width: int, height: int, is_new_tins: bool = True, is_old_tin_number: bool = False) -> dict:
        if is_new_tins:
            return {
                "place_of_birth": [width // 3, height // 2 + 45],
                "birth_date": [width // 2, height // 2 - 45],
                "sex": [width // 5 - 40, height // 2 - 45],
                "name": [width // 3, 2 * (height // 5) + 40],
                "issued": [width // 3 - 50, 3 * (height // 5) + 60],
                "tin": [3 * width // 4, 3 * (height // 5) + 60],
            }
        else:
            return {
                "place_of_birth": [3 * width // 10, 4 * height // 10 + 17],
                "birth_date": [4 * width // 6, 4 * height // 10 - 17],
                "sex": [width // 6, 4 * height // 10 - 17],
                "name": [width // 3, 2 * height // 6],
                "issued": [3 * width // 10 - 38, 6 * (height // 12) + 40],
                "tin": [5 * width // 10 + 30, 6 * (height // 12) + 40],
            }

from faker import Faker

from src.data_generator.base_data_generator import BaseDataGenerator
from src.data_generator.dataclasses import GeoPlaceDataclass

fake = Faker("ru_RU")


class GeoPlace(BaseDataGenerator):
    @staticmethod
    def generate():
        city = fake.city()  # Генерация случайного города
        region = fake.region()  # Генерация случайной области (региона)

        return GeoPlaceDataclass(city=city, region=region)

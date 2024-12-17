from pathlib import Path

import pandas as pd
import requests

from src.data_generator.base_data_generator import BaseDataGenerator
from src.data_generator.dataclasses import GeoPlaceDataclass


class GeoPlaceFromFile(BaseDataGenerator):
    @staticmethod
    def generate():
        # check file locally
        towns_path = Path("src/templates/towns.csv")

        if not towns_path.exists():
            url = "https://raw.githubusercontent.com/" "epogrebnyak/ru-cities/main/assets/towns.csv"
            content = requests.get(url).text
            towns_path.write_text(content, encoding="utf-8")

        # read as dataframe
        df_cities = pd.read_csv(towns_path)
        place = df_cities.sample(1)

        city = place.city.iloc[0]
        region = place.region_name.iloc[0]

        return GeoPlaceDataclass(city=city, region=region)

from typing import Any

import pandas as pd

from src.data_generator.base_data_generator import BaseDataGenerator
from src.data_generator.dataclasses import FullNameDataclass


class FullNameFromFileGenerator(BaseDataGenerator):
    @staticmethod
    def generate(gender: str = "мужской") -> Any:
        df_names = pd.read_csv("src/templates/names.csv")
        # df_names = pd.read_parquet("src/templates/names.parquet")

        full_name = df_names.sample(1)
        last_name = full_name.iloc[0, 0]
        first_name = full_name.iloc[0, 1]
        middle_name = full_name.iloc[0, 2]
        sx = "муж." if full_name.iloc[0, 3] == "М" else "жен."

        return FullNameDataclass(last_name=last_name, middle_name=middle_name, first_name=first_name, gender=sx)

import json
import shutil
from pathlib import Path

import pandas as pd

from src.output_formater.base_output_formater import BaseOutputFormater


class MTVQAOutputFormater(BaseOutputFormater):
    @staticmethod
    def load_json_from_file(file_path):
        """
        Загружает данные JSON из файла.

        Параметры:
        file_path : str
            Путь к JSON файлу.

        Возвращает:
        dict или list : Объект, загруженный из JSON.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def format(self, dataset_path: Path, output_dataset_path: Path | None) -> Path | str:
        if not isinstance(dataset_path, Path):
            dataset_path = Path(dataset_path)
        if output_dataset_path is None:
            output_dataset_path = "mtvqa"
        if not isinstance(output_dataset_path, Path):
            output_dataset_path = Path(output_dataset_path)
        output_dataset_path.mkdir(exist_ok=True, parents=True)
        columns = [
            "data_index",
            "split",
            "image_path",
            "question",
            "answer",
            "doc_class",
            "question_type",
            "answer_bbox",
        ]
        df = pd.DataFrame(columns=columns)
        for filename in (dataset_path / "jsons").iterdir():
            data = self.load_json_from_file(filename)
            for doc_class_type in list((dataset_path / "images").iterdir()):
                for key, value in data["fields"].items():
                    row_data = {
                        "data_index": data["index"],
                        "split": doc_class_type.stem,
                        "image_path": Path("images") / f"{data['index']}_{doc_class_type.stem}.jpg",
                        "question": f"Напиши {key}",
                        "answer": value["value"],
                        "doc_class": dataset_path.name,
                        "question_type": key,
                        "answer_bbox": str(value["bboxes"]),
                    }
                    df.loc[len(df)] = row_data

        df.to_csv(output_dataset_path / "annotations.csv", sep=";", encoding="utf-8-sig", index=False)
        shutil.copytree(dataset_path / "images" / "clean", output_dataset_path / "images", dirs_exist_ok=True)
        return output_dataset_path

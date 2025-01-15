import json
from abc import ABCMeta, abstractmethod
from pathlib import Path

from PIL import Image


class BaseDocumentGenerator(metaclass=ABCMeta):
    def __init__(self):
        self._template_path: str | Path = None
        self._output_path = self._get_output_path()
        self._doc_type: str | None = None

    @staticmethod
    def _get_tamplate_path():
        origin_path = Path("templates")
        if not origin_path.exists():
            origin_path.mkdir(exist_ok=True, parents=True)
        return origin_path

    @staticmethod
    def _get_output_path():
        origin_path = Path("dataset")
        if not origin_path.exists():
            origin_path.mkdir(exist_ok=True, parents=True)
        return origin_path

    @abstractmethod
    def _generate_one_sample(self) -> tuple[Image, dict]:
        pass

    def generate(self, num_samples: int) -> Path | str:
        output_path = self._output_path / self._doc_type
        output_path.mkdir(exist_ok=True, parents=True)
        (output_path / "images" / "clean").mkdir(exist_ok=True, parents=True)
        (output_path / "jsons").mkdir(exist_ok=True, parents=True)
        for index in range(num_samples):
            template, annotation = self._generate_one_sample()
            template.save(output_path / "images" / "clean" / f"{index}.jpg")
            annotation = {
                "fields": annotation,
                "index": index,
            }
            with open(output_path / "jsons" / f"{index}.json", "w", encoding="utf-8") as f:
                json.dump(annotation, f, ensure_ascii=False, indent=4)
        return output_path

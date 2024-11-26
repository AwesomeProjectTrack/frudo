import json
import uuid
from dataclasses import asdict
from pathlib import Path

from PIL import Image

from src.document_data_generator.dataclasses import Entity
from src.output_formater.base_output_formater import BaseOutputFormater


class JSONOutputFormater(BaseOutputFormater):
    def format(self, output_path: Path, annotations: dict[str, Entity], image: Image):
        if isinstance(output_path, str):
            output_path = Path(output_path)
        if not output_path.exists():
            output_path.mkdir(exist_ok=True)

        json_folder = output_path / "validation_dataset"
        image_folder = output_path / "validation_images"

        image_folder.mkdir(parents=True, exist_ok=True)

        json_folder.mkdir(parents=True, exist_ok=True)

        uid = uuid.uuid4()
        image_filename = f"{uid}.jpg"
        image.save(image_folder / image_filename)

        json_filename = f"{uid}.json"
        json_data = {key: value for key, value in annotations.items()}
        json_data["filename"] = str(image_folder / image_filename)
        with open(json_folder / json_filename, "w") as file:
            json.dump(json_data, file, indent=4)

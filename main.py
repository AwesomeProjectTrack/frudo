from pathlib import Path
from shutil import rmtree

import click
import yaml

from src.augmentations import get_augmentations
from src.document_generator import get_document_generator
from src.output_formater import get_output_formater
from src.task import Task


def get_config(config_path: Path):
    with open(config_path) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


@click.command()
@click.option("--config-path", help="Путь до конфига для запуска", type=click.Path(path_type=Path))
def main(config_path: Path):
    config = get_config(config_path)
    if Path(config.get("output_path")).exists():
        rmtree(config.get("output_path"))
    if config.get("document"):
        document_generators = [get_document_generator(name) for name in config.get("document")]
    else:
        document_generators = [get_document_generator("passport")]
    if config.get("augmentation"):
        augmentations = [get_augmentations(name) for name in config.get("augmentation")]
    else:
        augmentations = [get_augmentations("basic_aug")]
    if config.get("output_format"):
        output_formater = get_output_formater(config.get("output_format"))
    else:
        output_formater = get_output_formater("json")

    task = Task(
        document_generators=document_generators,
        output_formater=output_formater,
        augmentations=augmentations,
        output_path=config.get("output_path") or "validation_dataset",
    )
    task.execute(config.get("num_samples"))


if __name__ == "__main__":
    main()

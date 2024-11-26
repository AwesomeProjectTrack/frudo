from dataclasses import dataclass


@dataclass
class Entity:
    value: str
    bboxes: list[int | float]

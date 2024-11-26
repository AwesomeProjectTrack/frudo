from dataclasses import dataclass


@dataclass
class Entity:
    value: str
    bboxes: list[int | float]


@dataclass
class SnilsData:
    snils_number: Entity
    family_name: Entity
    middle_name: Entity
    first_name: Entity
    birth_date: Entity
    reg_date: Entity
    city: Entity
    region: Entity
    gender: Entity

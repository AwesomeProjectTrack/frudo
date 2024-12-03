from dataclasses import dataclass


@dataclass
class FullNameDataclass:
    last_name: str
    middle_name: str
    first_name: str
    gender: str  # добавил пол в класс для единообразия


@dataclass
class GeoPlaceDataclass:
    city: str
    region: str


@dataclass
class FullPassportNumber:
    pser: str
    pnum: str

from dataclasses import dataclass


@dataclass
class FullNameDataclass:
    last_name: str
    middle_name: str
    first_name: str


@dataclass
class GeoPlaceDataclass:
    city: str
    region: str

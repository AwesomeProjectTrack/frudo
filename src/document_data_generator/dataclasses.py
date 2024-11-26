from dataclasses import dataclass


@dataclass
class OutputDocumentData:
    field_name: str
    field_value: str
    bboxes: list[int | float]

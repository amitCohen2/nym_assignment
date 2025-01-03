from dataclasses import dataclass
from datetime import date


@dataclass
class Chart:
    name: str
    dob: date
    has_valid_ekg: bool

    @property
    def age(self) -> float:
        today = date.today()
        delta = today - self.dob
        return delta.days / 365.25

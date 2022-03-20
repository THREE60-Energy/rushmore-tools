from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Location:
    Region: str
    Country: str
    Stuff: Optional[str]


@dataclass
class RushmoreAbandonment:
    """Describes a single Rushmore Abandonment Review entry."""

    Location: Location
    WellId: int

    def __post_init__(self):
        self.WellId = f"Old: {self.WellId}, now is overridden in post init."

    def dump(self):
        {key: value for key, value in self.__dict__.items() if not key.startswith("_")}

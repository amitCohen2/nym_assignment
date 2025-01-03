from dataclasses import dataclass
from typing import Dict, List


@dataclass
class TextualWord:
    x0: float
    x1: float
    text: str


PagesToWords = Dict[int, List[TextualWord]]

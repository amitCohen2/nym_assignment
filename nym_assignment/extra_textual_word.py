from dataclasses import dataclass
from typing import Dict, List

from nym_assignment.textual_word import TextualWord


@dataclass
class ExtraTextualWord(TextualWord):
    fontname: str
    size: float

    @property
    def is_bold(self) -> bool:
        return 'Bold' in self.fontname


PagesToExtraWords = Dict[int, List[ExtraTextualWord]]

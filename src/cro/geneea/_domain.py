# -*- coding: utf8 -*-


from __future__ import annotations

from typing import Optional

import pandas as pd


class Text:
    def __init__(self, original: str, analyzed: dict):
        self.original = original.strip()
        self.analyzed = analyzed

    def __eq__(self, that: Optional[Text]) -> bool:
        return (self.original, self.analyzed) == (that.original, that.analyzed)

    def __hash__(self) -> int:
        return hash((self.original, self.analyzed))

    def __len__(self):
        return len(self.original)

    def entities(self) -> tuple[object]:
        ...

    def tags(self) -> tuple[object]:
        ...

    def relations(self) -> tuple[object]:
        ...

    def language(self) -> str:
        ...

    def sentiment(self) -> object:
        ...

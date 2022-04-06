# -*- coding: utf8 -*-


from __future__ import annotations

from typing import Optional

import json
import pandas as pd


class Text:

    """
    class to handle JSON respones
    """

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
        _entities = pd.DataFrame.from_dict(self.analyzed['entities'])
        return _entities

    def tags(self) -> tuple[object]:
        _tags = pd.DataFrame.from_dict(self.analyzed['tags'])
        return _tags

    def relations(self) -> tuple[object]:
        _relations = pd.DataFrame.from_dict(self.analyzed['relations'])
        return _relations

    def language(self) -> str:
        _language = self.analyzed['language']
        return _language

    def sentiment(self) -> object:
        _sentiment = pd.DataFrame.from_dict(self.analyzed)
        return _sentiment

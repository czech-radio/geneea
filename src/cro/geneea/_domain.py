# -*- coding: utf-8 -*-


from __future__ import annotations
from collections import namedtuple as NamedTuple
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
        pd.set_option("display.max_rows", None)

    def __eq__(self, that: Optional[Text]) -> bool:
        return (self.original, self.analyzed) == (that.original, that.analyzed)

    def __hash__(self) -> int:
        return hash((self.original, self.analyzed))

    def __len__(self):
        return len(self.original)

    """
    cast model first, then traslate to frames, optional

    """

    def entities(self) -> tuple[object]:
        _entities = pd.DataFrame.from_dict(self.analyzed["entities"])
        return _entities

    def tags(self) -> tuple[object]:
        _tags = pd.DataFrame.from_dict(self.analyzed["tags"])
        return _tags

    def relations(self) -> tuple[object]:
        _relations = pd.DataFrame.from_dict(self.analyzed["relations"])
        return _relations

    def language(self) -> str:
        _language = self.analyzed["language"]
        return _language

    def sentiment(self) -> object:
        _sentiment = self.analyzed["docSentiment"]
        return _sentiment


class Analysis:
    """
    top level class Analysis
    encapsluates lower level classes
    """

    text: Text
    language: str
    entities: List[Entity]
    tags: List[Tag]
    sentiment: Sentiment
    relations: List[Relation]


class Sentiment(NamedTuple):
    """
    originally docSentiment, it keeps sentiment of a whole document
    """

    mean: float
    label: str
    positive: float
    negative: float


class Entity(NamedTuple):
    """
    exctracted entities, known ones gets gkbId
    """

    id: str
    gkbId: str
    text: str
    type: str


class Relation(NamedTuple):
    """
    TODO: entitiy connection?
    """

    name: str
    type: str
    entity: Optional[Entity]


class Tag(NamedTuple):
    """
    tags derived from text
    """

    id: str
    text: str

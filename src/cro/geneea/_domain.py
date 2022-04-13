# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import Optional, NamedTuple

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

    def analysis(self) -> Analysis:
        _data = self.analyzed
        _analysis = Analysis(
            _data.original, language(), entities(), tags(), sentiment(), relations()
        )
        return _analysis

    def entities(self) -> tuple(Entities):
        _entities = self.analyzed["entities"]
        return _entities

    def tags(self) -> tuple(Tags):
        _tags = self.analyzed["tags"]
        return _tags

    def relations(self) -> tuple[object]:
        _relations = self.analyzed["relations"]
        return _relations

    def language(self) -> str:
        _language = self.analyzed["language"]
        return _language

    def sentiment(self) -> Sentiment:
        _sentiment = self.analyzed["docSentiment"]
        return _sentiment


# ??? def to_table(NamedTuple nt):
# pd.DataFrame.from_dict(self.analyzed["tags"])
#


class Analysis:
    """
    top level class Analysis
    encapsluates lower level classes
    """

    text: Text
    language: str
    entities: tuple(Entity)
    tags: tuple(Tag)
    sentiment: Sentiment
    relations: tuple(Relation)


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

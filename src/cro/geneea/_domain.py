# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import Optional, List, NamedTuple

import json
import pandas as pd


class Analysis(NamedTuple):
    """
    top level class Analysis
    encapsluates lower level classes
    """

    text: Text
    entities: tuple(Entity)
    tags: tuple(Tag)
    sentiment: Sentiment
    relations: tuple(Relation)


class Entity(NamedTuple):
    """
    exctracted entities, known ones gets gkbId
    """

    id: str
    stdForm: str
    type: str


entities: List[Entity] = []


class Sentiment(NamedTuple):
    """
    originally docSentiment, it keeps sentiment of a whole document
    """

    mean: float
    label: str
    positive: float
    negative: float


class Relation(NamedTuple):
    """
    TODO: entitiy connection?
    """

    id: str
    name: str
    textRepr: str
    type: str
    args: Optional[Entity]


class Tag(NamedTuple):
    """
    tags derived from text
    """

    id: str
    stdFrom: str
    type: str
    relevance: float


class Model:

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
            self.original,
            self.entities(),
            self.tags(),
            self.sentiment(),
            self.relations(),
        )
        return _analysis

    def entities(self) -> List[Entity]:
        entities: List[Entity] = []

        for entity in self.analyzed["entities"]:
            entities.append(Entity(entity["id"], entity["stdForm"], entity["type"]))

        return entities

    def tags(self) -> List[Tag]:
        tags: List[Tag] = []

        for tag in self.analyzed["tags"]:
            tags.append(Tag(tag["id"], tag["stdForm"], tag["type"], tag["relevance"]))
        return tags

    def relations(self) -> List[Relation]:
        relations: List[Relation] = []
        for relation in self.analyzed["relations"]:
            relations.append(
                Relation(
                    relation["id"],
                    relation["name"],
                    relation["textRepr"],
                    relation["type"],
                    relation["args"],
                )
            )
        return relations

    def language(self) -> str:
        return self.analyzed["language"]

    def sentiment(self) -> Sentiment:
        select = self.analyzed["docSentiment"]
        return Sentiment(
            select["mean"], select["label"], select["positive"], select["negative"]
        )

    # def as_dataframe(NamedTuple):
    #  return pd.DataFrame.from_dict()


# ??? def to_table(NamedTuple nt):
# pd.DataFrame.from_dict(self.analyzed["tags"])
#

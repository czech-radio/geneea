# -*- coding: utf-8 -*-

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import List, NamedTuple, Optional

import pandas as pd


@dataclass(frozen=True)
class Entity:
    """
    exctracted entities, known ones gets gkbId
    """

    id: str
    # gkbId: Optional[str]
    stdForm: str
    type: str


@dataclass(frozen=True)
class Sentiment:
    """
    originally docSentiment, it keeps sentiment of a whole document
    """

    mean: float
    label: str
    positive: float
    negative: float


@dataclass(frozen=True)
class Relation:
    """
    TODO: entitiy connection?
          not finished connecting to existing ones
    """

    id: str
    name: str
    textRepr: str
    type: str
    args: Optional[Entity]


@dataclass(frozen=True)
class Tag:

    """
    tags derived from text
    """

    id: str
    stdFrom: str
    type: str
    relevance: float


FullAnalysis = tuple[str, tuple[Entity], tuple[Tag], Sentiment, tuple[Relation]]


class Analysis:

    """
    Analysis domain model
    class to handle JSON respones,
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

    def analysis(self) -> FullAnalysis:

        return (
            self.original,
            self.entities(),
            self.tags(),
            self.sentiment(),
            self.relations(),
        )

    def entities(self) -> tuple[Entity]:
        _entities: List[Entity] = []
        for entity in self.analyzed["entities"]:
            _entities.append(Entity(entity["id"], entity["stdForm"], entity["type"]))

        return tuple(_entities)

    def tags(self) -> tuple[Tag]:
        _tags: List[Tag] = []

        for tag in self.analyzed["tags"]:
            _tags.append(Tag(tag["id"], tag["stdForm"], tag["type"], tag["relevance"]))
        return tuple(_tags)

    def relations(self) -> tuple[Relation]:
        _relations: List[Relation] = []
        for relation in self.analyzed["relations"]:
            _relations.append(
                Relation(
                    relation["id"],
                    relation["name"],
                    relation["textRepr"],
                    relation["type"],
                    relation["args"],
                )
            )
        return tuple(_relations)

    def language(self) -> str:
        return self.analyzed["language"]

    def sentiment(self) -> str:
        tmp = self.analyzed["docSentiment"]
        return Sentiment(tmp["mean"], tmp["label"], tmp["positive"], tmp["negative"])

    def to_table(self, input: tuple(object)) -> pd.DataFrame:
        tmplist = list(input)
        df = pd.DataFrame.from_dict([entry.as_dict() for entry in tmplist])
        return df

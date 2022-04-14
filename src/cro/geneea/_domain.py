# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import Optional, List, NamedTuple

import json
import pandas as pd


class Model:

    """
    class to handle JSON respones
    """

    def __init__(self, original: str, analyzed: dict):
        self.original = original.strip()
        self.analyzed = analyzed

        #        self.analysis = self.analysis()
        #        self.entities = self.entities()
        #        self.tags = self.tags()
        #        self.relations = self.relations()
        #        self.language = self.language()
        #        self.sentiment = self.sentiment()
        #        pd.set_option("display.max_rows", None)

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
        _entities: List[Entity] = []

        for entity in self.analyzed["entities"]:
            _entities.append(Entity(entity["id"], entity["stdForm"], entity["type"]))

        return _entities

    def tags(self) -> List[Tag]:
        _tags: List[Tag] = []

        for tag in self.analyzed["tags"]:
            _tags.append(Tag(tag["id"], tag["stdForm"], tag["type"], tag["relevance"]))
        return _tags

    def relations(self) -> List[Relation]:
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
        return _relations

    def language(self) -> str:
        return self.analyzed["language"]

    def sentiment(self) -> Sentiment:
        sentiment = self.analyzed["docSentiment"]
        return Sentiment(
            sentiment["mean"],
            sentiment["label"],
            sentiment["positive"],
            sentiment["negative"],
        )

    def to_table(self, input: tuple(object)) -> pd.DataFrame:
        tmplist = list(input)
        df = pd.DataFrame.from_dict([entry.as_dict() for entry in tmplist])
        return df


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
    # gkbId: Optional[str]
    stdForm: str
    type: str

    def as_dict(self):
        return {"id": self.id, "stdForm": self.stdForm, "type": self.type}


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
    # not finished connecting to existing ones
    args: Optional[Entity]

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "textRepr": self.textRepr,
            "type": self.type,
            "args": self.args,
        }


class Tag(NamedTuple):
    """
    tags derived from text
    """

    id: str
    stdFrom: str
    type: str
    relevance: float

    def as_dict(self):
        return {
            "id": self.id,
            "stdForm": self.stdForm,
            "type": self.type,
            "relevance": self.relevance,
        }

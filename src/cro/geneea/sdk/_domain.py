# -*- coding: utf-8 -*-

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import pandas as pd

__all__ = tuple(["Entity", "Sentiment", "Relation", "Tag", "Analysis"])


@dataclass(frozen=True)
class Entity:
    """
    Exctracted entities, known ones gets gkbId
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


@dataclass(frozen=True)
class Account:
    """
    an account entry
    """

    type: str
    remainingQuotas: str


FullAnalysis = tuple[str, tuple[Entity], tuple[Tag], Sentiment, tuple[Relation]]


class Analysis:

    """
    Analysis domain model.
    A class to handle JSON respones.
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
        """
        Initialize analysis, it returns FullAnalysis type by default.
        :return: FullAnalysis type
        """
        return (
            self.original,
            self.entities(),
            self.tags(),
            self.sentiment(),
            self.relations(),
        )

    def entities(self) -> tuple[Entity]:
        """
        Returns a tuple of Entities from analyzed JSON.
        :return: tuple[Entity]
        """
        _entities: List[Entity] = []
        for entity in self.analyzed["entities"]:
            _entities.append(Entity(entity["id"], entity["stdForm"], entity["type"]))

        return tuple(_entities)

    def tags(self) -> tuple[Tag]:
        """
        Function returns a tuple of Tags from analyzed JSON.
        :return: tuple[Tag]
        """
        _tags: List[Tag] = []

        for tag in self.analyzed["tags"]:
            _tags.append(Tag(tag["id"], tag["stdForm"], tag["type"], tag["relevance"]))
        return tuple(_tags)

    def relations(self) -> tuple[Relation]:
        """
        Function returns a tuple of Realtions from analyzed JSON.
        :return: tuple[Tag]
        """
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
        """
        Returns string object representing language.
        :return: str of detected language
        """
        return self.analyzed["language"]

    def sentiment(self) -> Sentiment:
        """
        Functions which returns Sentiment object from analyzed JSON.
        :return: Sentiment object
        """
        tmp = self.analyzed["docSentiment"]
        return Sentiment(tmp["mean"], tmp["label"], tmp["positive"], tmp["negative"])

    def account(self) -> Account:
        """
        Function returns Account object from Analyzed JSON.
        :return: Account object
        """
        return Account(self.analyzed["type"], self.analyzed["remainingQuotas"])

    def to_table(self, input: tuple(object)) -> pd.DataFrame:
        """
        Function converting a tuple of objects into Pandas DataFrame.
        """
        tmplist = list(input)
        df = pd.DataFrame.from_dict([entry.as_dict() for entry in tmplist])
        return df

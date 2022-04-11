# -*- coding: utf-8 -*-

from collections import namedtuple as NamedTuple


class Analysis:
    """
    top level class Analysis
    encapsluates lower level classes
    """

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

# -*- coding: utf-8 -*-


"""
Contains a domain model for Geneea NLP service.
"""


from __future__ import annotations

import dataclasses
import json
import xml.etree.cElementTree as ET
from dataclasses import dataclass
from typing import List, Optional

import pandas as pd

__all__ = tuple(["Tag", "Account", "Entity", "Sentiment", "Relation", "Analysis"])


Text = str
JSON = str
XML = str


@dataclass(frozen=True)
class Serializable:  # JSON:
    def to_json(self) -> JSON:
        result = json.dumps(dataclasses.asdict(self), ensure_ascii=False)
        return result


@dataclass(frozen=True)
class Tag(Serializable):
    """
    Tags derived from the document content.
    """

    id: str
    stdForm: str
    type: str
    relevance: float


@dataclass(frozen=True)
class Account(Serializable):
    """
    The Geneeas account informations.
    """

    type: str
    remainingQuotas: str


@dataclass(frozen=True)
class Entity(Serializable):
    """
    Entities extracted from the document content.
    """

    id: str
    # gkbId: Optional[str] # The recognized entities gets `gkbId`.
    stdForm: str
    type: str


# class EntityType(enun):
#     duration
#     organization
#     ...


# class relationType(enum):
#     VERB
#     ATTR
#     ...


@dataclass(frozen=True)
class Sentiment(Serializable):
    """
    Sentiment of the whole document content.
    """

    mean: float
    label: str
    positive: float
    negative: float


@dataclass(frozen=True)
class Relation(Serializable):
    """
    The relations between entities.
    """

    id: str
    name: str
    textRepr: str
    type: str
    args: Optional[Entity]


@dataclass(frozen=True)
class Paragraph(Serializable):
    """
    The text paragraph.
    """

    id: str
    tokens: list[str]


@dataclass(frozen=True)
class Sentence(Serializable):
    ...


@dataclass(frozen=True)
class Token(Serializable):
    ...


@dataclass(frozen=True)
class Analysis(Serializable):  # Aggregate
    """
    Analysis aggregate root entity.
    """

    original: str  # content
    analyzed: dict

    def __len__(self) -> int:
        """
        Get the length of the original text.
        """
        return len(self.original)

    @property
    def entities(self) -> tuple[Entity]:
        """
        Returns a tuple of Entities from analyzed JSON.
        :return: tuple[Entity]
        """
        _entities: List[Entity] = []
        for entity in self.analyzed["entities"]:
            _entities.append(Entity(entity["id"], entity["stdForm"], entity["type"]))

        return tuple(_entities)

    @property
    def tags(self) -> tuple[Tag]:
        """
        Function returns a tuple of Tags from analyzed JSON.
        :return: tuple[Tag]
        """
        _tags: List[Tag] = []

        for tag in self.analyzed["tags"]:
            _tags.append(Tag(tag["id"], tag["stdForm"], tag["type"], tag["relevance"]))
        return tuple(_tags)

    @property
    def relations(self) -> tuple[Relation]:
        """
        Get a tuple of realtions.
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

    @property
    def language(self) -> str:
        """
        Returns string object representing language.
        :return: str of detected language
        """
        return self.analyzed["language"]

    @property
    def sentiment(self) -> Sentiment:
        """
        Functions which returns Sentiment object from analyzed JSON.
        :return: Sentiment object
        """
        tmp = self.analyzed["docSentiment"]
        return Sentiment(tmp["mean"], tmp["label"], tmp["positive"], tmp["negative"])

    @property
    def account(self) -> Account:
        """
        Get the account object.
        :return: The account object.
        """
        return Account(None, None)

    @property
    def paragraphs(self) -> Any:
        return self.analyzed["paragraphs"]

    @property
    def version(self):
        return self.analyzed["version"]

    @property
    def language(self):
        return self.analyzed["language"]["detected"]

    # Serialization

    def to_xml(self) -> XML:
        """
        Writes XML from given tuple of Model objects
        """

        def _normalize_xml(root) -> XML:
            """
            Produces pretty XML file.
            """
            import os
            import xml.dom.minidom
            import xml.etree.cElementTree as ET

            xml_str = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
            result = os.linesep.join([s.strip() for s in xml_str.splitlines()])
            return result

        root = ET.Element("document")

        ET.SubElement(
            root, "original", length=f"{len(self.original)}"
        ).text = self.original

        analysis = ET.SubElement(root, "analysis")

        ### Add Entities to XML tree
        entities = ET.SubElement(analysis, "entities")
        for obj in self.entities:
            ET.SubElement(
                entities, "entity", id=f"{obj.id}", type=f"{obj.type}"
            ).text = f"{obj.stdForm}"

        ### Add Tags to XML tree
        tags = ET.SubElement(analysis, "tags")
        for obj in self.tags:
            ET.SubElement(
                tags, "tag", id=f"{obj.id}", relevance=f"{obj.relevance}"
            ).text = f"{obj.stdForm}"

        ### Add Sentiment object to XML tree
        sentiment = ET.SubElement(
            analysis,
            "sentiment",
            mean=f"{self.sentiment.mean}",
            positive=f"{self.sentiment.positive}",
            negative=f"{self.sentiment.negative}",
        ).text = f"{self.sentiment.label}"

        ### Add Relations to XML tree
        relations = ET.SubElement(analysis, "relations")
        for obj in self.relations:
            ET.SubElement(
                relations,
                "relation",
                id=f"{obj.id}",
                textRepr=f"{obj.textRepr}",
                type=f"{obj.type}",
            ).text = f"{obj.name}"

        ### Add Paragrahs to XML Tree
        paragraphs = ET.SubElement(analysis, "paragraphs")
        for obj in self.paragraphs:
            paragraph_node = ET.SubElement(
                paragraphs,
                "paragraph",
                id=f"{obj['id']}",
                type=f"{obj['type']}",
                text=obj["text"],
            )
            sentences = ET.SubElement(paragraph_node, "sentences")

            for sentence in obj["sentences"]:
                ET.SubElement(
                    paragraph_node,
                    "sentence",
                    id=sentence["id"],
                    tokens=sentence["tokens"],
                )

        result = _normalize_xml(root)

        return result

    def to_table(self, input: tuple(object)) -> pd.DataFrame:
        """
        Function converting a tuple of objects into Pandas DataFrame.
        """
        tmplist = list(input)
        df = pd.DataFrame.from_dict([entry.as_dict() for entry in tmplist])
        return df

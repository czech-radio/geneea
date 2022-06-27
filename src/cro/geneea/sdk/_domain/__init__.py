# -*- coding: utf-8 -*-


"""
Contains a domain model for Geneea NLP REST (JSON) service.
"""


from __future__ import annotations

import dataclasses
import enum
import json
import xml.dom.minidom
import xml.etree.cElementTree as ET
from dataclasses import dataclass
from typing import Any, Generic, List, Optional, TypeVar

import pandas as pd

__all__ = tuple(
    [
        "Account",
        "Entity",
        "Tag",
        "Sentence",
        "Sentiment",
        "Paragraphs",
        "Relation",
        "Mention",
        "Document",
    ]
)

# #################################################################################### #

Text = str  #: The text content alias.
XML = str  #: The XML content alias.
JSON = str  #: The JSON content alias.

# #################################################################################### #


@dataclass(frozen=True, slots=True)
class Serializable:
    # [ ] XML Serializable
    # [x] JSON Serializable
    def to_json(self) -> JSON:
        result = json.dumps(dataclasses.asdict(self), ensure_ascii=False)
        return result


@dataclass(frozen=True, slots=True)
class Identifiable:
    id: str


# #################################################################################### #


@dataclass(frozen=True, slots=True)
class Tag(Identifiable, Serializable):
    """
    Tags derived from the document content.
    """

    type: str  #: FIXME
    stdForm: str  #: FIXME
    relevance: float  #: FIXME


@dataclass(frozen=True, slots=True)
class Account(Serializable):
    """
    The account informations.
    """

    type: str  #: The account type.
    remainingQuotas: str  #: ???


class EntityType(enum.Enum):
    SET = "set"
    NUMBER = "number"
    DURATION = "diration"
    ORGANIZATION = "organization"
    LOCATION = "location"


@dataclass(frozen=True, slots=True)
class Entity(Identifiable, Serializable):
    """
    Entities extracted from the document content.
    """

    type: str
    stdForm: str
    # gkbId: Optional[str] # The recognized entities gets `gkbId`.
    # mentions:  {"id": "m0", "mwl": "každý den", "text": "každý den", "tokenIds" }


class RelationType(enum.Enum):
    VERB = "verb"
    ATTR = "attr"


@dataclass(frozen=True, slots=True)
class Sentiment(Serializable):
    """
    Sentiment of the whole document content.
    """

    # numerical values
    mean: float  # FIXME In XML str: we wants float
    positive: float
    negative: float
    # textual value <== numerical values
    label: str  # ??? neutral ...


@dataclass(frozen=True, slots=True)
class Relation(Identifiable, Serializable):
    """
    The relations between entities.
    """

    type: str  # FIXME Enum
    textRepr: str  # FIXME camelcase to snake_case or shorten
    name: str  # ???
    args: Optional[str]  # entity_id

    def __post_init__(self):
        # Check that `id` == r{number}
        pass


# #################################################################################### #


@dataclass(frozen=True, slots=True)
class Token(Serializable):
    """
    The token (word or interpunction).

    The position within raw text is offset + len(text).
    """

    id: str
    text: str
    offset: int
    relevance: Optional[float] = None  # NOTE: [optional/required]

    def __post_init__(self) -> None:
        # Check that `id == w{integer >= 0}.
        # Check that `offset >= 0`

        pass

    def __len__(self) -> int:
        return len(self.text)


@dataclass(frozen=True, slots=True)
class Sentence(Identifiable, Serializable):
    """
    The sentence consist of tokens.
    """

    tokens: tuple[str]

    def __post_init__(self) -> None:
        # Check the id matches regular expression `s{integer}`.
        pass

    def __len__(self) -> int:
        """
        Return the number of tokens (or length of raw text?).
        """
        return len(tokens)


@dataclass(frozen=True, slots=True)
class Paragraph(Identifiable, Serializable):
    """
    The paragraph consist of sentences.
    """

    type: str  # ENUM? např. BODY
    sentences: tuple[Sentence]

    @property
    def text(self) -> str:
        """
        Get the text from sentences tokens.
        """
        return NotImplemented

    def __post_init__(self) -> None:
        # Check the id matches regular expression `p{integer}`.
        pass


@dataclass(frozen=True, slots=True)
class Mention:
    """
    FIXME The mantion model.
    """


# #################################################################################### #


@dataclass(frozen=True, slots=True)
class Document(Serializable):  # AGGREGATE
    """
    Document main aggregate entity.

    OriginalContent  = raw str
    AnalysedContent  = obj tree

    def __init__(self, original):
        self.original = original

    def __eq__(self, that: obj) -> bool:
        return NotImplemented

    def __hash__(self) -> int:
        return NotImplemented
    """

    original: Text  # content
    analysed: dict  # content

    def __len__(self) -> int:
        """
        Get the length of the original text.
        """
        return len(self.original)

    # ###############################################################################  #
    #                                   PROPERTIES                                     #
    # ###############################################################################  #

    @property
    def language(self) -> str:  # FIXME Return domain object
        """
        Get the detected language abbreviation  e.g `cs`.

        :return: The detected language abbreviation.
        """
        return self.analysed.get("language").get("detected")

    @property
    def version(self) -> str:  # FIXME Return domain object.
        """
        Get the service version used to analyze the content (i.e. REST API version).

        :return: The service version.
        """
        return self.analysed.get("version")

    @property
    def account(self) -> Account:
        """
        Get the account information.

        :return: The account information.
        """
        return Account(None, None)  # FIXME [Sentinel values]

    @property
    def entities(self) -> tuple[Entity]:
        """
        Get the analysed entities.

        :return: The analysed entities.
        """
        result = tuple(
            (
                Entity(id=entity["id"], stdForm=entity["stdForm"], type=entity["type"])
                for entity in self.analysed.get("entities")
            )
        )

        return result

    @property
    def tags(self) -> tuple[Tag]:
        """
        Get the analysed tags.

        :return: The analysed tags.
        """
        result = tuple(
            (
                Tag(
                    id=tag.get("id"),
                    stdForm=tag.get("stdForm"),
                    type=tag.get("type"),
                    relevance=tag.get("relevance"),
                )
                for tag in self.analysed.get("tags")
            )
        )

        return result

    @property
    def relations(self) -> tuple[Relation]:
        """
        Get the analysed relations.

        :return: The analysed relations.
        """
        result = tuple(
            (
                Relation(
                    id=relation["id"],
                    name=relation["name"],
                    type=relation["type"],
                    args=relation["args"],
                    textRepr=relation["textRepr"],
                )
                for relation in self.analysed["relations"]
            )
        )

        return result

    @property
    def sentiment(self) -> Sentiment:
        """
        Get the analysed sentiment.

        :return: The analysed sentiment.
        """
        return Sentiment(
            mean=self.analysed.get("docSentiment").get("mean"),
            positive=self.analysed.get("docSentiment").get("positive"),
            negative=self.analysed.get("docSentiment").get("negative"),
            label=self.analysed.get("docSentiment").get("label"),
        )

    @property
    def paragraphs(self) -> tuple[Paragraph]:
        """
        Get the document paragraphs.

        :return: The document paragraphs.
        """
        result = tuple(
            (
                Paragraph(
                    id=paragraph.get("id"),
                    type=paragraph.get("type"),
                    sentences=tuple(
                        (
                            Sentence(
                                id=sentence.get("id"),
                                tokens=tuple(
                                    (
                                        Token(
                                            id=token.get("id"),
                                            text=token.get("text"),
                                            offset=token.get("off"),
                                            relevance=token.get("relevance"),
                                        )
                                        for token in sentence["tokens"]
                                    )
                                ),
                            )
                            for sentence in paragraph.get("sentences")
                        )
                    ),
                )
                for paragraph in self.analysed.get("paragraphs")
            )
        )

        return result

    # ###############################################################################  #
    #                                 SERIALIZATION                                    #
    # ###############################################################################  #

    def to_xml(self) -> XML:
        """
        Serialize entity to XML format.

        e.g. XML

        <?xml version='1.0' encoding='utf8'?>
        <document>
            <content length="123">
                [text]
            </content>
            <analysis version="3.2.1">
                ...
            </analysis>
        </document>
        """
        root = ET.Element("document")

        # Add content element (node) to XML tree.
        ET.SubElement(
            root, "original", length=f"{len(self.original)}"
        ).text = self.original

        analysis = ET.SubElement(root, "analysis")

        # Add entity elements (nodes) to XML tree.
        entities = ET.SubElement(analysis, "entities")
        for obj in self.entities:
            ET.SubElement(
                entities, "entity", id=f"{obj.id}", type=f"{obj.type}"
            ).text = f"{obj.stdForm}"

        # Add tags elements (nodes) to XML tree.
        tags = ET.SubElement(analysis, "tags")
        for obj in self.tags:
            ET.SubElement(
                tags, "tag", id=f"{obj.id}", relevance=f"{obj.relevance}"
            ).text = f"{obj.stdForm}"

        # Add sentiment element (node) to XML tree.
        sentiment = ET.SubElement(
            analysis,
            "sentiment",
            mean=f"{self.sentiment.mean}",
            positive=f"{self.sentiment.positive}",
            negative=f"{self.sentiment.negative}",
        ).text = f"{self.sentiment.label}"

        # Add relations elements (nodes) to XML tree.
        relations = ET.SubElement(analysis, "relations")
        for obj in self.relations:
            assert isinstance(obj, Relation)  # NOTE: [For debugging purpose.]
            ET.SubElement(
                relations,
                "relation",
                id=f"{obj.id}",
                textRepr=f"{obj.textRepr}",
                type=f"{obj.type}",
            ).text = f"{obj.name}"

        # Add paragrahs element (nodes) to XML tree.
        paragraphs = ET.SubElement(analysis, "paragraphs")
        for obj in self.paragraphs:
            assert isinstance(obj, Paragraph)  # NOTE: [For debugging purpose.]
            paragraph_node = ET.SubElement(
                paragraphs,
                "paragraph",
                id=f"{obj.id}",
                type=f"{obj.type}",
                text=f"{obj.text}",
            )
            # Add sentence elements (nodes) to each paragraph element (node).
            sentences = ET.SubElement(paragraph_node, "sentences")
            for sentence in obj.sentences:
                sentence_node = ET.SubElement(sentences, "sentence", id=sentence.id)
                # Add token elements (nodes) to each sentence element (node).
                tokens = ET.SubElement(sentence_node, "tokens")
                for token in sentence.tokens:
                    ET.SubElement(
                        tokens,
                        "token",
                        id=f"{token.id}",
                        offset=f"{token.offset}",
                        text=f"{token.text}",
                    )

        result: str = xml.dom.minidom.parseString(
            ET.tostring(root, encoding="utf-8", method="xml")
        ).toprettyxml()

        return result

    def to_table(self, input: tuple(object)) -> pd.DataFrame:
        """
        Function converting a tuple of objects into Pandas DataFrame.
        """
        tmplist = list(input)
        df = pd.DataFrame.from_dict([entry.as_dict() for entry in tmplist])
        return df

    # ###############################################################################  #
    #                                   FACTORIES                                      #
    # ###############################################################################  #

    @classmethod
    def from_json(cls, json: str) -> Analysis:
        analysed = json  # alias


# #################################################################################### #

T = TypeVar("T")  #: The type to serialize.
U = TypeVar("U")  #: The type after serialization.


class Serializer(Generic[T, U]):
    """
    Serializer (mapper/converter) transforms the type `T` into `U` (e.g. XML or JSON serializer).
    """

    def serialize(entity: T) -> U:
        """
        Serialize the entity of type `T` to format of type `U`.
        """

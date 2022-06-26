# -*- coding: utf-8 -*-


"""
Contains a domain model for Geneea NLP service.
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
        "Analysis",
        "Document",
    ]
)

# #################################################################################### #

Text = str
JSON = str
XML = str

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

    type: str  #: ???
    stdForm: str  #: ???
    relevance: str  #: FIXME Should be `float`.


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
    args: Optional[Entity]

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
    relevance: float  # FIXME It is the string in XML: we want float.

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

    sentences: tuple[Sentence]
    type: str  # ENUM? např. BODY

    def __post_init__(self) -> None:
        # Check the id matches regular expression `p{integer}`.
        pass


# #################################################################################### #


@dataclass(frozen=True, slots=True)
class Analysis(Serializable):  # Aggregate @ Document.
    """
    Analysis aggregate root entity.

    OriginalContent  = raw str
    AnalysedContent  = obj tree

    class Document:
        id: ...
        original: OriginalContent
        analysed: AnalysedContent
        hash

    def __init__(self, original):
        self.original = original

    def __eq__(self, that: obj) -> bool:
        return NotImplemented

    def __hash__(self) -> int:
        return NotImplemented

    """

    original: str  # content
    analysed: dict

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
        for entity in self.analysed["entities"]:
            _entities.append(Entity(entity["id"], entity["stdForm"], entity["type"]))

        return tuple(_entities)

    @property
    def tags(self) -> tuple[Tag]:
        """
        Function returns a tuple of Tags from analyzed JSON.
        :return: tuple[Tag]
        """
        _tags: List[Tag] = []

        for tag in self.analysed["tags"]:
            _tags.append(Tag(tag["id"], tag["stdForm"], tag["type"], tag["relevance"]))
        return tuple(_tags)

    @property
    def relations(self) -> tuple[Relation]:
        """
        Get a tuple of realtions.
        :return: tuple[Tag]
        """
        _relations: List[Relation] = []
        for relation in self.analysed["relations"]:
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
        return self.analysed["language"]

    @property
    def sentiment(self) -> Sentiment:
        """
        Functions which returns Sentiment object from analyzed JSON.
        :return: Sentiment object
        """
        tmp = self.analysed["docSentiment"]
        return Sentiment(tmp["mean"], tmp["label"], tmp["positive"], tmp["negative"])

    @property
    def account(self) -> Account:
        """
        Get the account object.
        :return: The account object.
        """
        return Account(None, None)

    @property
    def paragraphs(self) -> Any:  # FIXME Return domain object.
        """
        Get the document paragraphs.

        :return: The document paragraphs.
        """
        return self.analysed["paragraphs"]

    @property
    def version(self) -> str:  # FIXME Return domain object.
        return self.analysed["version"]

    @property
    def language(self) -> str:  # FIXME Return domain object.
        """
        Get the document detected language.

        Possible values are: FIXME

        :return: The detected language.
        """
        return self.analysed["language"]["detected"]

    # ###############################################################################  #
    #                                 SERIALIZATION                                    #
    # ###############################################################################  #

    def to_xml(self) -> XML:
        """
        Serialize entity to XML format.

        e.g.

        <?xml version='1.0' encoding='utf8'?>
        <xml>
            <test>123</test>
        </xml>
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
            ET.SubElement(
                relations,
                "relation",
                id=f"{obj.id}",
                textRepr=f"{obj.textRepr}",
                type=f"{obj.type}",
            ).text = f"{obj.name}"

        # Add paragrah elemente (nodes) to XML tree.
        paragraphs = ET.SubElement(analysis, "paragraphs")
        for obj in self.paragraphs:
            paragraph_node = ET.SubElement(
                paragraphs,
                "paragraph",
                id=f"{obj['id']}",
                type=f"{obj['type']}",
                text=obj["text"],
            )
            # Add sentence elements (nodes) to paragraph element (node).
            sentences = ET.SubElement(paragraph_node, "sentences")
            for sentence in obj["sentences"]:
                sentence_node = ET.SubElement(
                    sentences,
                    "sentence",
                    id=sentence["id"]
                    # tokens=sentence["tokens"],
                )
                # Add token elements (nodes) to sentende element (node).
                tokens = ET.SubElement(sentence_node, "tokens")
                for token in sentence["tokens"]:
                    ET.SubElement(
                        tokens,
                        "token",
                        id=f'{token["id"]}',
                        offset=f'{token["off"]}',
                        text=f'{token["text"]}',
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


# #################################################################################### #

T = TypeVar("T")  #: The type to serialize.
U = TypeVar("U")  #: The type after serialization.


class Serializer(Generic[T, U]):
    """
    Serializer (maper/converter) transforms the type `T` into `U`.
    """

    def serialize(entity: T) -> U:
        """
        Serialize the entity of type `T` to format of type `U`.
        """


# TODO
# XML Serializer
# JSON Serializer

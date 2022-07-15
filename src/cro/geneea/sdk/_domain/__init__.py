# -*- coding: utf-8 -*-


"""Contains a domain model for Geneea NLP REST (JSON) service."""


from __future__ import annotations

import dataclasses
import enum
import json
import xml.dom.minidom
import xml.etree.cElementTree as ET
from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar

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


Text = str  #: The text content alias.
XML = str  #: The XML content alias.
JSON = str  #: The JSON content alias.


@dataclass(frozen=True, slots=True)
class Serializable:
    """
    The serializable dataclasses.
    # - [ ] XML Serializable
    # - [x] JSON Serializable
    """

    def to_json(self) -> JSON:
        """
        Serialize dataclass to JSON.

        :retrun: The JSON serialized dataclass.
        """
        result = json.dumps(dataclasses.asdict(self), ensure_ascii=False)
        return result


@dataclass(frozen=True, slots=True)
class Identifiable:
    id: str


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


@dataclass(frozen=True, slots=True)
class Language:
    expected: str  #: The expected document language.
    detected: str  #: The detected document language.

    def __post__init__(self) -> None:
        """
        Check the language abbreviation format.

        "cs" accept
        "en" accept
        "XX" reject
        """


@dataclass(frozen=True, slots=True)
class Version:
    major: int  #: The major version number.
    minor: int  #: The minor version number.
    patch: int  #: The patch version number.

    def __post__init__(self) -> None:
        """
        Check the version major, minor and patch number.

        0.0.1 accept
        0.1.0 accept
        1.0.0 accept
        0.0.0 reject
        """


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
    mentions: Optional[
        dict
    ] = None  #: e.g {"id": "m0", "mwl": "každý den", "text": "každý den", "tokenIds" }
    gkbId: Optional[str] = None  #: The recognized entities gets `gkbId`.
    sentiment: Optional[str] = None
    derive_from: Optional[str] = None  #: + is_derived


class RelationType(enum.Enum):
    VERB = "verb"  # The verb part od speech.
    ATTR = "attr"  # the attribute.


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


class Document(object):  # ROOT_ENTITY
    """
    Represents a document completely analysed by Geneea NLP service.
    """

    def __init__(
        self,
        original: Text,
        language: Text,
        version: Text,
        sentiment: Optional[Sentiment] = None,
        paragraphs: tuple[Paragraph] | None = None,
        entities: tuple[Entity] | None = None,
        relations: tuple[Relation] | None = None,
        tags: tuple[Tag] | None = None,
    ) -> None:
        """
        Don't use directly:  use the :meth:`create()` factory method!

        :param original: The original document content.
        :param language: The detected language.
        :param version: The service version.
        """
        assert len(original) > 0
        self._original = original
        self._language = language
        self._version = version
        # The complete Geneea NLP analysis.
        self._sentiment = sentiment
        self._paragraphs = paragraphs
        self._entities = entities
        self._relations = relations
        self._tags = tags

    def __len__(self) -> int:
        """
        Get the length of the original text.
        """
        return len(self.original)

    # < > <= >= Sort by the content length.

    def __eq__(self, that: obj) -> bool:
        """
        Check if the objects are equal.
        """
        return (type(self), self.original) == (type(that), that.original)

    def __hash__(self) -> int:
        """
        Get the objects hash.
        """
        return hash((type(self), self.original))

    # Factories

    @classmethod
    def create(cls, original, analysed: JSON) -> Optional[Document]:
        """
        Create a new instance of document from the JSON input.

        :param original: The original content.
        :param: analysed: The analysed content.
        :return: The new instance of document or None on error.
        """
        # Get the language from JSON attribute.
        language = analysed.get("language").get("detected")

        # Get the version from JSON attribute.
        version = analysed.get("version")

        # # Get the sentiment from JSON attribute.
        sentiment = None
        if analysed.get("docSentiment") is not None:
            sentiment = Sentiment(
                mean=analysed.get("docSentiment").get("mean"),
                positive=analysed.get("docSentiment").get("positive"),
                negative=analysed.get("docSentiment").get("negative"),
                label=analysed.get("docSentiment").get("label"),
            )

        # Get the entities from JSON attribute.
        entities = None
        if analysed.get("entities") is not None:
            entities = tuple(
                (
                    Entity(
                        id=entity["id"],
                        stdForm=entity["stdForm"],
                        type=entity["type"],
                        mentions=entity["mentions"],
                    )
                    for entity in analysed.get("entities")
                )
            )

        # Get the tag from JSON attribute.
        tags = None
        if analysed.get("tags") is not None:
            tags = tuple(
                (
                    Tag(
                        id=tag.get("id"),
                        stdForm=tag.get("stdForm"),
                        type=tag.get("type"),
                        relevance=tag.get("relevance"),
                    )
                    for tag in analysed.get("tags")
                )
            )

        # Get the relations from JSON attribute.
        relations = None
        if analysed.get("relations") is not None:
            relations = tuple(
                (
                    Relation(
                        id=relation["id"],
                        name=relation["name"],
                        type=relation["type"],
                        args=relation["args"],
                        textRepr=relation["textRepr"],
                    )
                    for relation in analysed["relations"]
                )
            )

        # Get the paragraphs from JSON attribute.
        paragraphs = None
        if analysed.get("paragraphs") is not None:
            paragraphs = tuple(
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
                    for paragraph in analysed.get("paragraphs")
                )
            )

        result = cls(
            original=original,
            language=language,
            version=version,
            sentiment=sentiment,
            paragraphs=paragraphs,
            entities=entities,
            relations=relations,
            tags=tags,
        )

        return result

    # Properties

    @property
    def original(self) -> str:
        return self._original

    @property
    def language(self) -> str:  # FIXME Return domain object
        """
        Get the detected language abbreviation  e.g `cs`.

        :return: The detected language abbreviation.
        """
        return self._language

    @property
    def version(self) -> str:  # FIXME Return domain object.
        """
        Get the service version used to analyze the content (i.e. REST API version).

        :return: The service version.
        """
        return self._version

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
        return self._entities

    @property
    def tags(self) -> tuple[Tag]:
        """
        Get the analysed tags.

        :return: The analysed tags.
        """
        return self._tags

    @property
    def relations(self) -> tuple[Relation]:
        """
        Get the analysed relations.

        :return: The analysed relations.
        """
        return self._relations

    @property
    def sentiment(self) -> Optional[Sentiment]:
        """
        Get the analysed sentiment.

        :return: The analysed sentiment.
        """
        return self._sentiment

    @property
    def paragraphs(self) -> tuple[Paragraph]:
        """
        Get the document paragraphs.

        :return: The document paragraphs.
        """
        return self._paragraphs

    # Serializers (convertors)

    def to_xml(self, encoding="utf-8") -> XML:
        """
        Serialize object to XML format.

        :return: The serialized object.

        The XML should look like the following example.

        ..code: xml
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
        entities_node = ET.SubElement(analysis, "entities")
        mentions_node = ET.SubElement(analysis, "mentions")
        for entity in self.entities:
            entity_node = ET.SubElement(
                entities_node,
                "entity",
                id=f"{entity.id}",
                type=f"{entity.type}",
                stdForm=f"{entity.stdForm}",
            )
            # Add mention elements (nodes) to each entity element (node).
            for mention in entity.mentions:
                mention_node = ET.SubElement(
                    mentions_node,
                    "mention",
                    id=mention.get("id"),
                    entityId=entity.id,
                    mwl=mention.get("mwl"),
                    tokenIds=",".join(mention.get("tokenIds")),
                ).text = mention.get("text")

        # Add tags elements (nodes) to XML tree.
        tags = ET.SubElement(analysis, "tags")
        for tag in self.tags:
            ET.SubElement(
                tags, "tag", id=f"{tag.id}", relevance=f"{tag.relevance}"
            ).text = f"{tag.stdForm}"

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
                        tokens, "token", id=f"{token.id}", offset=f"{token.offset}"
                    ).text = f"{token.text}"

        result: str = xml.dom.minidom.parseString(
            ET.tostring(root, encoding=encoding, method="xml")
        ).toprettyxml()

        return result

    def to_json(self) -> JSON:
        return "JSON WILL BE HERE!"

    def to_table(self) -> pd.DataFrame:
        """
        Convert objects into pandas data-frame.
        :return: The pandad data-frame with collected data.
        """
        # result = pd.DataFrame.from_dict(self.analysed)
        result = NotImplemented
        return result

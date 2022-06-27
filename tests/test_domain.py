# -*- coding: utf-8 -*-


"""
The unit tests for domain models.

Tips: To compaere multiple values you can use th tuple e.g.

insetad of:

assert sentiment.mean == 0.0
assert sentiment.positive = 1.0
assert sentiment.negative = -1.0

or

assert sentiment.mean == 0.0 and sentiment.positive = 1.0 and sentiment.negative = -1.0

you can write:

assert (sentiment.mean, sentiment.positive, sentiment.negative) == (0.0, 1.0, -1.0)

ALWAYS initilize like this:

model = Model(param1 = value1, param2 = value2, ...)

NOT Like this

model = Model(value1, value2)


ALWAYS use the example values of the same type as in declaration!

class Person
    age: int

Person(age = 30) not Person(age="30 yers")

Python is dynamic language but it does not mean you should test agains nonsene values!

"""


import pytest

from cro.geneea.sdk import Account, Document, Entity, Relation, Sentiment, Tag


@pytest.mark.domain
def test_tag_model_is_correctly_initialized():
    # Arrange
    unique_id, stdForm, model_type, relevance = "t0", "form", "type", 1.0

    # Act
    model = Tag(id=unique_id, type=model_type, stdForm=stdForm, relevance=1.0)
    expects = unique_id, stdForm, model_type, relevance
    current = model.id, model.stdForm, model.type, model.relevance

    # Assert
    assert expects == current


@pytest.mark.domain
def test_account_model_is_correctly_initialized():
    # Arrange
    model_type, quotas = "type", "quotas"

    # Act
    model = Account(type=model_type, remainingQuotas=quotas)
    expects = model_type, quotas
    current = model.type, model.remainingQuotas

    # Assert
    assert expects == current


@pytest.mark.domain
def test_entity_model_is_correctly_initialized():
    # Arrange
    unique_id, stdForm, model_type = "e0", "stdForm", "type"

    # Act
    model = Entity(id=unique_id, stdForm=stdForm, type=model_type)
    current = model.id, model.stdForm, model.type
    expects = unique_id, stdForm, model_type

    # Assert
    assert expects == current


@pytest.mark.domain
def test_sentiment_model_is_correctly_initialized():
    # Arrange
    mean, positive, negative, label = 0.0, 1.0, -1.0, "neutral"

    # Act
    model = Sentiment(mean=mean, positive=positive, negative=negative, label=label)
    expects = mean, positive, negative, label
    current = model.mean, model.positive, model.negative, model.label

    # Assert
    assert expects == current


@pytest.mark.domain
def test_relation_model_is_correctly_initialized():
    # Arrange
    unique_id, name, textRepr, model_type, args = (
        "id_data",
        "name_data",
        "textRepr_data",
        "type_data",
        ["args_data", "args_data"],
    )

    # Act
    model = Relation(
        id=unique_id, type=model_type, textRepr=textRepr, name=name, args=args
    )

    expects = unique_id, model_type, textRepr, name, args
    current = model.id, model.type, model.textRepr, model.name, model.args

    # Assert
    assert expects == current


def analysis_fake():
    return Analysis(
        original="Populární známka se prodávala na jediném místě v centru Kyjeva, kde na ni každý den čekaly stovky lidí. Mezitím se arch šesti známek prodává na inzertních serverech za více než 10 tisíc korun.\n",
        analyzed={
            "version": "3.2.1",
            "language": {"detected": "cs"},
            "entities": [
                {"id": "e0", "stdForm": "P1D", "type": "set"},
                {"id": "e1", "stdForm": "10", "type": "number"},
                {"id": "e2", "stdForm": "Kyjev", "type": "location"},
            ],
            "tags": [
                {"id": "t0", "stdForm": "známka", "type": "base", "relevance": 3.917},
                {
                    "id": "t1",
                    "stdForm": "inzertní server",
                    "type": "base",
                    "relevance": 3.0,
                },
                {
                    "id": "t2",
                    "stdForm": "centrum Kyjeva",
                    "type": "base",
                    "relevance": 2.816,
                },
                {"id": "t3", "stdForm": "arch", "type": "base", "relevance": 2.714},
                {
                    "id": "t4",
                    "stdForm": "jediné místo",
                    "type": "base",
                    "relevance": 2.703,
                },
            ],
            "relations": [
                {
                    "id": "r0",
                    "name": "prodávat",
                    "textRepr": "prodávat(známka)",
                    "type": "VERB",
                    "args": [{"type": "OBJECT", "name": "známka"}],
                    "feats": {"negated": "false", "modality": ""},
                },
                {
                    "id": "r1",
                    "name": "čekat",
                    "textRepr": "čekat(stovka)",
                    "type": "VERB",
                    "args": [{"type": "SUBJECT", "name": "stovka"}],
                    "feats": {"negated": "false", "modality": ""},
                },
                {
                    "id": "r2",
                    "name": "každý",
                    "textRepr": "každý(den)",
                    "type": "ATTR",
                    "args": [{"type": "SUBJECT", "name": "den"}],
                    "feats": {"negated": "false", "modality": ""},
                },
                {
                    "id": "r3",
                    "name": "populární",
                    "textRepr": "populární(známka)",
                    "type": "ATTR",
                    "args": [{"type": "SUBJECT", "name": "známka"}],
                    "feats": {"negated": "false", "modality": ""},
                },
                {
                    "id": "r4",
                    "name": "jediný",
                    "textRepr": "jediný(místo)",
                    "type": "ATTR",
                    "args": [{"type": "SUBJECT", "name": "místo"}],
                    "feats": {"negated": "false", "modality": ""},
                },
                {
                    "id": "r5",
                    "name": "prodávat",
                    "textRepr": "prodávat(arch)",
                    "type": "VERB",
                    "args": [{"type": "OBJECT", "name": "arch"}],
                    "feats": {"negated": "false", "modality": ""},
                },
                {
                    "id": "r6",
                    "name": "inzertní",
                    "textRepr": "inzertní(server)",
                    "type": "ATTR",
                    "args": [{"type": "SUBJECT", "name": "server"}],
                    "feats": {"negated": "false", "modality": ""},
                },
            ],
            "docSentiment": {
                "mean": 0.0,
                "label": "neutral",
                "positive": 0.0,
                "negative": 0.0,
            },
            "usedChars": 193,
        },
    )


@pytest.mark.skip
@pytest.mark.domain
def test_analysis_version():
    assert False

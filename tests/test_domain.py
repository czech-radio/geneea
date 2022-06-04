# -*- coding: utf-8 -*-


import pytest

from cro.geneea.sdk._domain import Account, Analysis, Entity, Relation, Sentiment, Tag


@pytest.mark.domain
def test_tag_model():
    assert Tag("id_data", "stdForm_data", "type_data", "relevance_data") is not None


@pytest.mark.domain
def test_account_model():
    assert Account("type", "remainingQuotas") is not None


@pytest.mark.domain
def test_entity_model():
    assert Entity("id_data", "stdForm_data", "type_data") is not None


@pytest.mark.domain
def test_sentiment_model():
    assert Sentiment("mean_data", "label_data", "1.0", "-0.0") is not None


@pytest.mark.domain
def test_relation_mmodel():
    assert (
        Relation(
            "id_data",
            "name_data",
            "textRepr_data",
            "type_data",
            ["args_data", "args_data"],
        )
        is not None
    )


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


@pytest.mark.domain
def test_analysis_model_version():
    ...

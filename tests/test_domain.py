# -*- coding: utf-8 -*-


import pytest

from cro.geneea._domain import Analysis, Entity, Sentiment, Relation, Tag


@pytest.mark.domain
def test_text_model():
    assert (
        Analysis(original="Toto je testovací věta", analyzed={"test": "test"})
        is not None
    )


def test_entity():
    assert Entity("id_data", "stdForm_data", "type_data") is not None


def test_sentiment():
    assert Sentiment("mean_data", "label_data", "1.0", "-0.0") is not None


def test_relation():
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


def test_tag():
    assert Tag("id_data", "stdForm_data", "type_data", "relevance_data") is not None

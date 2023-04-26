# -*- coding: utf-8 -*-


"""
The integration tests for :class:`Client`.
"""

import os

import pytest

from cro.geneea import Account, Client, Document, Entity, Relation, Sentiment, Tag

TEST_FILES_PATH = "docs/examples/input.txt"


@pytest.fixture
def client():
    key = os.environ.get("GENEEA_API_KEY")
    return Client(key=key)


@pytest.fixture
def phrases():
    with open(TEST_FILES_PATH, encoding="utf8") as file:
        phrases = "\n".join(file.readlines())
    return phrases


@pytest.mark.client
def test_that_client_fetches_analysis(client, phrases):
    result: Document = client.get_analysis(phrases)
    assert result.paragraphs is not None
    assert len(result) > 0


@pytest.mark.client
def test_that_client_fetches_entities(client, phrases):
    result: tuple[Entity] = client.get_entities(phrases)
    assert len(result) > 0


@pytest.mark.client
def test_that_client_fetches_sentiment(client):
    result: Sentiment = client.get_sentiment("Hodně mě nebavi mluvit.")
    assert result.label == "negative"


@pytest.mark.client
def test_that_client_fetches_tags(client, phrases):
    result: tuple[Tag] = client.get_tags(phrases)
    assert len(result) > 0


@pytest.mark.client
def test_that_client_fetches_relations(client, phrases):
    result: tuple[Relation] = client.get_relations(phrases)
    assert len(result) > 0


@pytest.mark.skip
@pytest.mark.client
def test_that_client_fetches_account(client):
    result: Account = client.get_account()
    assert result is not None


@pytest.mark.skip
@pytest.mark.client
def test_that_client_fetches_status(client):
    result: Account = client.get_status()
    assert result is not None

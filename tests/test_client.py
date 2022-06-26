# -*- coding: utf-8 -*-


import os

import dotenv
import pytest

from cro.geneea.sdk import Account, Analysis, Client, Entity, Relation, Sentiment, Tag


@pytest.fixture
def client():
    key = os.environ.get("GENEEA_API_KEY")
    return Client(key=key)


@pytest.fixture
def phrases():
    with open("docs/examples/input.txt", encoding="utf8") as file:
        phrases = "\n".join(file.readlines())
    return phrases


@pytest.mark.client
def test_that_client_fetches_analysis(client, phrases):
    result: Analysis = client.get_analysis(phrases)
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
    result: tuple[Ralation] = client.get_relations(phrases)
    assert len(result) > 0


@pytest.mark.skip
@pytest.mark.client
def test_that_client_fetches_account(client):
    result: Account = client.get_account()
    assert result is not None

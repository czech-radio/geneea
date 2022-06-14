# -*- coding: utf-8 -*-


import os

import pytest

from cro.geneea.sdk import Client, Entity, Sentiment, Analysis


@pytest.fixture
def client():
    return Client(key=os.environ.get("GENEEA_API_KEY"))


@pytest.fixture
def phrases():
    with open("data/input.txt", encoding="utf8") as file:
        phrases = "\n".join(file.readlines())
    return phrases


@pytest.mark.client
def test_that_client_fetches_analysis(client, phrases):
    result: Analysis = client.get_analysis(phrases)
    assert result.paragraphs is not None
    assert len(result) > 0


@pytest.mark.client
def test_that_client_fetches_entities(client, phrases):
    result = client.get_entities(phrases)
    assert len(result) > 0


@pytest.mark.client
def test_that_client_fetches_sentiment(client):
    result: Sentiment = client.get_sentiment("hodne me nebavi mluvit")
    assert result.label == "negative"


@pytest.mark.client
def test_that_client_fetches_tags(client, phrases):
    result = client.get_tags(phrases)
    assert len(result) > 0


@pytest.mark.client
def test_that_client_fetches_relations(client, phrases):
    result = client.get_relations(phrases)
    assert len(result) > 0


@pytest.mark.client
def test_that_client_fetches_account(client):
    result = client.get_account()
    assert result is not None

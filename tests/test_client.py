# -*- coding: utf-8 -*-


import os

import pytest

from cro.geneea.sdk import Client, Entity, Sentiment


@pytest.fixture
def client():
    return Client(key=os.environ.get("GENEEA_API_KEY"))


@pytest.fixture
def phrases():
    return "\n".join(Client.read_phrases("data/input.txt"))


@pytest.mark.client
def test_that_client_fetches_analysis(client, phrases):
    result = client.get_analysis(phrases)
    print(result)
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

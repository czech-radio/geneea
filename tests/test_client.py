# -*- coding: utf-8 -*-


import os
import logging
import xml.etree.cElementTree as ET
import xml.dom.minidom


import pytest

from cro.geneea.sdk import Client, Sentiment
from cro.geneea.sdk._domain import Entity


@pytest.fixture
def client():
    KEY = os.environ.get("GENEEA_API_KEY")
    _client = Client(key=KEY)
    assert _client.key is not None
    return _client


@pytest.fixture
def phrases():
    return "\n".join(Client.read_phrases("data/input.txt"))


@pytest.mark.client
def test_client():
    assert Client(key=None) is not None


@pytest.mark.client
def test_that_client_return_analysis(client, phrases):
    result = client.get_analysis(phrases)
    assert len(result) > 0


@pytest.mark.client
def test_that_client_return_entities(client, phrases):
    result = client.get_entities(phrases)
    assert len(result) > 0


@pytest.mark.client
def test_that_client_return_sentiment(client):
    result: Sentiment = client.get_sentiment("hodne me nebavi mluvit")
    assert result.label == "negative"


@pytest.mark.client
def test_that_client_return_tags(client, phrases):
    result = client.get_tags(phrases)
    assert len(result) > 0


@pytest.mark.client
def test_that_client_return_relations(client, phrases):
    result = client.get_relations(phrases)
    assert len(result) > 0


@pytest.mark.client
def test_that_client_returns_account(client):
    result = client.get_account()
    assert result is not None

    
@pytest.mark.client
def test_that_xml_prettyfier_works(client):
    root = ET.Element("root")
    ET.SubElement(root, "test_write", write="ok").text = "True"

    ok_write = client.pretty_print_xml_given_root(root, "data/test_write_0.xml")
    assert ok_write is True

    
@pytest.mark.client
def test_that_client_writes_file(client):
    test_tuple = tuple(
        [Entity("e0", "test", "is ok"), Entity("e1", "test", "is also ok")]
    )
    ok_write = client.write_tuple_to_XML(test_tuple, "data/test_write_1.xml")
    assert ok_write is True


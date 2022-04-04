# -*- coding: utf8 -*-


import pytest


@pytest.mark.domain
def test_model():
    from cro.geneea._domain import Datamodel

    assert Datamodel('{"text": "Toto je testovací věta"}') is not None

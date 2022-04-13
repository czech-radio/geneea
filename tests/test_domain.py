# -*- coding: utf-8 -*-


import pytest

from cro.geneea._domain import Model


@pytest.mark.domain
def test_text_model():
    assert (
        Model(original="Toto je testovací věta", analyzed={"test": "test"}) is not None
    )

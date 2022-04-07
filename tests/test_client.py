# -*- coding: utf-8 -*-

import pytest

from cro.geneea import Client


@pytest.mark.client
def test_client():
    assert Client(key=None) is not None


import pytest


@pytest.mark.domain
def test_model():
    from cro.geneea._datamodel import Datamodel
    assert Datamodel(None) is not None
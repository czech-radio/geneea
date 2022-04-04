import pytest

from cro.geneea import __version__, Client

"""
Package tests
-------------
Test the project as a package e.g. check the version, style etc.
"""


@pytest.mark.client
def test_client():
    assert Client(key=None) is not None


def test_version():
    assert __version__ == "0.1.0"

# -*- coding: utf-8 -*-

"""
Test the project as a package e.g. check the version, style etc.
"""

import pytest

from cro.geneea.sdk import __version__


@pytest.mark.package
def test_version():
    assert __version__ == "0.5.0"

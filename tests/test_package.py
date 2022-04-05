# -*- coding: utf8 -*-

"""
Test the project as a package e.g. check the version, style etc.
"""

import pytest

from cro.geneea import __version__


def test_version():
    assert __version__ == "0.1.0"

# -*- coding: utf-8 -*-

"""
Test the project as a package e.g. check the version, style etc.
"""

import pytest

from cro.geneea.sdk import __version__


def test_version():
    assert __version__ == "0.2.0"

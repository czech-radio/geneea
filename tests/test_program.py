# -*- coding: utf-8 -*-

"""
The simple tests of command line interface.
"""

import os

import pytest


@pytest.mark.package
def test_geneea_program_entrypoint():
    exit_status = os.system("cro.geneea --help")
    assert exit_status == 0

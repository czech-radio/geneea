# -*- coding: utf-8 -*-

import os

"""
The simple tests of command line interface.
"""


def test_geneea_program_entrypoint():
    exit_status = os.system("cro.geneea --help")
    assert exit_status == 0

# -*- coding: utf-8 -*-

import argparse

from cro.geneea._client import Client as GeneeaClient

"""
The command line interface.
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", required=True, type=str, help="source filename")

    args = parser.parse_args()

    client = GeneeaClient()

    result = client.analyze("Toto je testovací věta!")

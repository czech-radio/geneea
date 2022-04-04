# -*- coding: utf-8 -*-

import argparse
import os

from cro.geneea._client import Client as GeneeaClient

"""
The command line interface.
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", required=True, type=str, help="source filename")

    args = parser.parse_args()

    KEY = os.environ.get("GENEEA_API_KEY")

    client = GeneeaClient(key=KEY)

    result = client.analyze("Toto je testovací věta!")

    print(result)

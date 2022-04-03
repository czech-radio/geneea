# -*- coding: utf-8 -*-

import argparse

from _client import Client as GeneeaClient

"""
The command line interface.
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", required=True, type=str, help="source filename")

    args = parser.parse_args()

    print(f"Geneea API hello {args.file}")

    client = GeneeaClient(args.file)

    # TODO arguments = parser.parse_args()

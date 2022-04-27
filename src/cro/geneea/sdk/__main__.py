# -*- coding: utf-8 -*-

"""
The command line interface.
"""


import os, sys
import argparse

from cro.geneea.sdk import Analysis, Client


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", required=True, type=str, help="The file name")

    parser.add_argument(
        "-t", "--type", required=True, type=str, help="The operation type"
    )

    args = parser.parse_args()

    KEY = os.environ.get("GENEEA_API_KEY")

    client = Client(key=KEY)

    text = "\n".join(Client.read_phrases(args.file))

    print(f"{args.type.upper()}\n{len(args.type) * '-'}")

    match args.type:

        case "analysis":
            result = client.get_analysis(text)
            print(result)

        case "account":
            result = client.get_account()
            print(result)

        case "entities":
            result = client.get_entities(text)
            print(result)

        case "tags":
            result = client.get_tags(text)
            print(result)

        case "sentiment":
            result = client.get_sentiment(text)
            print(result)

        case "relations":
            result = client.get_relations(text)
            print(result)

        case _:
            print(
                "Choose one of the following type: 'analysis', 'account', 'entities', 'tags', 'sentiment', 'relations', 'table'"
            )

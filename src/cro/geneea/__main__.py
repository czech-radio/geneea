# -*- coding: utf-8 -*-

"""
The command line interface.
"""


import argparse
import os

from cro.geneea import Client as GeneeaClient
from cro.geneea import Text as Text


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, type=str, help="The file name")
    parser.add_argument(
        "-t", "--type", required=True, type=str, help="The operation type"
    )

    args = parser.parse_args()

    KEY = os.environ.get("GENEEA_API_KEY")

    client = GeneeaClient(key=KEY)

    text = "\n".join(GeneeaClient.read_phrases(args.file))

    print(f"{args.type.upper()}\n{len(args.type) * '-'}")

    match args.type:

        case "analysis":
            result = client.get_analysis(text)
            print(result)
            text = Text(text, result)

        case "account":
            result = client.get_account()
            print(result)

        case "entities":
            result = client.get_entities(text)
            text = Text(text, result)
            print(text.entities())

        case "tags":
            result = client.get_tags(text)
            text = Text(text, result)
            print(text.tags())
        case "sentiment":
            result = client.get_sentiment(text)
            text = Text(text, result)
            print(text.sentiment())
        case "relations":
            result = client.get_relations(text)
            text = Text(text, result)
            print(text.relations())
        case _:
            print(
                "Choose one of the following type: 'analysis', 'account', 'entities', 'tags', 'sentiment', 'relations'"
            )

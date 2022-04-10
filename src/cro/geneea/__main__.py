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

    match args.type:

        case "analysis":
            # ANALYSIS
            print("\nANALYSIS\n--------")
            result = client.get_analysis(text)
            print(result)
            text = Text(text, result)

        case "account":
            # ACCOUNT
            print("ACCOUNT\n--------")
            result = client.get_account()
            print(result)
        case "entities":
            # ENTITIES
            print("ENTITIES\n--------")
            result = client.get_entities(text)
            text = Text(text, result)
            print(text.entities())
        case "tags":
            # TAGS
            print("TAGS\n--------")
            result = client.get_tags(text)
            text = Text(text, result)
            print(text.tags())
        case "sentiment":
            # SENTIMENT
            print("SENTIMENT\n--------")
            result = client.get_sentiment(text)
            text = Text(text, result)
            print(text.sentiment())
        case "relations":
            # REALATION
            print("RELATIONS\n--------")
            result = client.get_relations(text)
            text = Text(text, result)
            print(text.relations())
        case _:
            print(
                "Choose one of the following type: 'analysis', 'account', 'entities', 'tags', 'sentiment', 'relations'"
            )

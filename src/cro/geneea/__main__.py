# -*- coding: utf-8 -*-

"""
The command line interface.
"""


import argparse
import os

from cro.geneea import Client
from cro.geneea import Model


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
            model = Model(text, result)
            print(model.analysis())

        case "account":
            result = client.get_account()
            print(result)

        case "entities":
            result = client.get_entities(text)
            model = Model(text, result)
            print(model.entities())

        case "tags":
            result = client.get_tags(text)
            model = Model(text, result)
            print(model.tags())

        case "sentiment":
            result = client.get_sentiment(text)
            model = Model(text, result)
            print(model.sentiment())

        case "relations":
            result = client.get_relations(text)
            model = Model(text, result)
            print(model.relations())

        case "table":
            result = client.get_entities(text)
            model = Model(text, result)
            df = model.to_table(model.entities())
            print(df)

        case _:
            print(
                "Choose one of the following type: 'analysis', 'account', 'entities', 'tags', 'sentiment', 'relations', 'table'"
            )

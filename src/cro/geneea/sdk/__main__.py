# -*- coding: utf-8 -*-

"""
The command line interface.
"""


import argparse
import os, sys

from cro.geneea.sdk import Client


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", required=True, type=str, help="The file name")

    parser.add_argument(
        "-t", "--type", required=True, type=str, help="The operation type"
    )

    parser.add_argument(
        "-x",
        "--xml",
        required=False,
        action="store_true",
        help="[Optional] Output a XML file",
    )

    args = parser.parse_args()

    KEY = os.environ.get("GENEEA_API_KEY")

    client = Client(key=KEY)

    #    incoming = sys.stdin.readlines()
    #    if (incoming != 'null') {
    #        print(f"test incoming: {incoming}")
    #    }

    text = "\n".join(Client.read_phrases(args.file))

    print(f"{args.type.upper()}\n{len(args.type) * '-'}")

    match args.type:

        case "analysis":
            result = client.get_analysis(text)

            if args.xml != None:
                client.write_full_analysis_to_XML(
                    result,
                    f"{args.file[0:args.file.index('.')]}_{args.type.lower()}.xml",
                )

            print(result)

        case "account":
            result = client.get_account()
            print(result)

        case "entities":
            result = client.get_entities(text)

            if args.xml != None:
                client.write_tuple_to_XML(
                    result,
                    f"{args.file[0:args.file.index('.')]}_{args.type.lower()}.xml",
                )

            print(result)

        case "tags":
            result = client.get_tags(text)

            if args.xml != None:
                client.write_tuple_to_XML(
                    result,
                    f"{args.file[0:args.file.index('.')]}_{args.type.lower()}.xml",
                )

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

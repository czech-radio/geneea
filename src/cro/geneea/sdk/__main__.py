# -*- coding: utf-8 -*-

"""
The command line interface.
"""

import argparse
import os
import sys

import dotenv

from cro.geneea.sdk import Client


def read_args():
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", required=True, type=str, help="Input filename")

    parser.add_argument(
        "-t", "--type", required=True, type=str, help="The operation type"
    )

    parser.add_argument(
        "-f",
        "--format",
        required=True,
        type=str,
        help="[Optional] type of an output file, allowed types xml, json or csv",
    )

    result = parser.parse_args()

    return result


def read_envs() -> dict:
    """
    Reads the needed environment variables.
    """
    dotenv.load_dotenv()

    geneea_api_key = os.getenv("GENEEA_API_KEY")

    if geneea_api_key is None:
        raise ValueError(
            """Please set GEENEA_API_KEY environment variable.
            Alternatively write it to the .env  file and place it to the root folder."""
        )

    return {"GENEEA_API_KEY": os.environ.get("GENEEA_API_KEY")}


def main():

    args = read_args()
    envs = read_envs()

    client = Client(key=envs["GENEEA_API_KEY"])

    with open(args.input, encoding="utf8") as file:
        text = "\n".join(file.readlines())

    # print(f"{args.type.upper()}\n{len(args.type) * '-'}")

    match args.format:
        case None:
            format = "xml"
        case "csv" | "xml" | "json":
            format = args.format.lower()
        case _:
            print("The allowed format is ('xml', 'json', 'csv').")
            sys.exit(1)

    match args.type:
        case "analysis":
            result = client.get_analysis(text)
            result = client.serialize(result, format)
            print(result)
            # vs write to file with name = f"{args.input[0:args.input.index('.')]}_{args.type.lower()}.xml",

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
                "Choose one of the following type: 'analysis', 'account', 'entities', 'tags', 'sentiment', 'relations'."
            )

import os
import sys
import json

from requests import post

from cro.geneea._datamodel import Datamodel


__API_KEY__ = os.environ.get("GENEEA_API_KEY")

class Client:
    """
    Geneea API Client
    """

    __URL__ = "https://api.geneea.com/v3"


    def __init__(self):
        """
        Please FIX this.
        """

    @classmethod
    def get_txt(cls, file_name):
        raw = ""
        print("Processing file: ", file_name)
        with open(file_name, encoding="utf8") as file:
            line = file.readline()
            while line:
                line = file.readline()
                raw = raw + line
        return raw

    @classmethod
    def analyze(cls, _input) -> str:
        """
        Analyze a given text.
        """
        try:
            print(f"Connecting to {cls.__URL__} using key {__API_KEY__}")

            text = {"text": f"{_input}"}

            headers = {
                "content-type": "application/json",
                "Authorization": f"user_key {__API_KEY__}",
            }

            data = post(f"{cls.__URL__}/analysis", json = text, headers = headers).json()
            return json.dumps(data)
        except Exception as ex:
            e = sys.exc_info()[0]
            print("Connection error: ", e)
            raise


    @classmethod
    def deserialize(cls, input):
        """
        todo json to datamodel
        """
        datamodel = Datamodel(input)

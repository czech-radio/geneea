import datetime as dt
import json
import os
from enum import Enum

from requests import post as POST

from cro.geneea._datamodel import Datamodel

__API_KEY__ = os.environ.get("GENEEA_API_KEY")
__API_URL__ = os.environ.get("GENEEA_API_URL")


class Client:

    """
    Geneea API Client
    """

    def __init__(self, _filename):
        filename = _filename
        text = self.get_txt(filename)
        response = self.callGeneea(text)
        self.deserialize(response)

    @classmethod
    def get_txt(a, _filename):
        raw = ""
        print("processing file: ", _filename)
        with open(_filename, encoding="utf8") as f:
            line = f.readline()
            while line:
                line = f.readline()
                raw = raw + line
        return raw

    @classmethod
    def callGeneea(self, _input) -> str:
        """
        get response from a server
        """
        url = f"{__API_URL__}"
        date_format = f"%Y-%m-%d"
        headers = {
            "content-type": "application/json",
            "Authorization": f"user_key {__API_KEY__}",
        }
        text = {"text": f"{_input}"}
        print(f"connecting to {__API_URL__} using key {__API_KEY__}")
        data = []
        try:
            data = POST(url, json=text, headers=headers).json()
            print("OK")
        except:
            e = sys.exc_info()[0]
            print("connection error: ", e)

        return json.dumps(data)

    @classmethod
    def deserialize(self, _input):
        """
        todo json to datamodel
        """
        datamodel = Datamodel(_input)

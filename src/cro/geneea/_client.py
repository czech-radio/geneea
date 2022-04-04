# -*- coding: utf-8 -*-

import logging
import sys

from requests import post

from cro.geneea._datamodel import Datamodel


class Client:
    """
    Geneea API Client
    """

    __URL__ = "https://api.geneea.com/v3"

    def __init__(self, key: str):
        self._key = key

    @property
    def key(self) -> str:
        return self._key

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

    def analyze(self, input) -> str:
        """
        Analyze a given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.
        """
        try:
            headers = {
                "content-type": "application/json",
                "Authorization": f"user_key {self.key}",
            }
            data = post(
                f"{self.__URL__}/analysis", json={"text": input}, headers=headers
            )

            return data.json()

        except Exception as ex:
            logging.error(f"Connection error {ex}")
            raise ex

    @classmethod
    def deserialize(cls, input: dict) -> Datamodel:
        """
        TODO Convert JSON to model.
        """
        return Datamodel(input)

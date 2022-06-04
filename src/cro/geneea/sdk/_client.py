# -*- coding: utf-8 -*-


"""
Contains a client implementing the SDK features.
"""


import logging
import os
from os import PathLike
from typing import Optional

from requests import post

from cro.geneea.sdk._domain import Account, Analysis, Entity, Relation, Sentiment, Tag

__all__ = tuple(["Client"])


LOGGER = logging.getLogger(__name__)
TIMEOUT = 300.05  # The HTTP connection timeout.


class Client:
    """
    Geneea REST API client for https://api.geneea.com/

    base url: https://api.geneea.com/api-docs

    See example JSON output in project `data` folder.

    Possible errors e.g.:
    {'exception': 'Exception', 'message': 'The requested resource is not available.'}


    201 	Created
    401 	Unauthorized
    403 	Forbidden
    404 	Not Found

    """

    __URL__: str = "https://api.geneea.com/"

    def __init__(self, key: str) -> None:
        """
        Create a new client with the given secret key.

        :param key: The secret access key.
        """
        self._key = key
        self._headers = {
            "content-type": "application/json",
            "Authorization": f"user_key {self._key}",
        }

    def __eq__(self, that) -> bool:
        return isinstance(that, type(self)) and self.key == that.key

    def __hash__(self) -> int:
        return hash((type(self), self.key))

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, value: str) -> None:
        self._key = value

    @property
    def headers(self):
        return self._headers

    @classmethod
    def read_phrases(cls, file_path: PathLike, encoding: str = "utf8") -> list[str]:
        """
        The helper method to load phrases from the file.
        We assume that each phrase is  placed on separate line.

        :param file_path: The file path.
        :param encoding: The file content encoding.
        :return: The list of phrases.
        :raises: OSError: If the file cannot be opened.
        """
        with open(file_path, encoding=encoding) as file:
            return file.readlines()

    # Serialization helpers.

    @classmethod
    def serialize(cls, model: Analysis, format: str) -> Optional[str]:
        result = None

        match format:
            case "xml":
                result = model.to_xml()
            case "json":
                result = model.to_json()

        return result

    def _post(self, endpoint, data=None) -> None:
        try:
            response = post(
                f"{self.__URL__}/v3/{endpoint}",
                json={"text": data, "params": ["paragraphs"]},
                headers=self.headers,
                timeout=TIMEOUT,
            )
            logging.info(response.status_code)

            # @todo Check status code.

            result = Analysis(original=data, analyzed=response.json())

            return result

        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_status(self) -> str:
        return NotImplemented

    def get_tags(self, text: str) -> tuple[Tag]:
        """
        Get tags for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.
        """
        return self._post("tags", data=text).tags

    def get_account(self) -> Account:
        """
        Get account information.
        :return: Account object
        """
        return self._post("account", data="\n").account

    def get_entities(self, text: str) -> tuple[Entity]:
        """
        Get entites for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.
        """
        return self._post("entities", data=text).entities

    def get_sentiment(self, text: str) -> Sentiment:
        return self._post("sentiment", data=text).sentiment

    def get_relations(self, text: str) -> tuple[Relation]:
        return self._post("relations", data=text).relations

    def get_analysis(self, text: str) -> Analysis:
        """
        Get analysis for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.
        """
        return self._post("analysis", data=text)

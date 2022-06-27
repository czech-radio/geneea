# -*- coding: utf-8 -*-


"""
Contains a client implementing the SDK features.
"""


import logging
import os
from os import PathLike
from typing import Optional

import dotenv
from requests import post

from cro.geneea.sdk._domain import Account, Document, Entity, Relation, Sentiment, Tag

__all__ = tuple(["Client"])


LOGGER = logging.getLogger(__name__)


class ClientException(Exception):
    """
    Raises when the client error occures.
    """


class Client:
    """
    The simple but effective *Geneea NLP v3 service* client.

    See the example `json`/`xml` output files in `/docs/examples/` directory.

    NOTE: [
        POST request status codes
        201    Created
        401    Unauthorized
        403    Forbidden
        404    Not Found
    ]

    NOTE: [
      Consider change URL to "https://api.geneea.com/v3/analysis/T:CRo-transcripts".
      This URL uses the special model trained for our (Czech Radi) purpose e.g better political
      parties recognition.
    ]
    """

    def __init__(self, key: str) -> None:
        """
        Create a new client with the given private Geneea API key.

        :param key: The private Geneea API key.
        """
        self._key = key
        self._url = "https://api.geneea.com/"
        self._timeout = (3, 30)  # The connection and read timeout in seconds.
        self._headers = {
            "Accept": "application/json; charset=UTF-8",
            "Authorization": f"user_key {self._key}",
            "Content-Type": "application/json; charset=UTF-8",
        }

    def __eq__(self, that: object) -> bool:
        """
        The client are considered equal if they have the same attributes
        (structural equality).

        :param that: The object instance.
        :return: The `True` when clients are equal otherwise `False`.
        """
        return isinstance(that, type(self)) and self.key == that.key

    def __hash__(self) -> int:
        """
        Get the object hash value.

        :return The objects hash value.
        """
        return hash((type(self), self.key))

    @property
    def key(self) -> str:
        """
        Get the service private key.

        :return: The service key value.
        """
        return self._key

    @key.setter
    def key(self, value: str) -> None:
        """
        Set the service private key.

        :param value: The service key value.
        """
        self._key = value

    @property
    def url(self) -> str:
        """
        Get the service URL.

        :return: The service URL.
        """
        return self._url

    @property
    def timeout(self) -> int:
        """
        Get the service request timeout.

        :return: The service request timeout.
        """
        return self._timeout

    @property
    def headers(self) -> dict:
        """
        Get the service request headers.

        :return: The service request headers.
        """
        return self._headers

    @classmethod
    def serialize(cls, model: Document, output_format: str) -> Optional[str]:
        """
        Serialize the model to desired output format.

        :param model: The domain model to serialize.
        :param format: The output format e.g 'xml', 'json', 'csv'.
        :return: The serialized domain model.
        :raises: ValueError: If the file format is not spuported.
        """
        result = None

        match output_format:
            case "xml":
                result: str = model.to_xml()
            case "json":
                result: str = model.to_json()
            case _:
                raise ValueError(f"Supported formats are ('xml, 'json').")

        return result

    # ################################### HELPERS #################################### #

    def _send(self, endpoint, data=None, expected_status_code: int = 200) -> None:
        """
        Send the POST request to the endpoint.

        See the methods:
        * :meth:`get_status()`
        * :meth:`get_tags()`
        etc.

        :param endpoint: The request enpoint e.g 'analysis'
        :param extected_status_code:
            The expected status code of succesfull request.
            Because some POST request are equaivalent to GET they returns 200 status
            code when succeded. Some returns 201 as written in their documenatation.
            Change it from 200 to 201 when needed (other values are not allowed).

        :raise ClientException:
        :return: The POST request result as JSON.
        """
        if expected_status_code not in (200, 201):
            raise ValueError("The expected status code is either 200 or 201.")

        try:
            response = post(
                f"{self.url}/v3/{endpoint}",
                json={"text": data, "returnMentions": "true"},
                headers=self.headers,
                timeout=self.timeout,
            )
            response.encoding = "utf-8"

            # Check status code and errors e.g.
            # {'exception': 'BadCredentialsException', 'message': 'the user key is invalid'}
            if response.status_code != expected_status_code:
                logging.info(f"{response.status_code}: {response.json()}")
                resource_info = f"; {endpoint}" if response.status_code == 404 else ""
                raise ClientException(
                    f'{response.json()["exception"]} [{response.status_code}]: {response.json()["message"]}{resource_info}'
                )

            result = Document.create(original=data, analysed=response.json())

            return result

        except Exception as ex:
            logging.error(ex)
            raise ex

    # ################################### FEATURES ################################### #

    # GENERAL

    def get_status(self) -> str:
        """
        Get the service status check.
        """
        return NotImplemented

    def get_account(self) -> Account:
        """
        Get account information.
        :return: Account object
        """
        result = self._send("account", data="\n").account
        return result

    # ANALYSIS

    def get_tags(self, text: str) -> tuple[Tag]:
        """
        Get tags for the given input text.

        :param input: The input text to analyze.
        :return The analysed input text.
        """
        result = self._send("tags", data=text).tags
        return result

    def get_entities(self, text: str) -> tuple[Entity]:
        """
        Get entites for the given input text.

        :param input: The input text to analyze.
        :return The analysed input text.
        """
        result = self._send("entities", data=text).entities
        return result

    def get_sentiment(self, text: str) -> Sentiment:
        """
        Get sentiment for the given input text.

        :param input: The input text to analyze.
        :return The analysed input text.
        """
        result = self._send("sentiment", data=text).sentiment
        return result

    def get_relations(self, text: str) -> tuple[Relation]:
        """
        Get relations for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.
        """
        result = self._send("relations", data=text).relations
        return result

    def get_analysis(self, text: str) -> Document:
        """
        Get analysis for the given input text.

        :param input: The input text to analyze.
        :return The analysed input text.
        """
        result = self._send("analysis", data=text)
        return result

# -*- coding: utf-8 -*-


import logging
from requests import get, post
from cro.geneea._domain import Model


LOG = logging.getLogger(__name__)

DEFAULT_CONNECTION_TIMEOUT = 3.05


class Client:
    """
    Geneea REST API client for https://api.geneea.com/

    See example JSON output in project `data` folder.

    Possible errors e.g.:
    {'exception': 'Exception', 'message': 'The requested resource is not available.'}
    """

    __URL__ = "https://api.geneea.com/"

    def __init__(self, key: str) -> None:
        self._key = key
        self.headers = {
            "content-type": "application/json",
            "Authorization": f"user_key {self._key}",
        }

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, value: str) -> None:
        self._key = value

    @classmethod
    def read_phrases(cls, path: str) -> list[str]:
        """
        The helper method to load phrases from file.

        Each phrase must be placed on separate line.

        """
        with open(path, encoding="utf-8") as file:
            line = file.readlines()

        return line

    def get_account(self) -> dict:
        """
        Get account information.
        """
        try:
            response = get(f"{self.__URL__}/account", headers=self.headers)
            logging.info(response.status_code)
            # @todo Check status code.
            return response.json()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_analysis(self, text: str) -> dict:
        """
        Get analysis for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.
        """
        try:
            response = post(
                f"{self.__URL__}/v3/analysis",
                json={"text": text},
                headers=self.headers,
                timeout=DEFAULT_CONNECTION_TIMEOUT,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            return response.json()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_entities(self, text: str) -> dict:
        """
        Get entites for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.
        """
        try:
            response = post(
                f"{self.__URL__}/v3/entities",
                json={"text": text},
                headers=self.headers,
                timeout=DEFAULT_CONNECTION_TIMEOUT,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            return response.json()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_tags(self, text: str) -> dict:
        """
        Get tags for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.
        """
        try:
            response = post(
                f"{self.__URL__}/v3/tags",
                json={"text": text},
                headers=self.headers,
                timeout=DEFAULT_CONNECTION_TIMEOUT,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            return response.json()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_sentiment(self, text: str) -> dict:
        """
        Get sentiment for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.
        """
        try:
            response = post(
                f"{self.__URL__}/v3/sentiment",
                json={"text": text},
                headers=self.headers,
                timeout=DEFAULT_CONNECTION_TIMEOUT,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            return response.json()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_relations(self, text: str) -> dict:
        """
        Get relations for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.
        """
        try:
            response = post(
                f"{self.__URL__}/v3/relations",
                json={"text": text},
                headers=self.headers,
                timeout=DEFAULT_CONNECTION_TIMEOUT,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            return response.json()
        except Exception as ex:
            logging.error(ex)
            raise ex

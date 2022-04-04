# -*- coding: utf-8 -*-


import logging

from requests import get, post

from cro.geneea._domain import Datamodel


class Client:
    """
    Geneea REST API client for https://api.geneea.com/

    Possible errors e.g.:
    {'exception': 'Exception', 'message': 'The requested resource is not available.'}
    """

    __URL__ = "https://api.geneea.com/"

    def __init__(self, key: str) -> None:
        self._key = key
        self.headers = {
            "content-type": "application/json",
            "Authorization": f"user_key {self.key}",
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
        with open(path, encoding="utf8") as file:
            return file.readlines()

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

    def get_analysis(self, input) -> dict:
        """
        get analysis for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.

        See example JSON output in `data` folder.
        """
        try:
            response = post(
                f"{self.__URL__}/v3/analysis",
                json={"text": input},
                headers=self.headers,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            return response.json()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_entities(self, input) -> dict:
        """
        Get entites for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.

        See example JSON output in `data` folder.
        """
        try:
            response = post(
                f"{self.__URL__}/v3/entities",
                json={"text": input},
                headers=self.headers,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            return response.json()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_tags(self, input) -> dict:
        """
        Get tags for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.

        See example JSON output in `data` folder.
        """
        try:
            response = post(
                f"{self.__URL__}/v3/tags", json={"text": input}, headers=self.headers
            )
            logging.info(response.status_code)
            # @todo Check status code.
            return response.json()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_sentiment(self, input) -> dict:
        """
        Get sentiment for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.

        See example JSON output in `data` folder.
        """
        try:
            response = post(
                f"{self.__URL__}/v3/sentiment",
                json={"text": input},
                headers=self.headers,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            return response.json()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_relations(self, input) -> dict:
        """
        Get relation for the given input text.

        :param input: The input text to analyze.
        :return The analyzed input text.

        See example JSON output in `data` folder.
        """
        try:
            response = post(
                f"{self.__URL__}/v3/relations",
                json={"text": input},
                headers=self.headers,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            return response.json()
        except Exception as ex:
            logging.error(ex)
            raise ex

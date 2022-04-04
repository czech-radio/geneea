# -*- coding: utf-8 -*-


import logging

from requests import get, post

from cro.geneea._datamodel import Datamodel


class Client:
    """
    Geneea REST API client for https://api.geneea.com/

    Errors e.g.:
    {'exception': 'Exception', 'message': 'The requested resource is not available.'}
    """

    __URL__ = "https://api.geneea.com/"

    def __init__(self, key: str):
        self._key = key
        self.headers = {
            "content-type": "application/json",
            "Authorization": f"user_key {self.key}",
        }

    @property
    def key(self) -> str:
        return self._key

    @classmethod
    def read_phrases(cls, path) -> list[str]:
        with open(path, encoding="utf8") as file:
            lines = file.readlines()
            return lines

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

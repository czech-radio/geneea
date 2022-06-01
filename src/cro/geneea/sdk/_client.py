# -*- coding: utf-8 -*-

import logging
import xml.etree.cElementTree as ET
import xml.dom.minidom
import os
import json

from os import PathLike

from requests import get, post

from cro.geneea.sdk._domain import Analysis, Entity, Relation, Sentiment, Tag, Account

__all__ = tuple(["Client"])

LOGGER = logging.getLogger(__name__)
TIMEOUT = 300.05  # The HTTP connection timeout.


class Client:
    """
    Geneea REST API client for https://api.geneea.com/

    See example JSON output in project `data` folder.

    Possible errors e.g.:
    {'exception': 'Exception', 'message': 'The requested resource is not available.'}
    """

    __URL__ = "https://api.geneea.com/"

    def __init__(self, key: str) -> None:
        """
        Create a new client instance with the given secret key.
        :param key: The secret access key.
        """
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
    def read_phrases(cls, path: PathLike) -> list[str]:
        """
        The helper method to load phrases from the file.

        Each phrase must be placed on separate line.
        We assume that the file is encoded as UTF-8.
        :param path: str of a path to textfile
        :return: readlines as txt
        :raises: todo
        """
        with open(path, encoding="utf-8") as file:
            return file.readlines()

    def pretty_print_xml_given_root(self, root, output_xml: str) -> bool:
        """
        Produces pretty XML file
        """
        xml_string = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
        xml_string = os.linesep.join(
            [s for s in xml_string.splitlines() if s.strip()]
        )  # remove the weird newline issue
        try:
            with open(output_xml, "w") as file_out:
                file_out.write(xml_string)
            return True
        except:
            print("Error saving file")
            return False

    def write_tuple_to_XML(self, input_tuple: tuple[object], filename: str) -> bool:
        """
        Writes XML from given tuple of Model objects
        """
        root = ET.Element("root")
        doc = ET.SubElement(root, "doc")

        for obj in input_tuple:
            ET.SubElement(
                doc, f"{type(obj).__name__}", id=f"{obj.id}"
            ).text = f"{obj.stdForm}"

        # tree = ET.ElementTree(root)

        result = self.pretty_print_xml_given_root(root, filename)
        return result

    def write_full_analysis_to_XML(self, _analysis: tuple, filename: str) -> bool:
        """
        Writes XML from given tuple of Model objects
        """
        root = ET.Element("root")
        doc = ET.SubElement(root, "doc")

        analysis = ET.SubElement(doc, "Analysis")
        ET.SubElement(
            analysis, "Fulltext", source_text_length=f"{len(_analysis[0])}"
        ).text = _analysis[0]

        ### Add Entities to XML tree
        entities = ET.SubElement(analysis, "Entities")
        for obj in _analysis[1]:
            ET.SubElement(
                entities, "Entity", id=f"{obj.id}", type=f"{obj.type}"
            ).text = f"{obj.stdForm}"

        ### Add Tags to XML tree
        tags = ET.SubElement(analysis, "Tags")
        for obj in _analysis[2]:
            ET.SubElement(
                tags, "Tag", id=f"{obj.id}", relevance=f"{obj.relevance}"
            ).text = f"{obj.stdForm}"

        ### Add Sentiment object to XML tree
        sentiment = ET.SubElement(analysis, "Sentiment")
        obj = _analysis[3]
        ET.SubElement(
            sentiment,
            "Sentiment",
            mean=f"{obj.mean}",
            positive=f"{obj.positive}",
            negative=f"{obj.negative}",
        ).text = f"{obj.label}"

        ### Add Relations to XML tree
        relations = ET.SubElement(analysis, "Relations")
        for obj in _analysis[4]:
            ET.SubElement(
                relations,
                "Relations",
                id=f"{obj.id}",
                textRepr=f"{obj.textRepr}",
                type=f"{obj.type}",
            ).text = f"{obj.name}"

        # tree = ET.ElementTree(root)

        result = self.pretty_print_xml_given_root(root, filename)
        return result

    def write_full_analysis_to_JSON(self, _analysis: tuple, filename: str) -> bool:
        text = _analysis[0]
        entities = _analysis[1]
        tags = _analysis[2]
        sentiment = _analysis[3]
        relations = _analysis[4]

        data = {
            "text": text,
            "entities": [entity.to_json() for entity in entities],
            "tags": [tag.to_json() for tag in tags],
            "sentiment": sentiment.to_json(),
            "relations": [relation.to_json() for relation in relations],
        }

        sucess = False

        try:
            with open(filename, "w") as file:
                json.dump(data, file)
            success = True
        except Exception as ex:
            logging.error(ex)

        return sucess

    def get_account(self) -> Account:
        """
        Get account information.
        :return: Account object
        """
        try:
            response = get(f"{self.__URL__}/account", headers=self.headers)
            logging.info(response.status_code)
            # @todo Check status code.
            data = response.json()
            model = Analysis("\n", data)
            return model.account()

        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_analysis(self, text: str) -> Analysis:
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
                timeout=TIMEOUT,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            data = response.json()
            model = Analysis(text, data)
            return model.analysis()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_entities(self, text: str) -> tuple[Entity]:
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
                timeout=TIMEOUT,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            data = response.json()
            model = Analysis(text, data)
            return model.entities()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_tags(self, text: str) -> tuple[Tag]:
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
                timeout=TIMEOUT,
            )
            logging.info(response.status_code)
            # @todo Check status code.
            data = response.json()
            model = Analysis(text, data)
            return model.tags()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_sentiment(self, text: str) -> Sentiment:
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
                timeout=TIMEOUT,
            )

            logging.info(response.status_code)

            # Check the status code.
            if response.status_code != 200:
                raise ValueError(f"Failure: {response.status_code} code")

            data = response.json()
            model = Analysis(text, data)
            return model.sentiment()

        except Exception as ex:
            logging.error(ex)
            raise ex

    def get_relations(self, text: str) -> tuple[Relation]:
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
                timeout=TIMEOUT,
            )
            logging.info(response.status_code)
            # @todo Check status code.

            data = response.json()
            model = Analysis(text, data)
            return model.relations()

        except Exception as ex:
            logging.error(ex)
        raise ex

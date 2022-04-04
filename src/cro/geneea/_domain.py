# -*- coding: utf8 -*-

import json
from types import SimpleNamespace

import pandas as pd


class Datamodel(object):
    def __init__(self, input):
        self.__dict__ = json.loads(input)  # What is this?

        # ... and this vvvv ?

        # self.entities = pd.DataFrame.from_dict(
        #     pd.json_normalize(self.entities), orient="columns"
        # )
        # self.tags = pd.DataFrame.from_dict(
        #     pd.json_normalize(self.tags), orient="columns"
        # )
        # self.itemSentiments = pd.DataFrame.from_dict(
        #     pd.json_normalize(self.itemSentiments), orient="columns"
        # )
        # self.docSentiment = pd.DataFrame.from_dict(
        #     pd.json_normalize(self.docSentiment), orient="columns"
        # )

        # print(self.entities)
        # print(self.tags)
        # print(self.itemSentiments)
        # print(self.docSentiment)

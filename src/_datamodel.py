# -*- coding: utf-8 -*-

import json
import pandas as pd
from types import SimpleNamespace

class Datamodel(object):
    def __init__(self,_input):
        self.__dict__ = json.loads(_input)
        self.entities = pd.DataFrame.from_dict(pd.json_normalize(self.entities), orient='columns')
        self.tags = pd.DataFrame.from_dict(pd.json_normalize(self.tags), orient='columns')
        self.itemSentiments = pd.DataFrame.from_dict(pd.json_normalize(self.itemSentiments), orient='columns')
        self.docSentiment = pd.DataFrame.from_dict(pd.json_normalize(self.docSentiment), orient='columns')

        print(self.entities)
        print(self.tags)
        print(self.itemSentiments)
        print(self.docSentiment)

import os
import datetime as dt
from enum import Enum

from requests import post as POST

__API_KEY__=os.environ.get('GENEEA_API_KEY')
__API_URL__=os.environ.get('GENEEA_API_URL')



class Client:
    
    """
    Geneea API Client
    """

    def __init__(self, _filename):
        filename=_filename
        text = self.get_txt(filename)
        response=self.callGeneea(text)

    @classmethod
    def get_txt(a,_filename):
        raw = ""
        print("processing file: ",_filename)
        with open(_filename,encoding='utf8') as f:
            line = f.readline()
            while line:
                line = f.readline()
                raw = raw + line
        return raw

    @classmethod
    def callGeneea(self,str: input) -> tuple:
        """
        get response from a server
        """
        url=f"{__API_URL__}"
        date_format=f"%Y-%m-%d"
        headers = {
                'content-type': 'application/json',
                'Authorization': 'user_key {__API_KEY__}'
                }
        text={'text': '{input}'}
        print(f"connecting to {__API_URL__} using key {__API_KEY__}")
        data = POST(url, json=text, headers=headers).json()
        print(data)
        return data

    @classmethod
    def parse_results(tuple: input):
        """
        todo json to datamodel
        """




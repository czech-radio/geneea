# -*- coding: utf-8 -*-

"""
$ python .\docs\examples\raw_requests.py

{'version': '3.2.1', 'language': {'detected': 'cs'}, 'entities': [{'id': 'e0', 'stdForm': 'Andrej Babiš', 'type': 'person'}, {'id': 'e1', 'stdForm': 'StB', 'type': 'organization'}, {'id': 'e2', 'stdForm': 'tajná policie', 'type': 'general'}], 'tags': [{'id': 't0', 'stdForm': 'Andrej Babiš', 'type': 'base', 'relevance': 4.0}, {'id': 't1', 'stdForm': 'tajná policie', 'type': 'base', 'relevance': 4.0}, {'id': 't2', 'stdForm': 'StB', 'type': 'base', 'relevance': 4.0}, {'id': 't3', 'stdForm': 'agent', 'type': 'base', 'relevance': 2.666}, {'id': 't4', 'stdForm': 'dokument', 'type': 'base', 'relevance': 2.509}], 'relations': [{'id': 'r0', 'name': 'vedený', 'textRepr': 'vedený(Andrej Babiš)', 'type': 'ATTR', 'args': [{'type': 'SUBJECT', 'name': 'Andrej Babiš', 'entityId': 'e0'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r1', 'name': 'někdejší', 'textRepr': 'někdejší(tajná policie)', 'type': 'ATTR', 'args': [{'type': 'SUBJECT', 'name': 'tajná policie', 'entityId': 'e2'}], 'feats': {'negated': 'false', 'modality': ''}}], 'docSentiment': {'mean': 0.3, 'label': 'positive', 'positive': 0.3, 'negative': 0.0}, 'usedChars': 100}

"""

import os

import requests

URL = "https://api.geneea.com/"
KEY = os.environ.get("GENEEA_API_KEY")
HEADERS = {
    "content-type": "application/json",
    "Authorization": f"user_key {KEY}",
}

PHRASE = "Byl Andrej Babiš vedený v dokumentech někdejší tajné policie StB jako agent oprávněně, nebo ne?"
TIMEOUT = 300


if __name__ == "__main__":

    # request = requests.Request("POST",
    #     f"{URL}/v3/analysis",
    #     json={"text": PHRASE},
    #     headers=HEADERS,
    #     # timeout=TIMEOUT,
    #     # params={"paragraphs": True}
    # )

    # prepared = request.prepare()

    # print(prepared.method)
    # print(prepared.__dict__)

    result = requests.post(
        f"{URL}/v3/analysis",
        json={"text": PHRASE},
        headers=HEADERS,
        timeout=TIMEOUT,
        # params={"paragraphs": True}
    )

    print(result.json())

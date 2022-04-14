# 𝔠𝔯𝔬-𝔤𝔢𝔫𝔢𝔢𝔞-𝔠𝔩𝔦𝔢𝔫𝔱

**Python library to work with Geneea NLP REST service.**

![language-Python](https://img.shields.io/badge/language-Python-blue.svg)
[![build: tests](https://github.com/czech-radio/cro-geneea-client/actions/workflows/main.yml/badge.svg)](https://github.com/czech-radio/cro-geneea-client/actions/workflows/main.yml)
[![style: black](https://img.shields.io/badge/style-black-000000.svg)](https://github.com/psf/black)
[![quality: bugs](https://sonarcloud.io/api/project_badges/measure?project=czech-radio_cro-geneea-client&metric=bugs)](https://sonarcloud.io/dashboard?id=czech-radio_cro-geneea-client)
[![quality: code smells](https://sonarcloud.io/api/project_badges/measure?project=czech-radio_cro-geneea-client&metric=code_smells)](https://sonarcloud.io/dashboard?id=czech-radio_cro-geneea-client)
[![quality: reliability](https://sonarcloud.io/api/project_badges/measure?project=czech-radio_cro-geneea-client&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=czech-radio_cro-geneea-client)

- Status: developed (maintained)
- Version: 0.1.0-alpha (latest)
- Release: https://github.com/czech-radio/cro-geneea-client/releases/
- Website: https://czech-radio.github.io/cro-geneea-client/.
- Category: library, client
- Suppport: Python 3.10+, Windows, macOS, Ubuntu

:star: Star us on GitHub — it motivates us!


## Purpose

The library SDK wrapper for [Geneea](https://geneea.com/) API that returns raw JSON or Pythonic domain model.

## Features

- [ ] &hellip;

### Development notes

- [ ] __General Domain Model__
  - [ ] Language: The language detected. 
  - [ ] Analysis:
    - [ ] Relations
    - [ ] Tag
    - [ ] Sentiment
    - [ ] Entity =
            Person | Organization | Location | Product | Event | General # basic
            URL | Email | HashTag | Mention                              # internet
            Date | Time | Duration | Set                                 # date and time
            Number | Ordinal | Money | Percent                           # numbers
            
  - [ ] Text = original + analyzed content (this should be persisted in DB)
  - [ ] Serialize/Deserialize JSON results into domain model.

- We assume tahat all input texts are UTF-8 encoded.
- Text corrections, could contain various newline character types, no diacritics etc.


## Installation

**Prerequisites**

* We assume that you use at least Python 3.9.
* We assume that you use the virtual environment.

One can install package from the GitHub repository.

Activate the virtual environment.

```shell
source .venv/bin/activate
```

Install the package.

```
pip install git+https://github.com/czech-radio/cro-geneea-client.git
```

## Usage

Export the environent variables.

__UNIX__


```shell
export GENEEA_API_KEY=xxx
```

__Windows__


```shell
$env:GENEEA_API_KEY=xxx
```

### Use as a library

```python
import os
from cro.geneea import Client

client = client(key = os.environ.get("GENEEA_API_KEY"))

phrase = "\n".join(GeneeaClient.read_phrases("input.txt"))

# The full analysis and create models
analysis = client.get_analysis(phrase)
model = Model(phrase,analysis)
print(model.analysis())

# return model for detected entities
entities = client.get_entities(phrase)
model = Model(phrase,entities)
print(model.entities())

# get model for sentiment
sentiment = client.get_sentiment(phrase)
model = Model(phrase,sentiment)
print(model.sentiment())

# get model for tags
tags = client.get_tags(phrase)
model = Model(phrase,tags)
print(model.tags())

# get model for realtions
relations = client.get_relations(phrase)
model = Model(phrase,relations)
print(model.relations())

```




### Use as a command line program

```shell
cro.geneea --file <file_name> -type <type_name>
```

e.g.

```
cro.geneea --file ./data/input.txt --type analysis

ANALYSIS
--------
{'version': '3.2.1', 'language': {'detected': 'cs'}, 'entities': [{'id': 'e0', 'stdForm': 'PRESENT_REF', 'type': 'date'}, {'id': 'e1', 'stdForm': 'uprchlíci', 'type': 'general'}, {'id': 'e2', 'stdForm': 'jídlo', 'type': 'general'}, {'id': 'e3', 'stdForm': 'krize', 'type': 'general'}], 'tags': [{'id': 't0', 'stdForm': 'narativ', 'type': 'base', 'relevance': 4.0}, {'id': 't1', 'stdForm': 'jídlo', 'type': 'base', 'relevance': 4.0}, {'id': 't2', 'stdForm': 'uprchlíci', 'type': 'base', 'relevance': 4.0}, {'id': 't3', 'stdForm': 'krize', 'type': 'base', 'relevance': 4.0}, {'id': 't4', 'stdForm': 'ubytovávání', 'type': 'base', 'relevance': 2.555}], 'relations': [{'id': 'r0', 'name': 'ukrajinský', 'textRepr': 'ukrajinský(uprchlíci)', 'type': 'ATTR', 'args': [{'type': 'SUBJECT', 'name': 'uprchlíci', 'entityId': 'e1'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r1', 'name': 'vážit si', 'textRepr': 'vážit si-not(který,jídlo)', 'type': 'VERB', 'args': [{'type': 'SUBJECT', 'name': 'který'}, {'type': 'OBJECT', 'name': 'jídlo', 'entityId': 'e2'}], 'feats': {'negated': 'true', 'modality': ''}}, {'id': 'r2', 'name': 'sdílet', 'textRepr': 'sdílet(člověk,narativ)', 'type': 'VERB', 'args': [{'type': 'SUBJECT', 'name': 'člověk'}, {'type': 'OBJECT', 'name': 'narativ'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r3', 'name': 'uprchlický', 'textRepr': 'uprchlický(krize)', 'type': 'ATTR', 'args': [{'type': 'SUBJECT', 'name': 'krize', 'entityId': 'e3'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r4', 'name': 'převažovat', 'textRepr': 'převažovat(narativ)', 'type': 'VERB', 'args': [{'type': 'OBJECT', 'name': 'narativ'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r5', 'name': 'další', 'textRepr': 'další(narativ)', 'type': 'ATTR', 'args': [{'type': 'SUBJECT', 'name': 'narativ'}], 'feats': {'negated': 'false', 'modality': ''}}], 'docSentiment': {'mean': -0.1, 'label': 'negative', 'positive': 0.0, 'negative': -0.1}, 'usedChars': 197}
```

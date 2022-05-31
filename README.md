# 𝖈𝖗𝖔-𝖌𝖊𝖓𝖊𝖊𝖆-𝖘𝖉𝖐

[RELEASES](https://github.com/czech-radio/cro-geneea-sdk/releases/) | [WEBSITE](https://czech-radio.github.io/cro-geneea-sdk/)

![language](https://img.shields.io/badge/language-Python_v3.10+-blue.svg)
![version](https://img.shields.io/badge/version-0.3.0-blue.svg)
[![build](https://github.com/czech-radio/cro-geneea-sdk/actions/workflows/main.yml/badge.svg)](https://github.com/czech-radio/cro-geneea-sdk/actions/workflows/main.yml)
[![reliability](https://sonarcloud.io/api/project_badges/measure?project=czech-radio_cro-geneea-sdk&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=czech-radio_cro-geneea-sdk)

**Python library to work with Geneea NLP REST service.**

_The library SDK wrapper for [Geneea](https://geneea.com/) API that returns raw JSON or Pythonic domain model._

:star: Star us on GitHub — it motivates us!

## Features

- [ ] &hellip;

__Development notes__

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
from cro.geneea.sdk import Client

client = client(key = os.environ.get("GENEEA_API_KEY"))

phrase = "\n".join(GeneeaClient.read_phrases("input.txt"))

# eventually ie.: phrase = "Příliž žluťoučký kůň"


# The full analysis and create models
analysis = client.get_analysis(phrase)
print(analysis)

# return model for detected entities
entities = client.get_entities(phrase)
print(entities)

# get model for sentiment
sentiment = client.get_sentiment(phrase)
print(sentiment)

# get model for tags
tags = client.get_tags(phrase)
print(tags)

# get model for realtions
relations = client.get_relations(phrase)
print(relations)

```

### Use as a command line program

```shell
cro.geneea -i <file_name> -t <type_name> [optional output xml,csv] -f xml
# <type_name> must be either: analysis, tags, entities, relations, account
```

e.g.

```
cro.geneea --file ./data/input.txt --type analysis

ANALYSIS
--------
{'version': '3.2.1', 'language': {'detected': 'cs'}, 'entities': [{'id': 'e0', 'stdForm': 'PRESENT_REF', 'type': 'date'}, {'id': 'e1', 'stdForm': 'uprchlíci', 'type': 'general'}, {'id': 'e2', 'stdForm': 'jídlo', 'type': 'general'}, {'id': 'e3', 'stdForm': 'krize', 'type': 'general'}], 'tags': [{'id': 't0', 'stdForm': 'narativ', 'type': 'base', 'relevance': 4.0}, {'id': 't1', 'stdForm': 'jídlo', 'type': 'base', 'relevance': 4.0}, {'id': 't2', 'stdForm': 'uprchlíci', 'type': 'base', 'relevance': 4.0}, {'id': 't3', 'stdForm': 'krize', 'type': 'base', 'relevance': 4.0}, {'id': 't4', 'stdForm': 'ubytovávání', 'type': 'base', 'relevance': 2.555}], 'relations': [{'id': 'r0', 'name': 'ukrajinský', 'textRepr': 'ukrajinský(uprchlíci)', 'type': 'ATTR', 'args': [{'type': 'SUBJECT', 'name': 'uprchlíci', 'entityId': 'e1'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r1', 'name': 'vážit si', 'textRepr': 'vážit si-not(který,jídlo)', 'type': 'VERB', 'args': [{'type': 'SUBJECT', 'name': 'který'}, {'type': 'OBJECT', 'name': 'jídlo', 'entityId': 'e2'}], 'feats': {'negated': 'true', 'modality': ''}}, {'id': 'r2', 'name': 'sdílet', 'textRepr': 'sdílet(člověk,narativ)', 'type': 'VERB', 'args': [{'type': 'SUBJECT', 'name': 'člověk'}, {'type': 'OBJECT', 'name': 'narativ'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r3', 'name': 'uprchlický', 'textRepr': 'uprchlický(krize)', 'type': 'ATTR', 'args': [{'type': 'SUBJECT', 'name': 'krize', 'entityId': 'e3'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r4', 'name': 'převažovat', 'textRepr': 'převažovat(narativ)', 'type': 'VERB', 'args': [{'type': 'OBJECT', 'name': 'narativ'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r5', 'name': 'další', 'textRepr': 'další(narativ)', 'type': 'ATTR', 'args': [{'type': 'SUBJECT', 'name': 'narativ'}], 'feats': {'negated': 'false', 'modality': ''}}], 'docSentiment': {'mean': -0.1, 'label': 'negative', 'positive': 0.0, 'negative': -0.1}, 'usedChars': 197}
```

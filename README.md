# 𝖈𝖗𝖔-𝖌𝖊𝖓𝖊𝖊𝖆-𝖘𝖉𝖐

[RELEASES](https://github.com/czech-radio/cro-geneea-sdk/releases/) | [WEBSITE](https://czech-radio.github.io/cro-geneea-sdk/)

![language](https://img.shields.io/badge/language-Python_v3.10+-blue.svg)
![version](https://img.shields.io/badge/version-0.5.0-blue.svg)
[![build](https://github.com/czech-radio/cro-geneea-sdk/actions/workflows/main.yml/badge.svg)](https://github.com/czech-radio/cro-geneea-sdk/actions/workflows/main.yml)
[![quality](https://app.codacy.com/project/badge/Grade/da3fb452af474ddc940eb0194da8b6f9)](https://www.codacy.com/gh/czech-radio/cro-geneea-sdk/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=czech-radio/cro-geneea-sdk&amp;utm_campaign=Badge_Grade)

**Python library to work with Geneea NLP REST service.**

_The library SDK wrapper for [Geneea](https://geneea.com/) and helpers for NLP analysis._

:star: Star us on GitHub — it motivates us!

## Features

- [x] Get document tags.
- [x] Get document entities.
- [x] Get document relations.
- [x] Get document sentiment.
- [ ] Get complete analysis (tags, entities, relations).
- [ ] Get account information.

## Installation

**Prerequisites**

* We assume that you use at least Python 3.9.
* We assume that you use the virtual environment.

One can install package from the GitHub repository.

Activate the virtual environment.

```shell
source .venv/bin/activate   # Unix

.\.venv\Scripts\activate    # Windows
```

Install the package.

```
pip install git+https://github.com/czech-radio/cro-geneea-client.git
```

## Usage

Export the environent variables.


```shell
export GENEEA_API_KEY=xxx    # Unix

$env:GENEEA_API_KEY=xxx      # Windows
```

### Use as a program

```shell
cro.geneea --input <file_name> --type <type_name> --format <format_name>
# <type_name> must be either: analysis, tags, entities, relations, account
# <format_name> must be either: xml, json
```

e.g.

```
cro.geneea --input ./data/input.txt --type analysis --format json

ANALYSIS
--------
{'version': '3.2.1', 'language': {'detected': 'cs'}, 'entities': [{'id': 'e0', 'stdForm': 'PRESENT_REF', 'type': 'date'}, {'id': 'e1', 'stdForm': 'uprchlíci', 'type': 'general'}, {'id': 'e2', 'stdForm': 'jídlo', 'type': 'general'}, {'id': 'e3', 'stdForm': 'krize', 'type': 'general'}], 'tags': [{'id': 't0', 'stdForm': 'narativ', 'type': 'base', 'relevance': 4.0}, {'id': 't1', 'stdForm': 'jídlo', 'type': 'base', 'relevance': 4.0}, {'id': 't2', 'stdForm': 'uprchlíci', 'type': 'base', 'relevance': 4.0}, {'id': 't3', 'stdForm': 'krize', 'type': 'base', 'relevance': 4.0}, {'id': 't4', 'stdForm': 'ubytovávání', 'type': 'base', 'relevance': 2.555}], 'relations': [{'id': 'r0', 'name': 'ukrajinský', 'textRepr': 'ukrajinský(uprchlíci)', 'type': 'ATTR', 'args': [{'type': 'SUBJECT', 'name': 'uprchlíci', 'entityId': 'e1'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r1', 'name': 'vážit si', 'textRepr': 'vážit si-not(který,jídlo)', 'type': 'VERB', 'args': [{'type': 'SUBJECT', 'name': 'který'}, {'type': 'OBJECT', 'name': 'jídlo', 'entityId': 'e2'}], 'feats': {'negated': 'true', 'modality': ''}}, {'id': 'r2', 'name': 'sdílet', 'textRepr': 'sdílet(člověk,narativ)', 'type': 'VERB', 'args': [{'type': 'SUBJECT', 'name': 'člověk'}, {'type': 'OBJECT', 'name': 'narativ'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r3', 'name': 'uprchlický', 'textRepr': 'uprchlický(krize)', 'type': 'ATTR', 'args': [{'type': 'SUBJECT', 'name': 'krize', 'entityId': 'e3'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r4', 'name': 'převažovat', 'textRepr': 'převažovat(narativ)', 'type': 'VERB', 'args': [{'type': 'OBJECT', 'name': 'narativ'}], 'feats': {'negated': 'false', 'modality': ''}}, {'id': 'r5', 'name': 'další', 'textRepr': 'další(narativ)', 'type': 'ATTR', 'args': [{'type': 'SUBJECT', 'name': 'narativ'}], 'feats': {'negated': 'false', 'modality': ''}}], 'docSentiment': {'mean': -0.1, 'label': 'negative', 'positive': 0.0, 'negative': -0.1}, 'usedChars': 197}
```

### Use as a library

```python
import os
from cro.geneea.sdk import Client

client = client(key = os.environ.get("GENEEA_API_KEY"))

# Try `phrase = "Příliž žluťoučký kůň"`.
with open("input.txt", encoding='utf8') as file:
    phrases = "\n".join(file.readlines())

# Get (full) analysis.
analysis = client.get_analysis(phrase)
print(analysis)

# Get entities.
entities = client.get_entities(phrase)
print(entities)

# Get sentiment.
sentiment = client.get_sentiment(phrase)
print(sentiment)

# Get tags.
tags = client.get_tags(phrase)
print(tags)

# Get realations.
relations = client.get_relations(phrase)
print(relations)
```

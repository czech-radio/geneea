# 𝖈𝖗𝖔-𝖌𝖊𝖓𝖊𝖊𝖆-𝖘𝖉𝖐

[RELEASES](https://github.com/czech-radio/cro-geneea-sdk/releases/) | [WEBSITE](https://czech-radio.github.io/cro-geneea-sdk/)

![language](https://img.shields.io/badge/language-Python_v3.10+-blue.svg)
![version](https://img.shields.io/badge/version-0.6.0-blue.svg)
[![build](https://github.com/czech-radio/cro-geneea-sdk/actions/workflows/main.yml/badge.svg)](https://github.com/czech-radio/cro-geneea-sdk/actions/workflows/main.yml)
[![quality](https://app.codacy.com/project/badge/Grade/da3fb452af474ddc940eb0194da8b6f9)](https://www.codacy.com/gh/czech-radio/cro-geneea-sdk/dashboard?utm_source=github.com&utm_medium=referral&utm_content=czech-radio/cro-geneea-sdk&utm_campaign=Badge_Grade)

**Python library to work with Geneea NLP REST service.**

_The library SDK wrapper for [Geneea](https://geneea.com/) and helpers for NLP analysis._

:star: Star us on GitHub — it motivates us!

## Features

- [x] Get document tags.
- [x] Get document entities.
- [x] Get document relations.
- [x] Get document sentiment.
- [ ] Get complete analysis (tags, entities, relations).
- [x] Get account information.
- [ ] Get status.

## Installation

**Prerequisites**

- We assume that you use at least Python 3.9.
- We assume that you use the virtual environment.

One can install package from the GitHub repository.

Activate the virtual environment:

```shell
source .venv/bin/activate   # Unix

.\.venv\Scripts\activate    # Windows
```

Install the package from GitHub:

```
pip install git+https://github.com/czech-radio/cro-geneea-client.git
```

Local develepment:

```
git clone https://github.com/czech-radio/cro-geneea-client.git
pip install -e .[dev]
```

## Usage

Export the environment variables:

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
```

```json
{"original": "Populární známka se prodávala na jediném místě v centru Kyjeva, kde na ni každý den čekaly stovky lidí. Mezitím se arch šesti známek prodává na inzertních serverech za více než 10 tisíc korun.\n", "analyzed": {"version": "3.2.1", "language": {"detected": "cs"}, "paragraphs": [{"id": "p0", "type": "BODY", "text": "Populární známka se prodávala na jediném místě v centru Kyjeva, kde na ni každý den čekaly stovky lidí. Mezitím se arch šesti známek prodává na inzertních serverech za více než 10 tisíc korun.", "sentences": [{"id": "s0", "tokens": [{"id": "w0", "off": 0, "text": "Populární"}, {"id": "w1", "off": 10, "text": "známka"}, {"id": "w2", "off": 17, "text": "se"}, {"id": "w3", "off": 20, "text": "prodávala"}, {"id": "w4", "off": 30, "text": "na"}, {"id": "w5", "off": 33, "text": "jediném"}, {"id": "w6", "off": 41, "text": "místě"}, {"id": "w7", "off": 47, "text": "v"}, {"id": "w8", "off": 49, "text": "centru"}, {"id": "w9", "off": 56, "text": "Kyjeva"}, {"id": "w10", "off": 62, "text": ","}, {"id": "w11", "off": 64, "text": "kde"}, {"id": "w12", "off": 68, "text": "na"}, {"id": "w13", "off": 71, "text": "ni"}, {"id": "w14", "off": 74, "text": "každý"}, {"id": "w15", "off": 80, "text": "den"}, {"id": "w16", "off": 84, "text": "čekaly"}, {"id": "w17", "off": 91, "text": "stovky"}, {"id": "w18", "off": 98, "text": "lidí"}, {"id": "w19", "off": 102, "text": "."}]}, {"id": "s1", "tokens": [{"id": "w20", "off": 104, "text": "Mezitím"}, {"id": "w21", "off": 112, "text": "se"}, {"id": "w22", "off": 115, "text": "arch"}, {"id": "w23", "off": 120, "text": "šesti"}, {"id": "w24", "off": 126, "text": "známek"}, {"id": "w25", "off": 133, "text": "prodává"}, {"id": "w26", "off": 141, "text": "na"}, {"id": "w27", "off": 144, "text": "inzertních"}, {"id": "w28", "off": 155, "text": "serverech"}, {"id": "w29", "off": 165, "text": "za"}, {"id": "w30", "off": 168, "text": "více"}, {"id": "w31", "off": 173, "text": "než"}, {"id": "w32", "off": 177, "text": "10"}, {"id": "w33", "off": 180, "text": "tisíc"}, {"id": "w34", "off": 186, "text": "korun"}, {"id": "w35", "off": 191, "text": "."}]}]}], "entities": [{"id": "e0", "stdForm": "P1D", "type": "set", "mentions": [{"id": "m0", "mwl": "každý den", "text": "každý den", "tokenIds": ["w14", "w15"]}]}, {"id": "e1", "stdForm": "10", "type": "number", "mentions": [{"id": "m1", "mwl": "10", "text": "10", "tokenIds": ["w32"]}]}, {"id": "e2", "stdForm": "Kyjev", "type": "location", "mentions": [{"id": "m2", "mwl": "Kyjev", "text": "Kyjeva", "tokenIds": ["w9"]}]}], "tags": [{"id": "t0", "stdForm": "známka", "type": "base", "relevance": 3.917, "mentions": [{"id": "m3", "text": "známka", "tokenIds": ["w1"]}, {"id": "m4", "text": "známek", "tokenIds": ["w24"]}]}, {"id": "t1", "stdForm": "inzertní server", "type": "base", "relevance": 3.0, "mentions": [{"id": "m5", "text": "inzertních serverech", "tokenIds": ["w27", "w28"]}]}, {"id": "t2", "stdForm": "centrum Kyjeva", "type": "base", "relevance": 2.816, "mentions": [{"id": "m6", "text": "centru Kyjeva", "tokenIds": ["w8", "w9"]}]}, {"id": "t3", "stdForm": "arch", "type": "base", "relevance": 2.714, "mentions": [{"id": "m7", "text": "arch", "tokenIds": ["w22"]}]}, {"id": "t4", "stdForm": "jediné místo", "type": "base", "relevance": 2.703, "mentions": [{"id": "m8", "text": "jediném místě", "tokenIds": ["w5", "w6"]}]}], "relations": [{"id": "r0", "name": "prodávat", "textRepr": "prodávat(známka)", "type": "VERB", "args": [{"type": "OBJECT", "name": "známka"}], "feats": {"negated": "false", "modality": ""}, "support": [{"tokenIds": ["w3", "w2"]}]}, {"id": "r1", "name": "čekat", "textRepr": "čekat(stovka)", "type": "VERB", "args": [{"type": "SUBJECT", "name": "stovka"}], "feats": {"negated": "false", "modality": ""}, "support": [{"tokenIds": ["w16"]}]}, {"id": "r2", "name": "každý", "textRepr": "každý(den)", "type": "ATTR", "args": [{"type": "SUBJECT", "name": "den"}], "feats": {"negated": "false", "modality": ""}, "support": [{"tokenIds": ["w14"]}]}, {"id": "r3", "name": "populární", "textRepr": "populární(známka)", "type": "ATTR", "args": [{"type": "SUBJECT", "name": "známka"}], "feats": {"negated": "false", "modality": ""}, "support": [{"tokenIds": ["w0"]}]}, {"id": "r4", "name": "jediný", "textRepr": "jediný(místo)", "type": "ATTR", "args": [{"type": "SUBJECT", "name": "místo"}], "feats": {"negated": "false", "modality": ""}, "support": [{"tokenIds": ["w5"]}]}, {"id": "r5", "name": "prodávat", "textRepr": "prodávat(arch)", "type": "VERB", "args": [{"type": "OBJECT", "name": "arch"}], "feats": {"negated": "false", "modality": ""}, "support": [{"tokenIds": ["w25", "w21"]}]}, {"id": "r6", "name": "inzertní", "textRepr": "inzertní(server)", "type": "ATTR", "args": [{"type": "SUBJECT", "name": "server"}], "feats": {"negated": "false", "modality": ""}, "support": [{"tokenIds": ["w27"]}]}], "docSentiment": {"mean": 0.0, "label": "neutral", "positive": 0.0, "negative": 0.0}, "usedChars": 193}}
```

```
cro.geneea --input ./data/input.txt --type analysis --format xml

ANALYSIS
--------
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<document>
  <original length="193">Populární známka se prodávala na jediném místě v centru Kyjeva, kde na ni každý den čekaly stovky lidí. Mezitím se arch šesti známek prodává na inzertních serverech za více než 10 tisíc korun.</original>
  <analysis>
    <entities>
      <entity id="e0" type="set">P1D</entity>
      <entity id="e1" type="number">10</entity>
      <entity id="e2" type="location">Kyjev</entity>
    </entities>
    <tags>
      <tag id="t0" relevance="3.917">známka</tag>
      <tag id="t1" relevance="3.0">inzertní server</tag>
      <tag id="t2" relevance="2.816">centrum Kyjeva</tag>
      <tag id="t3" relevance="2.714">arch</tag>
      <tag id="t4" relevance="2.703">jediné místo</tag>
    </tags>
    <sentiment mean="0.0" positive="0.0" negative="0.0">neutral</sentiment>
    <relations>
      <relation id="r0" textRepr="prodávat(známka)" type="VERB">prodávat</relation>
      <relation id="r1" textRepr="čekat(stovka)" type="VERB">čekat</relation>
      <relation id="r2" textRepr="každý(den)" type="ATTR">každý</relation>
      <relation id="r3" textRepr="populární(známka)" type="ATTR">populární</relation>
      <relation id="r4" textRepr="jediný(místo)" type="ATTR">jediný</relation>
      <relation id="r5" textRepr="prodávat(arch)" type="VERB">prodávat</relation>
      <relation id="r6" textRepr="inzertní(server)" type="ATTR">inzertní</relation>
    </relations>
    <paragraphs>
      <paragraph id="p0" type="BODY" text="Populární známka se prodávala na jediném místě v centru Kyjeva, kde na ni každý den čekaly stovky lidí. Mezitím se arch šesti známek prodává na inzertních serverech za více než 10 tisíc korun.">
        <sentences />
        <sentence id="s0" tokens="[{'id': 'w0', 'off': 0, 'text': 'Populární'}, {'id': 'w1', 'off': 10, 'text': 'známka'}, {'id': 'w2', 'off': 17, 'text': 'se'}, {'id': 'w3', 'off': 20, 'text': 'prodávala'}, {'id': 'w4', 'off': 30, 'text': 'na'}, {'id': 'w5', 'off': 33, 'text': 'jediném'}, {'id': 'w6', 'off': 41, 'text': 'místě'}, {'id': 'w7', 'off': 47, 'text': 'v'}, {'id': 'w8', 'off': 49, 'text': 'centru'}, {'id': 'w9', 'off': 56, 'text': 'Kyjeva'}, {'id': 'w10', 'off': 62, 'text': ','}, {'id': 'w11', 'off': 64, 'text': 'kde'}, {'id': 'w12', 'off': 68, 'text': 'na'}, {'id': 'w13', 'off': 71, 'text': 'ni'}, {'id': 'w14', 'off': 74, 'text': 'každý'}, {'id': 'w15', 'off': 80, 'text': 'den'}, {'id': 'w16', 'off': 84, 'text': 'čekaly'}, {'id': 'w17', 'off': 91, 'text': 'stovky'}, {'id': 'w18', 'off': 98, 'text': 'lidí'}, {'id': 'w19', 'off': 102, 'text': '.'}]" />
        <sentence id="s1" tokens="[{'id': 'w20', 'off': 104, 'text': 'Mezitím'}, {'id': 'w21', 'off': 112, 'text': 'se'}, {'id': 'w22', 'off': 115, 'text': 'arch'}, {'id': 'w23', 'off': 120, 'text': 'šesti'}, {'id': 'w24', 'off': 126, 'text': 'známek'}, {'id': 'w25', 'off': 133, 'text': 'prodává'}, {'id': 'w26', 'off': 141, 'text': 'na'}, {'id': 'w27', 'off': 144, 'text': 'inzertních'}, {'id': 'w28', 'off': 155, 'text': 'serverech'}, {'id': 'w29', 'off': 165, 'text': 'za'}, {'id': 'w30', 'off': 168, 'text': 'více'}, {'id': 'w31', 'off': 173, 'text': 'než'}, {'id': 'w32', 'off': 177, 'text': '10'}, {'id': 'w33', 'off': 180, 'text': 'tisíc'}, {'id': 'w34', 'off': 186, 'text': 'korun'}, {'id': 'w35', 'off': 191, 'text': '.'}]" />
      </paragraph>
    </paragraphs>
  </analysis>
</document>
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

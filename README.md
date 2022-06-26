# 𝖈𝖗𝖔-𝖌𝖊𝖓𝖊𝖊𝖆-𝖘𝖉𝖐

[RELEASES](https://github.com/czech-radio/cro-geneea-sdk/releases/) | [WEBSITE](https://czech-radio.github.io/cro-geneea-sdk/)

![language](https://img.shields.io/badge/language-Python_v3.10+-blue.svg)
![version](https://img.shields.io/badge/version-0.6.0-blue.svg)
[![build](https://github.com/czech-radio/cro-geneea-sdk/actions/workflows/main.yml/badge.svg)](https://github.com/czech-radio/cro-geneea-sdk/actions/workflows/main.yml)
[![quality](https://app.codacy.com/project/badge/Grade/da3fb452af474ddc940eb0194da8b6f9)](https://www.codacy.com/gh/czech-radio/cro-geneea-sdk/dashboard?utm_source=github.com&utm_medium=referral&utm_content=czech-radio/cro-geneea-sdk&utm_campaign=Badge_Grade)

**Python library to work with Geneea NLP REST service.**

_The library SDK wrapper for [Geneea](https://geneea.com/) and helpers for NLP analysis._

:star: Star us on GitHub — it motivates us!

## Installation

**Prerequisites**

- We assume that you use at least Python 3.9.
- We assume that you use the virtual environment.

One can install package from the GitHub repository.

Activate the virtual environment:

Unix

```shell
source .venv/bin/activate
```

Windows

```powershell
.\.venv\Scripts\activate
```

Install the latest package version from repository main branch.

```
pip install git+https://github.com/czech-radio/cro-geneea-client.git
```

For development clone the repository and install with editable mode.

```
git clone https://github.com/czech-radio/cro-geneea-client.git
pip install -e .[dev]
```

## Features & Usage

- [x] Get the document tag.
- [x] Get the document entities.
- [x] Get the document relations.
- [x] Get the document sentiment.
- [ ] Get the document analysis i.e. tags, entities, relations, sentiment.
- [x] Get the account information.
- [ ] Get the status.

**TODO**

- The domain model needs review and some changes.
- The XML and JSON serialization outputs should be equal.

### Prerequisities

Export the environment variables:

Unix

```shell
export GENEEA_API_KEY=YOUR_KEY
```

Windows

```powershell
$env:GENEEA_API_KEY=YOUR_KEY
```

### Use as a program

```shell
cro.geneea --input <file_name> --type <type_name> --format <format_name>

# The <format_name> option must be one of: `xml`, `json`.
# The <type_name> option must be one of: `analysis`, `tags`, `entities`, `relations`, `account`.
```

e.g.

```
cro.geneea --input ./docs/examples/input.txt --type analysis --format xml
```

```
cro.geneea --input ./docs/examples/input.txt --type analysis --format json
```

See the examples [analysis.xml](./docs/examples/analysis.xml) and [analysis.json](./docs/examples/analysis.json).

### Use as a library

```python
import os
from cro.geneea.sdk import Client

client = client(key = os.environ.get("GENEEA_API_KEY"))
# Try `phrase = "Příliž žluťoučký kůň"`.

with open("input.txt", encoding='utf8') as file:
    phrases = "\n".join(file.readlines())
```

### Get the document analysis

```python
analysis = client.get_analysis(phrase)
```

### Get only the document entities

```python
entities = client.get_entities(phrase)
```

### Get only the document sentiment

```python
sentiment = client.get_sentiment(phrase)
```

### Get only the document tags

```python
tags = client.get_tags(phrase)
```

### Get only the document realations

```python
relations = client.get_relations(phrase)
```

## Contribution

&hellip;

## Documentation

The complete documentation soon&hellip;

## References

- https://geneea.com/
- https://demo.geneea.com/
- https://api.geneea.com/
- https://api.geneea.com/api-docs

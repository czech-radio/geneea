# geneea

[RELEASES](https://github.com/czech-radio/geneea/releases/) | [WEBSITE](https://czech-radio.github.io/geneea/)

![language](https://img.shields.io/badge/language-Python_v3.10+-blue.svg)
![version](https://img.shields.io/badge/version-0.6.0-blue.svg)
[![build](https://github.com/czech-radio/cro-geneea-sdk/actions/workflows/main.yml/badge.svg)](https://github.com/czech-radio/cro-geneea-sdk/actions/workflows/main.yml)
[![quality](https://app.codacy.com/project/badge/Grade/da3fb452af474ddc940eb0194da8b6f9)](https://www.codacy.com/gh/czech-radio/cro-geneea-sdk/dashboard?utm_source=github.com&utm_medium=referral&utm_content=czech-radio/cro-geneea-sdk&utm_campaign=Badge_Grade)

**Python library to work with Geneea NLP REST service.**

_The library SDK wrapper for [Geneea](https://geneea.com/) and helpers for NLP analysis._

:star: Star us on GitHub — it motivates us!

## Installation

Prerequisites:

- We assume that you use at least Python 3.9.
- We assume that you use the virtual environment.

Install the latest package version from repository main branch.

```powershell
pip install git+https://github.com/czech-radio/cro-geneea-client.git
```

For development clone the repository and install with editable mode.

```powershell
git clone https://github.com/czech-radio/cro-geneea-client.git
pip install -e .[dev]
```

## Features & Usage

- Get the document tags.
- Get the document entities.
- Get the document relations.
- Get the document sentiment.
- Get the account information (work-in.progress).
- Get the service health check status (work-in.progress).
- Get the document complete analysis (tags, entities, relations, sentiment).

At this moment only the synchronous (blocking) calls are implemented. This may
change in the future.

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

```powershell
cro.geneea --input <file_name> --type <type_name> --format <format_name>
```

- The <format_name> option must be one of: xml, json
- The <type_name> option must be one of: tags, entities, relations, account, analysis

e.g.

```powershell
cro.geneea --input ./docs/examples/input.txt --type analysis --format xml
```

```powershell
cro.geneea --input ./docs/examples/input.txt --type analysis --format json
```

See the examples [analysis.xml](./docs/examples/analysis.xml) and [analysis.json](./docs/examples/analysis.json).

### Use as a library

See example [notebook](./docs/examples/Document-Analysis.ipynb)

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
analysis = client.get_analysis(phrases)
```

### Get only the document entities

```python
entities = client.get_entities(phrases)
```

### Get only the document sentiment

```python
sentiment = client.get_sentiment(phrases)
```

### Get only the document tags

```python
tags = client.get_tags(phrases)
```

### Get only the document realations

```python
relations = client.get_relations(phrases)
```

## Contribution

See the [CONTRIBUTING.md](./.github/CONTRIBUTING.md) document.

## Documentation

The complete documentation soon&hellip;

## References

- [Geneea](https://geneea.com/)
- [Geneea demo](https://demo.geneea.com/)
- [Genee REST API documentation](https://api.geneea.com/)

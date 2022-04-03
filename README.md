# 𝔠𝔯𝔬-𝔤𝔢𝔫𝔢𝔢𝔞-𝔠𝔩𝔦𝔢𝔫𝔱

**The 𝔠𝔯𝔬-𝔤𝔢𝔫𝔢𝔢𝔞-𝔠𝔩𝔦𝔢𝔫𝔱 is a Python library to work with Geneea NLP REST service.**

![Python](https://img.shields.io/badge/Language-Python-blue.svg)
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
- Suppport: Python 3.9+, Windows, macOS, Ubuntu

:star: Star us on GitHub — it motivates us!


## Purpose

The library <strike>reads contents of local text file _(utf-8)_</strike> and sends it as a query to [Geneea](https://geneea.com/) API
that returns JSON with its analysis.

&hellip;

## Features

- [ ] &hellip;

### TODO

- [ ] Text file corrections, could contain various newline character types, disturbing/unnecessary/varying headers etc.
- [ ] Charset identification/normalization is to consider
- [ ] building query+headers to a POST form
- [ ] gathering/parsing JSON results into datamodel
- [ ] outputting response from server to `stdout`, writing to databse, storing as files etc.

## Installation

**Prerequisites**

* We assume that you use at least Python 3.9.
* We assume that you use the virtual environment.

One can install package from the GitHub repository.

```
pip install git+https://github.com/czech-radio/cro-geneea-client.git
```

## Usage
```
export GENEEA_API_KEY=https://xxx/url/to/geneea/api
export GENEEA_API_URL=apikeyinstringform

source .venv/bin/activate


python src/ -f "input_filename.txt"
```

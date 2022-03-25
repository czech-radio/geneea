# 𝔠𝔯𝔬-𝔤𝔢𝔫𝔢𝔢𝔞-𝔠𝔩𝔦𝔢𝔫𝔱

**The 𝔠𝔯𝔬-𝔤𝔢𝔫𝔢𝔢𝔞-𝔠𝔩𝔦𝔢𝔫𝔱 is a Python library to work with Geneea NLP REST service.**

## Purpose

library reads contents of local text file _(utf-8)_ and sends it as a query to [Geneea](https://geneea.com/) API
that returns JSON with its analysis

&hellip;

## TODO

- [ ] Text file corrections, could contain various newline character types, disturbing/unnecessary/varying headers etc.
- [ ] Charset identification/normalization is to consider
- [ ] building query+headers to a POST form
- [ ] gathering/parsing JSON results into datamodel
- [ ] outputting response from server to ```stdout```, writing to databse, storing as files etc.

## Installation

**Prerequisites**

* We assume that you use at least Python 3.9.
* We assume that you use the virtual environment.

One can install package from the GitHub repository.

```
pip install git+https://github.com/czech-radio/cro-geneea-client.git
```

## Usage

export GENEEA_API_KEY=xxx
export GENEEA_API_URL=yyy

cro.geneea -f "input_filename.txt"


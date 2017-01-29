# BibTeX parser for Python

A simple and maintainable parser for the BibTeX language using pyparsing.

## What to expect
This project is work in progress.
The following versioning scheme tells you what you can expect from the current version.

* Version 0.1: More or less just a skeleton and won't reliably produce a result.
* Version 0.2: All the functions described below will be implemented, but not all edge cases will work.
* Version 0.3: A full implementation of the bibtex language, including tags and comments. A strict mode. But no customisation. <!--TODO: replace foo-->

If no major problems show up, I will release a stable Version 1.0 after that.

## Installation
The easiest way to install python-bibtex is with the pip package manager.
```sh
git clone https://github.com/DrFrankeStein/python-bibtex
cd python-bibtex
pip install .
```
Sometime in the future it will also be available on pypi.
But maybe under a different name.

### Dependencies

* [pyparsing](http://pyparsing.wikispaces.com/)

## Usage

### As a python library
Simply import the load/loads and dump/dumps functions from the bibtex module,
as in any other parser module.

They will return a list of dictionaries.
Each dictionary represents a reference and will always contain a `type` and a `id` entry.

```python
>>> import bibtex
>>> bibtex.loads("""
... @article{foo16,
...     author = "John Doe",
...     year = 2016,
...     title = "Foo and Bar"
... }""")
[{'author': 'John Doe',
  'id': 'foo16',
  'title': 'Foo and Bar',
  'type': 'article',
  'year': '2016'}]
```

### As a command line tool
The commands
```sh
bib2json file.bib
```
or
```sh
bib2yaml file.bib
```
generate a `file.json` or `file.yaml` respectively.

A special use case is [pandocs](http://pandoc.org/MANUAL.html#citations) system for including references.
This requires as certain structure that can be generated with the `-p`/`--pandoc` command line option.
```sh
bib2yaml -p file.bib
```

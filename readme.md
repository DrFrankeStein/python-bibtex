# BibTeX parser for Python

A simple and maintainable parser for the BibTeX language using pyparsing.


## Usage

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


## Dependencies

* [pyparsing](http://pyparsing.wikispaces.com/)

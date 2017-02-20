"""Simple BibTeX parser using pyparing.

The api is oriented on the API of common serialisation modules
such as pickle, json, pyyaml and so on.

The following functions are provided:

load
    Parse BibTeX from a filelike object
loads
    Parse BibTeX from a string
dump
    Write BibTeX to a filelike object
dumps
    Write BibTeX to a string

Examples:

    >>> import bibtex
    >>> bibtex.loads('@book{foo16, author="John Doe", year=2016, title="Foo"')
    [{'author': 'John Doe',
      'id': 'foo16',
      'title': 'Foo',
      'type': 'book',
      'year': '2016'}]

    >>> print(bibtex.dumps([{'author': 'John Doe',
                             'id': 'foo16',
                             'title': 'Foo',
                             'type': 'book',
                             'year': '2016'}]))
    @book{foo16,
        author = "John Doe",
        title = "Foo",
        year = "2016"
    }

"""
from  bibtex.reader import load, loads
from bibtex.writer import dump, dumps

__all__ = ['load', 'loads', 'dump', 'dumps']

__version__ = '0.1.2'

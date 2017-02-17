# -*- encoding: utf-8 -*-
"""
Tests for the parserfuntions `loads` and `dumps` from the bibtex module.
"""

import pytest
from bibtex import load, loads, dump, dumps
import pyparsing as pp


BIBCODE_EXAMPLES = [
    ("""@ArTiCle{SomeLabel,
     author = {Max Mustermann},
     title=  {Einführung in das Sammeln von Briefmarken},
     abstract= {Foo}
     }""",
     [{'type' : 'article',
       'id'   : 'SomeLabel',
       'author': 'Max Mustermann',
       'title': 'Einführung in das Sammeln von Briefmarken',
       'abstract': 'Foo'}]),
    ("""
     @article{bar15,
         author = "Maya {Musterman}",
         title= FOO
     }
     @book{Foo16,
         author = 'Max {Musterman}',
         year = 1788,
         title = "The Title"
     }""",
     [{'author': 'Maya {Musterman}',
       'id': 'bar15',
       'title': 'FOO',
       'type': 'article'},
      {'author': 'Max {Musterman}',
       'id': 'Foo16',
       'title': 'The Title',
       'type': 'book',
       'year': '1788'}]),
    ("""
     @article{bar15,
         title= Bar,
         author = {Maya Musterman}
     }
     @book{foo16,
         author = {{Max Musterman}},
         title = Foo
     }""",
     [{'author': 'Maya Musterman',
       'id': 'bar15',
       'title': 'Bar',
       'type': 'article'},
      {'author': 'Max Musterman',
       'id': 'foo16',
       'title': 'Foo',
       'type': 'book'}]),
    ]


@pytest.mark.parametrize('bibcode,bibdata', BIBCODE_EXAMPLES)
def test_loads_with_known_values(bibcode, bibdata):
    assert loads(bibcode) == bibdata


@pytest.mark.parametrize('bibcode,bibdata', BIBCODE_EXAMPLES)
def test_selfconsistency(bibcode, bibdata):
    assert loads(dumps(bibdata)) == bibdata


def test_loads_empty():
    assert loads('') == []
    assert loads('\n ') == []


def test_dumps_empty():
    assert dumps([]) == ''


def test_exception_on_empty_attributes():
   with pytest.raises(pp.ParseException):
       loads('@{title={},author={}}')
   with pytest.raises(pp.ParseException):
       loads('@ARTICLE{}')


def test_raise_on_incomplete_record():
   with pytest.raises(pp.ParseException):
       loads('@ARTICLE{label,title={},author={},')
   with pytest.raises(pp.ParseException):
       loads('@ARTICLE{label,title={},author')


def test_raise_on_missing_syntax():
   with pytest.raises(pp.ParseException):
       loads('@ARTICLE{label,title={},author{}}')
   with pytest.raises(pp.ParseException):
       loads('@ARTICLE{label,title=,author={}}')
   with pytest.raises(pp.ParseException):
       loads('@ARTICLE{label,title={}author={}}')


def test_raise_on_maleformed_record():
    with pytest.raises(KeyError):
        dumps([{'id': 'foo16', 'author': 'John Doe'}])
    with pytest.raises(KeyError):
        dumps([{'type': 'book', 'author': 'John Doe'}])
    with pytest.raises(ValueError):
        dumps([{'id': 'bar17', 'type': '', 'author': 'John Doe'}])


def test_raise_on_maleformed_strings():
    with pytest.raises(ValueError):
        dumps([{'id': 'bar17', 'type': 'bo@ok', 'author': 'John Doe'}])
    with pytest.raises(ValueError):
        dumps([{'id': 'bar,17', 'type': 'book', 'author': 'John Doe'}])
    with pytest.raises(ValueError):
        dumps([{'id': 'bar17', 'type': 'book', 'aut,hor': 'John Doe'}])


def test_real_examples():
    list(load(open('./tests/examples.bib')))

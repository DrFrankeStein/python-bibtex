"""
Tests for the parserfuntions `loads` and `dumps` from the bibtex module.
"""

import pytest
from bibtex import loads, dumps
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
    ]


@pytest.mark.parametrize('bibcode,bibdata', BIBCODE_EXAMPLES)
def test_loads_with_known_values(bibcode, bibdata):
    assert loads(bibcode) == bibdata


@pytest.mark.parametrize('bibcode,bibdata', BIBCODE_EXAMPLES)
def test_selfconsistency(bibcode, bibdata):
    assert loads(dumps(bibdata)) == bibdata


def test_exception_on_empty_attributes():
   with pytest.raises(pp.ParseException):
       print(loads('@{title={},author={}}'))
   with pytest.raises(pp.ParseException):
       print(loads('@ARTICLE{}'))


def test_exception_on_incomplete_record():
   with pytest.raises(pp.ParseException):
       loads('@ARTICLE{label,title={},author={},')
   with pytest.raises(pp.ParseException):
       loads('@ARTICLE{label,title={,author={}}')

# TODO: make more tests
#       - missing '='
#       - unknown Type
#       - wrong commas

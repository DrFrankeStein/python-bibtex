import pyparsing as pp
from pyparsing import Word, Group, OneOrMore, Suppress, Optional,\
                      alphas, alphanums, alphas8bit, punc8bit


def _syntax(bibfile, number, line):
    print('texbib parser: Syntaxerror in file {}, line {}\n\t'
          .format(bibfile, number), line)
    # TODO: rewrite to convert pyparsing error to msg


def bibtex_parser():
    """Builds a pyparsing expression that can parse bibtex"""

    # define allowed characters for values
    val_chrs = alphanums + alphas8bit

    cite_type = Word(alphas).setParseAction(lambda t: t[0].lower()) # TODO: strict

    # allow whitespace and punctuation in quoted values; TODO: refactor
    more = ' !#$%&()*+,-./:;<=>?@[\\]^_`´~|' + punc8bit
    braced = Suppress('{') + Word(val_chrs+more+'"') + Suppress('}')

    # key; TODO: allow only known keys in strict
    key = Word(val_chrs)
    value = braced ^ pp.quotedString.setParseAction(pp.removeQuotes)\
            ^ Word(val_chrs)

    # value in braces or in quotes or as singe word
    key_value_pair = key + Suppress('=') + value

    citation = Group(Suppress('@') + cite_type
                     + Suppress('{') + Word(alphanums+'_-') + Suppress(',')
                     + Group(pp.delimitedList(Group(key_value_pair)))
                     + Suppress('}'))

    return OneOrMore(citation)


def read(string):
    bibtex = bibtex_parser()
    for cite_type, bib_id, info in bibtex.parseString(string):
        yield dict(list(info) + [('type', cite_type), ('id', bib_id)])


def loads(string):
    return list(read(string))


def load(path_or_buffer):
    # bibtex = bibtex_parser()
    # bibtex.parseFile(path_or_buffer)
    return

import pyparsing as pp
from pyparsing import Word, Group, Suppress


def _syntax(bibfile, number, line):
    print('texbib parser: Syntaxerror in file {}, line {}\n\t'
          .format(bibfile, number), line)
    # TODO: rewrite to convert pyparsing error to msg


def bibtex_parser():
    """Builds a pyparsing expression that can parse bibtex

    No Arguments. Returns None."""

    # define allowed characters for values
    val_chrs = pp.alphanums + pp.alphas8bit

    # TODO: strict
    cite_type = Word(pp.alphas).setParseAction(lambda t: t[0].lower())

    # allow whitespace and punctuation in quoted values
    single = pp.QuotedString('"', multiline=True)
    double = pp.QuotedString("'", multiline=True)
    # allow values with multiple braces
    braced = pp.nestedExpr('{', '}').setParseAction(lambda t: ' '.join(t[0]))

    # key; TODO: allow only known keys in strict
    key = Word(val_chrs).setParseAction(lambda t: t[0].lower())
    value = single | double | Word(val_chrs) | braced

    # value in braces or in quotes or as singe word
    key_value_pair = key + Suppress('=') + value

    citation = Group(Suppress('@') + cite_type
                     + Suppress('{') + Word(pp.alphanums+'_-') + Suppress(',')
                     + Group(pp.delimitedList(Group(key_value_pair)))
                     + Suppress('}'))

    comment = Group(Suppress('@') + pp.Literal('comment') + braced)

    tag_def = Group(Suppress('@') + pp.Literal('string') + braced
                    + Suppress('{')
                    + Group(pp.delimitedList(Group(key_value_pair)))
                    + Suppress('}'))

    bibitem = citation | comment | tag_def

    return pp.OneOrMore(bibitem)



def read(string):
    """Parse `string` as bibtex and return a generator that yields citations as dicts.
    Each dict has a `id` and a `type` entry.

    Arguments:
    - string: str
        bibtex formated string

    Returns:
    - Generator[Dict[str,str]]"""
    if not string.strip():
        raise StopIteration
    bibtex = bibtex_parser()
    for cite_type, bib_id, info in bibtex.parseString(string):
        yield dict(list(info) + [('type', cite_type), ('id', bib_id)])


def loads(string):
    """Parse `string` as bibtex and return a list of the citations, each as dict.
    Each dict has a `id` and a `type` entry.

    Arguments:
    - string: str
        bibtex formated string

    Returns:
    - List[Dict[str,str]]"""
    return list(read(string))


def load(filelike):
    """Parse content of filelike as BibTeX and return a list of the citations, each as dict.
    Each dict has a `id` and a `type` entry.

    Arguments:
    - filelike: filelike
        An object that has a `read` method

    Returns:
    - List[Dict[str,str]]"""
    return list(read(filelike.read()))

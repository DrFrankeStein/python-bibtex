def _valid(value):
    return value and not any(c in value for c in '@{},')


def cite_str(bibitem):
    if any(not _valid(bibitem[att]) for att in ('type', 'id'))\
            or any(not _valid(key) for key in bibitem):
        raise ValueError

    head = '@{item[type]}{{{item[id]},\n\t'.format(item=bibitem)
    key_value_pairs = ['{key} = "{value}"'.format(key=key, value=value)
                       for key, value in bibitem.items()
                       if key not in ('id', 'type')]
    return head + ',\n\t'.join(key_value_pairs) + '\n}'


def write(bib):
    """Yield a BibTeX representaion for each element in `bib`.

    Arguments:
    - bib: List[Dict[str,str]]
        list of  citations, each citation must be a dict with an `id` and a `type` entry

    Returns:
    - Generator[str]"""
    for item in bib:
        yield cite_str(item)


def dumps(bib):
    """Make a BibTeX representaion bib.

    Arguments:
    - bib: List[Dict[str,str]]
        list of  citations, each citation must be a dict with an `id` and a `type` entry

    Returns:
    - BibTeX formated string: str"""
    return '\n'.join(list(write(bib)))


def dump(bib, filelike):
    """Write BibTeX representation from `bib` to `filelike`.

    Arguments:
    - bib: List[Dict[str,str]]
        list of  citations, each citation must be a dict with an `id` and a `type` entry
    - filelike: filelike
        An object that has a `write` method

    Returns None."""
    for item in write(bib):
        filelike.write(item)

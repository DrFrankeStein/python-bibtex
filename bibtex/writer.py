def cite_str(bibitem):
    # TODO: check for maleformed items
    head = '@{item[type]}{{{item[id]},\n\t'.format(item=bibitem)
    key_value_pairs = ['{} = "{}"'.format(key, val)
                       for key, val in bibitem.items()
                       if key not in ('id','type')]
    return  head + ',\n\t'.join(key_value_pairs) + '\n}'


def write(bib):
    for item in bib:
        yield cite_str(item)


def dumps(bib):
    return '\n'.join(list(write(bib)))


def dump(bib, filelike):
    for item in write(bib):
        filelike.write(item)

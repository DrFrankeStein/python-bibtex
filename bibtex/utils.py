import sys, os, argparse

from bibtex.reader import load


def get_argparser(prog_name):
    """Utility function to build an ArgumentParser,
    usable for both `bib2json` and `bib2yaml`"""
    argp = argparse.ArgumentParser(
        prog=prog_name,
        description='Convert BibTeX references to {}.'.format(prog_name[-4:]))
    argp.add_argument('-o', '--outfile', metavar='PATH',
                      help=('custom output file name '
                            'or `stdout` for writing to stdout'))
    argp.add_argument('-p', '--pandoc', action='store_true',
                      help='sturcure output in pandoc compatible form')
    argp.add_argument('-r', '--readable', action='store_true',
                      help='add line breaks and indent')
    argp.add_argument('-s', '--strict', action='store_true',
                      help='strict mode, parses only standard BibTeX')
    argp.add_argument('infile',
                      help=('BibTeX file to process'
                            'or `-`/`stdin` for reading from stdin'))
    return argp


def get_in_buffer(infn):
    if infn in ('-', 'stdin'):
        buf = sys.stdin
    else:
        buf = open(infn, 'r')
    return buf


def get_out_buffer(outfn, infn):
    if not outfn:
        buf = open(os.path.splitext(infn)[0] + '.json', 'w')
    elif outfn == 'stdout':
        buf = sys.stdout
    else:
        buf = open(outfn, 'w')
    return buf


def bib2yaml():
    """Entry point for the bib2yaml commad line tool"""
    args = get_argparser('bib2yaml').parse_args()

    try:
        import yaml
    except ImportError:
        sys.stderr.write('bib2yaml: pyyaml is not installed\n')
        sys.exit(1)

    with get_in_buffer(args.infile) as infile:
        bib = load(infile)

    if args.readable:
        writer_options = {'default_flow_style': False}
    else:
        writer_options = {}

    with get_out_buffer(args.outfile, args.infile) as outfile:
        yaml.dump(bib, outfile, **writer_options)


def bib2json():
    """Entry point for the bib2json commad line tool"""
    args = get_argparser('bib2json').parse_args()

    import json

    with get_in_buffer(args.infile) as infile:
        bib = load(infile)

    if args.readable:
        writer_options = {'indent': 4}
    else:
        writer_options = {}

    with get_out_buffer(args.outfile, args.infile) as outfile:
        json.dump(bib, outfile, **writer_options)

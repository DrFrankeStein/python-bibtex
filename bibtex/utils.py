import sys, os, argparse

from bibtex.reader import load


def get_argparser(prog_name):
    argp = argparse.ArgumentParser(
        prog=prog_name,
        description='Convert BibTeX references to {}.'
                    .format(prog_name[-4:]))
    argp.add_argument('-s', '--strict', action='store_true',
                      help='strict mode, parses only standard BibTeX')
    argp.add_argument('-o', '--outfile',
                      help='custom output file name')
    argp.add_argument('infile', help='BibTeX file to process')
    return argp


def bib2yaml():
    """Entry point for the bib2yaml commad line tool"""
    argp = get_argparser('bib2yaml')
    argp.add_argument('-p', '--pandoc', action='store_true',
                      help='sturcure yaml in pandoc compatible format')
    args = argp.parse_args()

    try:
        import yaml
    except ImportError:
        sys.stderr.write('bib2yaml: pyyaml is not installed\n')
        sys.exit(1)

    with open(args.infile, 'r') as infile:
        bib = load(infile)

    with open(os.path.splitext(args.infile)[0] + '.yaml', 'w') as outfile:
        yaml.dump(bib, outfile, default_flow_style=False)


def bib2json():
    """Entry point for the bib2json commad line tool"""
    args = get_argparser('json').parse_args()

    import json

    with open(args.infile, 'r') as infile:
        bib = load(infile)

    with open(os.path.splitext(args.infile)[0] + '.json', 'w') as outfile:
        json.dump(bib, outfile, indent=4)

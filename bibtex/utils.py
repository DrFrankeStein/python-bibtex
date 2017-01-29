import os, argparse

from bibtex.reader import load


def bib2yaml():
    """Entry point for the bib2yaml commad line tool"""
    argp = argparse.ArgumentParser(
        prog='bib2yaml',
        description='Convert BibTeX references to yaml.')

    argp.add_argument('-p', '--pandoc', action='store_true',
                      help='Sturcure yaml in pandoc compatible format')
    argp.add_argument('infile', help='BibTeX file to process')

    args = argp.parse_args()

    try:
        import yaml
    except ImportError:
        print('bib2yaml: pyyaml is not installed')

    with open(args.infile, 'r') as infile:
        bib = load(infile)

    with open(os.path.splitext(args.infile)[0] + '.yaml', 'w') as outfile:
        yaml.dump(bib, outfile, default_flow_style=False)


def bib2json():
    """Entry point for the bib2json commad line tool"""
    import json

    argp = argparse.ArgumentParser(
        prog='bib2json',
        description='Convert BibTeX references to json.')

    argp.add_argument('infile', help='BibTeX file to process')

    args = argp.parse_args()

    with open(args.infile, 'r') as infile:
        bib = load(infile)

    with open(os.path.splitext(args.infile)[0] + '.json', 'w') as outfile:
        json.dump(bib, outfile, indent=4)

import argparse
import json
import yaml

from bibtex.reader import load
from bibtex.writer import dump


def bib2yaml():
    """Entry point for the bib2yaml commad line tool"""

    argp = argparse.ArgumentParser(
        prog='bib2yaml',
        description='Convert BibTeX references to yaml.')

    argp.add_argument('-p', '--pandoc', action='store_true',
                      help='Sturcure yaml in pandoc compatible format')
    argp.add_argument('infile', help='BibTeX file to process')

    args = argp.parse_args()

    print(args)


def bib2json():
    """Entry point for the bib2json commad line tool"""

    argp = argparse.ArgumentParser(
        prog='bib2json',
        description='Convert BibTeX references to json.')

    argp.add_argument('infile', help='BibTeX file to process')

    args = argp.parse_args()

    print(args)

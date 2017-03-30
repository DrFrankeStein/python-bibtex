"""This module contains a specification of the BibTeX language.

Contents:

    bnf: str
        Extended Backus–Naur form
        note that there is no universlly agreed upon BNF for bibtex.
        this is just what I used for this parser
    citation_types: Dict[str, Dict[str, Union[str, List[str]]]]
        strictly these are all allowd citation types with descriptions
        and lists of attributes that must or can be in a citation
        of that type
"""


bnf = """
bibtex   ::= citation [citation ...] ;
citation ::= "@" [ type "{" [id ","] kvpair ("," kvpair)* "}"
                 | "string" "{" abbr ("," abbr)* "}"
                 | "comment" "{" comment "}"
                 | "preamble" "{" preamble "}" ]
id       ::= [\a-_]+
kvpair   ::= key "=" value
type     ::= [ article | book | booklet | conference | inbook
             | incollection | inproceedings | manual | mastersthesis
             | misc | phdthesis | proceedings | techreport | unpublished]
key 	 ::= s. fields.py
value 	 ::= s. fields.py
comment  ::= anything
preamble ::= ???"""


citation_types = {
    "article": {
        "description": "An article from a journal or magazine",
        "required": ["author", "title", "journal", "year", "volume"],
        "optional": ["number", "pages", "month", "note", "key"]},
    "book": {
        "description": "A book with an explicit publisher",
        "required": [["author", "editor"], "title", "publisher", "year"],
        "optional": ["volume", "number", "series", "address", "edition",
                     "month", "note", "key"]},
    "booklet": {
        "description": ("A work that is printed and bound, but without"
                        " a named publisher or sponsoring institution"),
        "required": ["title"],
        "optional": ["author", "howpublished", "address", "month", "year",
                     "note", "key"]},
    "conference": {
        "description": ("The same as inproceedings,"
                        "included for Scribe compatibility"),
        "required": ["author", "title", "booktitle", "year"],
        "optional": ["editor", ["volume", "number"], "series", "pages", "note",
                     "address", "month", "organization", "publisher", "key"]},
    "inbook": {
        "description": "A part of a book, usually untitled. May be a chapter"
                       "(or section, etc.) and/or a range of pages",
        "required": [["author", "editor"], "title", "chapter"/"pages",
                     "publisher", "year"],
        "optional": [["volume", "number"], "series", "type", "address",
                     "edition", "month", "note", "key"]},
    "incollection": {
        "description": "A part of a book having its own title",
        "required": ["author", "title", "booktitle", "publisher", "year"],
        "optional": ["editor", ["volume", "number"], "series", "type", "pages",
                     "chapter", "address", "edition", "month", "note", "key"]},
    "inproceedings": {
        "description": "An article in a conference proceedings",
        "required": ["author", "title", "booktitle", "year"],
        "optional": ["editor", ["volume", "number"], "series", "pages", "note",
                     "address", "month", "organization", "publisher", "key"]},
    "manual": {
        "description": "Technical documentation",
        "required": ["title"],
        "optional": ["author", "organization", "address", "edition",
                     "month", "year", "note", "key"]},
    "mastersthesis": {
        "description": "A Master's thesis",
        "required": ["author", "title", "school", "year"],
        "optional": ["type", "address", "month", "note", "key"]},
    "misc": {
        "description": "For use when nothing else fits",
        "required": [],
        "optional": ["author", "title", "howpublished", "month", "year",
                     "note", "key"]},
    "phdthesis": {
        "description": "A Ph.D. thesis",
        "required": ["author", "title", "school", "year"],
        "optional": ["type", "address", "month", "note", "key"]},
    "proceedings": {
        "description": "The proceedings of a conference",
        "required": ["title", "year"],
        "optional": ["editor", ["volume", "number"], "series", "address",
                     "month", "publisher", "organization", "note", "key"]},
    "techreport": {
        "description": ("A report published by a school or other institution,"
                        "usually numbered within a series"),
        "required": ["author", "title", "institution", "year"],
        "optional": ["type", "number", "address", "month", "note", "key"]},
    "unpublished": {
        "description": ("A document having an author and title,"
                        "but not formally published"),
        "required": ["author", "title", "note"],
        "optional": ["month", "year", "key"]}
}

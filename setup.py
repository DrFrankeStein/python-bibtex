from setuptools import setup
import re


def version():
    with open('texbib/__init__.py', 'r') as init_file:
        _version = re.search('__version__ = \'([^\']+)\'', init_file.read()).group(1)
    return _version


setup(
    name='bibtex',
    version=version(),
    description='A simple, maintainable BibTeX parser using pyparsing',
    long_description='',
    url='https://github.com/DrFrankeStein/python-bibtex',
    author='Lars Franke',
    author_email='lars.ch.franke@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: Markup :: LaTeX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    keywords='bibtex latex',
    packages=['bibtex'],
    install_requires=['pyparsing'],
    extras_require={
        'yaml': ['pyyaml'],
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'bib2yaml=bibtex.utils:bib2yaml',
            'bib2json=bibtex.utils:bib2json'
        ],
    },
)

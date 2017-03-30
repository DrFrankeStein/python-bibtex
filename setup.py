from setuptools import setup
import sys, re


def version():
    with open('bibtex/__init__.py', 'r') as init_file:
        _version = re.search('__version__ = \'([^\']+)\'',
                             init_file.read()).group(1)
    return _version


def requirements():
    req = {
        'yaml': ['pyyaml'],
        'test': ['pytest'],
    }
    if sys.version_info < (2, 7):
        req['cli'] = ['argparse']
    return req


setup(
    name='bibtex',
    version=version(),
    description='A simple, maintainable BibTeX parser using pyparsing',
    long_description='',
    url='https://github.com/DrFrankeStein/python-bibtex',
    author='Lars Franke',
    author_email='lars.ch.franke@gmail.com',
    license='LGPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: Markup :: LaTeX',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)'
    ] + ['Programming Language :: Python :: {v}'.format(v=x) for x in
         '2 2.6 2.7 3 3.3 3.4 3.5 3.6'.split()],
    keywords='bibtex latex',
    packages=['bibtex'],
    install_requires=['pyparsing', 'setuptools'],
    extras_require=requirements(),
    entry_points={
        'console_scripts': [
            'bib2yaml=bibtex.utils:bib2yaml',
            'bib2json=bibtex.utils:bib2json'
        ],
    },
)

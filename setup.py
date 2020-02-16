#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from setuptools import setup, find_packages
from ebnf import version


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ""


AUTHOR = "Xiongfei Shi"
AUTHOR_EMAIL = "jenson.shixf@gmail.com"

CLASSIFIERS = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Object Brokering",
    "Topic :: System :: Distributed Computing",
]

DESCRIPTION = "An EBNF parser."
LONG_DESCRIPTION = read("README.rst")
KEYWORDS = ['EBNF', 'BNF', 'DSL']

INSTALL_REQUIRES = []

setup(
    name='ebnf',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    classifiers=CLASSIFIERS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
    keywords=KEYWORDS,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    packages=find_packages(),
    url="https://github.com/shixiongfei/ebnf",
    version=version
)

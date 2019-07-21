#!/usr/bin/env python

from distutils.core import setup

from googleplaces import __author__, __email__, __version__

DESCRIPTION = 'A simple wrapper around the Google Places API.'

setup(
    name = 'python-google-places',
    version = "1.4.3",
    url = 'http://github.com/slimkrazy/python-google-places',
    author = __author__,
    author_email = __email__,
    packages=['googleplaces'],
    install_requires=[
        'six',
    ],
    description = DESCRIPTION,
)

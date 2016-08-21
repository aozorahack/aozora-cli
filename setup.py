#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

import aozoracli.version

setup(
    name='aozora-cli',
    version=aozoracli.version.__version__,
    description='Aozora Bunko Command Line Tool',
    author='Yasuhiro Kiyota',
    author_email='yasuhiroki.duck@gmail.com',
    url='https://github.com/aozorahack/aozora-cli',
    scripts=['bin/aozora'],
    packages=['aozoracli'],
    install_requires=['requests', 'click', 'jmespath'],
    license="MIT",
)

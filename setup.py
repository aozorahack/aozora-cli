#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='aozora-cli',
    version='0.1',
    description='Aozora Bunko Command Line Tool',
    author='Yasuhiro Kiyota',
    author_email='yasuhiroki.duck@gmail.com',
    url='https://github.com/aozorahack/aozora-cli',
    scripts=['bin/aozora'],
    packages=['aozoracli'],
    install_requires=['requests', 'click', 'jmespath'],
)

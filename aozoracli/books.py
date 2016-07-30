#!/usr/bin/env python

import requests

import aozoracli.client

def main():
    print("Start aozora command line tool")
    books = aozoracli.client.get_books().json()
    print(books)

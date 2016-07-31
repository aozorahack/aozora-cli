#!/usr/bin/env python

import aozoracli.client
PATH_KEY = 'id'
PAYLOAD_KEYS = ['author', 'title']

def main(options):
    from .util import _filter, _parse_options
    options, id, payload = _parse_options(options, PATH_KEY, PAYLOAD_KEYS)
    books = aozoracli.client.get_books(id, payload).json()

    if books == None:
        print("Could not get aozora books data")
        return False

    for key in options.keys():
        if options[key] == None:
            continue
        books = _filter(books, key, options[key])

    if len(books) == 0:
        print("Not found books")
        return False

    return books

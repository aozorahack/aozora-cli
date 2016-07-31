#!/usr/bin/env python

import aozoracli.client
PATH_KEY = 'id'
PAYLOAD_KEYS = ['author', 'title']

def main(options):
    options, id, payload = _parse_options(options)
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

    print(books)
    return True

def _filter(books, key, value):
    return [b for b in books if b[key] == value]

def _parse_options(options):
    if options == None:
        return

    path = options.pop(PATH_KEY)

    payload = {}
    for key in PAYLOAD_KEYS:
        if options[key] == None:
            continue
        payload[key] = options.pop(key)

    return (options, path, payload)


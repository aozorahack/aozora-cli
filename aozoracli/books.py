#!/usr/bin/env python

import aozoracli.client

def main(options):
    books = aozoracli.client.get_books().json()

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
    print(key, value)
    return [b for b in books if b[key] == value]



#!/usr/bin/env python

def _filter(books, key, value):
    return [b for b in books if b[key] == value]

def _parse_options(options, path_key, payload_keys):
    if options == None:
        return

    path = options.pop(path_key)

    payload = {}
    for key in payload_keys:
        if not key in options or options[key] == None:
            continue
        payload[key] = options.pop(key)

    return (options, path, payload)


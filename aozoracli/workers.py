#!/usr/bin/env python

import aozoracli.client
PATH_KEY = 'id'
PAYLOAD_KEYS = ['name']

def main(options):
    from .util import _filter, _parse_options
    options, id, payload = _parse_options(options, PATH_KEY, PAYLOAD_KEYS)
    workers = aozoracli.client.get_workers(id, payload).json()

    if workers == None:
        print("Could not get aozora workers data")
        return False

    for key in options.keys():
        if options[key] == None:
            continue
        workers = _filter(workers, key, options[key])

    if len(workers) == 0:
        print("Not found workers")
        return False

    print(workers)
    return True


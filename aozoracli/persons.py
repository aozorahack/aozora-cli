#!/usr/bin/env python

import aozoracli.client
PATH_KEY = 'id'
PAYLOAD_KEYS = ['name']

def main(options):
    from .util import _parse_options
    options, id, payload = _parse_options(options, PATH_KEY, PAYLOAD_KEYS)
    persons = aozoracli.client.get_persons(id, payload).json()

    if persons == None:
        print("Could not get aozora persons data")
        return False

    if len(persons) == 0:
        print("Not found persons")
        return False

    return persons


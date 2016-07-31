#!/usr/bin/env python

import aozoracli.client

PAYLOAD_KEYS = ['name']

def main(options):
    options, payload = _parse_options(options)
    persons = aozoracli.client.get_persons(payload).json()

    if persons == None:
        print("Could not get aozora persons data")
        return False

    for key in options.keys():
        if options[key] == None:
            continue
        persons = _filter(persons, key, options[key])

    if len(persons) == 0:
        print("Not found persons")
        return False

    print(persons)
    return True

def _filter(persons, key, value):
    print(key, value)
    return [b for b in persons if b[key] == value]

def _parse_options(options):
    payload = {}
    for key in PAYLOAD_KEYS:
        if options[key] == None:
            continue
        payload[key] = options.pop(key)

    return (options, payload)


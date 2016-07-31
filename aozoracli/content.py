#!/usr/bin/env python

import aozoracli.client
PATH_KEY = 'id'
PAYLOAD_KEYS = ['format']

def main(options):
    output_format = options['format']

    from .util import _parse_options
    options, id, payload = _parse_options(options, PATH_KEY, PAYLOAD_KEYS)
    res = aozoracli.client.get_content(id, payload)

    return res.text


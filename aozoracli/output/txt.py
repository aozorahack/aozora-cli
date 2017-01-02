#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dump(res):
    return _format_print_txt(res)

def _format_print_txt(data):
    if isinstance(data, list):
        return "\n".join([_to_txt(d) for d in data])
    elif isinstance(data, dict):
        return _format_print_txt(d)
    else:
        return str(data)

def _to_txt(data):
    if data == None:
        return ""

    if isinstance(data, list):
        output = ""
        for d in data:
            output += _to_txt(d)
        return output
    elif isinstance(data, dict):
        sorted_keys = sorted(data.keys())
        sorted_values = []
        for key in sorted_keys:
            val = _to_txt(data[key])
            sorted_values.append(val)
        return " ".join(sorted_values)
    elif isinstance(data, int):
        return str(data)
    else:
        return data.encode("UTF-8")


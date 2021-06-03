#!/usr/bin/python3
"""
Module 4-from_json_string

Return python object represented by a JSON string (string)
"""


def from_json_string(my_str):
    """ Return object represented by a JSON string """
    import json

    return json.loads(my_str)

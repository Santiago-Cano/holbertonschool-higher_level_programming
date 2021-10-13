#!/usr/bin/python3
"""
Module 3-to_json_string
Return JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """ Return JSON representation of my_obj """
    import json

    return json.dumps(my_obj)

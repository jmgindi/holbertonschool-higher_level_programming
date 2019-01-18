#!/usr/bin/python3
import json

"""
module contains 1 function
    from_json_string
"""


def from_json_string(my_str):
    """ converts a JSON string to its matching object

    Args:
        my_str (obj:`str`): JSON string to convert
    """
    return json.loads(my_str)

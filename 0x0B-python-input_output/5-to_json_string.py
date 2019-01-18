#!/usr/bin/python3
import json
"""
module contains 1 function:
    to_json_string
"""


def to_json_string(my_obj):
    """ returns a JSON representation of my_obj

    Args:
        my_obj (obj:`obj`): any object
    """
    return json.dumps(my_obj)

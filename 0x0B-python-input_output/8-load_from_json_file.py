#!/usr/bin/python3
import json
"""
module contains 1 function:
    load_from_json_file
"""

def load_from_json_file(filename):
    """ loads an object from a json file

    Args:
        filename (obj:`str`): file to load object from
    """
    with open(filename) as f:
        return json.load(f)

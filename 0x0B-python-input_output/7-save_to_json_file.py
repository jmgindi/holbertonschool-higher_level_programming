#!/usr/bin/python3
import json
"""
module contains 1 function:
    save_to_json_file
"""

def save_to_json_file(my_obj, filename):
    """ saves an object to a text file using JSON
    representation

    Args:
        my_obj (obj:`obj`): object to save
        filename (obj:`str`): name of file
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

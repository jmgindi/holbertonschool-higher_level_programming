#!/usr/bin/python3
import json
"""
module contains 1 function:
    class_to_json
"""
def class_to_json(obj):
    """ returns a dict description of a class instance 
    for JSON serialization
    """
    return obj.__dict__

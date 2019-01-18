#!/usr/bin/python3
try:
    import json
    import sys
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '8-load_from_json_file').load_from_json_file
except ImportError:
    print("Import Error")
"""
script to add arguments to a JSON list
"""


try:
    a_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    a_list = []
for arg in sys.argv:
    if arg == sys.argv[0]:
        continue
    a_list.append(arg)
save_to_json_file(a_list, 'add_item.json')
